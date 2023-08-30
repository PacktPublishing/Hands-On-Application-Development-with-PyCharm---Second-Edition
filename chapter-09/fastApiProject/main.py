from fastapi import FastAPI, status, HTTPException

app = FastAPI()
names = ["Bruce", "Karina", "Kitty", "Phoebe"]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api/v1/names")
async def get_names():
    return [{"id": idx, "name": name} for idx, name in enumerate(names)]


@app.post("/api/v1/names", status_code=status.HTTP_201_CREATED)
async def create_name(name: dict):
    new_name = name["name"]
    names.append(new_name)
    return {"message": "Name added successfully"}


@app.put("/api/v1/names")
async def update_name(update_data: dict):
    id = update_data["id"]

    if not isinstance(id, int):
        raise HTTPException(status_code=400, detail="ID must be an integer")

    name = update_data["name"]

    if id >= len(names):
        raise HTTPException(status_code=404, detail="Name not found")

    names[id] = name
    return {"message": "Name updated successfully"}


@app.delete("/api/v1/names/{id}")
async def delete_name(id: int):
    if id >= len(names):
        raise HTTPException(status_code=404, detail="Name not found")

    deleted_name = names.pop(id)
    return {"message": f"Deleted name: {deleted_name}"}
