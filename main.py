# def main():
#     print("Hello from uv-tutorial!")


# if __name__ == "__main__":
#     main()

from fastapi import FastAPI, Request, Depends
from httpx import request

app = FastAPI(docs_url="/swagger")

@app.get("/")
def read_root():
    return { "Hello": "World" }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return { "item_id": item_id, "q": q }


@app.get("/request_headers")
def read_request_headers(request: Request):
    return { "accept": request.headers.get("accept") }


def test_depends(request: Request):
    print("test_depends called with request:", request)
    print(request.headers.get("authorization"))
    print(request.headers.get("user-agent"))
    print(request.method, request.url.path)
    return f"Depends works with request: {request.method} {request.url.path}"

@app.get("/check_depends")
def check_depends(msg: str = Depends(test_depends)):
    return { "message": msg }

@app.get("/docs")
def custom_docs():
    return { "message": "This is the custom docs endpoint" }


@app.middleware("http")
async def middleware_one(request: Request, call_next):
    print("Middleware ONE - before")
    response = await call_next(request)
    print("Middleware ONE - after")
    return response

@app.middleware("http")
async def middleware_two(request: Request, call_next):
    print("Middleware TWO - before")
    response = await call_next(request)
    print("Middleware TWO - after")
    return response