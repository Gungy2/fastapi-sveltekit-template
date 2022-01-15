import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hello from the backend!"


def dev():
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)


def start():
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, workers=2)


if __name__ == "__main__":
    dev()
