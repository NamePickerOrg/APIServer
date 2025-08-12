# 主入口，为了保证整体可维护性，主要功能分散在api下各个程序中
from fastapi import FastAPI,status
app = FastAPI

@app.get("/")
def hello():
    return {"resp":"Hello World"}

@app.get("/version")
def version():
    return {
        "version":"NamePicker API Server v0.0.1",
        "codename":"Elysia",
        "protocol":"v1"
    }
