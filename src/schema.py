from pydantic import BaseModel


class Items(BaseModel):
    name: str
    price: float
    is_offer: bool = None
