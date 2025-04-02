from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id2}")
async def read_user_item(item_id2: str, width: float, height: float):
    item = {"item_id": item_id2, "width": width, "height": height, "Area": width*height}
    return item
    