from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "success"}

@app.get("/{key}")
async def check(key: str):
    return key