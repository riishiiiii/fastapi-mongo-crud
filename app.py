from fastapi import FastAPI
import uvicorn
from items import router as items_router

app = FastAPI()

app.include_router(items_router, prefix="/items", tags=["items"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)
