from fastapi import FastAPI
from request_response_models.generate_request import GenerateRequest

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/generate")
async def generate(generate_request: GenerateRequest):
    return {"message": generate_request.board_name}
