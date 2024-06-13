from fastapi import APIRouter, Depends, Query
from database import get_db
from schema import Items
from pymongo.errors import DuplicateKeyError
from motor.core import AgnosticDatabase
from typing import Optional

router = APIRouter()


@router.post("/")
async def add_items(item: Items, db: AgnosticDatabase = Depends(get_db)) -> dict:
    """_summary_

    Args:
        item (Items): Items object
        db (AgnosticDatabase, optional): Defaults to Depends(get_db).

    Returns:
        dict: id of the inserted item
    """

    try:
        result = await db.items.insert_one(item.model_dump())
    except DuplicateKeyError:
        return {"error": "Item with this name already exists"}
    return {"id": str(result.inserted_id)}


@router.get("/")
async def get_items(
    name: Optional[str] = Query(
        None, title="Name of the item", description="Name of the item to search for"
    ),
    is_offer: Optional[bool] = Query(
        None, title="Offer status", description="Offer status of the item to search for"
    ),
    db: AgnosticDatabase = Depends(get_db),
) -> list[Items]:
    """_summary_

    Returns:
        items: list of created Items
    """

    query = {}
    if name:
        query["name"] = name
    if is_offer:
        query["is_offer"] = is_offer
    items = db.items.find(query)
    return [Items(**item) async for item in items]


@router.get("/{name}")
async def get_item(name: str, db: AgnosticDatabase = Depends(get_db)) -> Items | dict:
    """_summary_

    Args:
        name (str): name of the item to search for
        db (AgnosticDatabase, optional): Defaults to Depends(get_db).

    Returns:
        Items | dict: item with name or error message
    """
    item = await db.items.find_one({"name": name})
    if item:
        return Items(**item)
    return {"error": "item not found"}


@router.put("/{name}")
async def update_item(
    name: str, item: Items, db: AgnosticDatabase = Depends(get_db)
) -> dict:
    """_summary_

    Args:
        name (str): name of the item to search for
        item (Items): items object with updated values
        db (AgnosticDatabase, optional):  Defaults to Depends(get_db).

    Returns:
        messgae: message of the update
    """
    db.items.update_one({"name": name}, {"$set": item.model_dump()})
    return {"message": "item updated"}


@router.delete("/{name}")
async def delete_item(name: str, db: AgnosticDatabase = Depends(get_db)) -> dict:
    """_summary_

    Args:
        name (str): name of the item to delete
        db (AgnosticDatabase, optional): _description_. Defaults to Depends(get_db).

    Returns:
        message: message of the delete
    """
    db.items.delete_one({"name": name})
    return {"message": "item deleted"}
