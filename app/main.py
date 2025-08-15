# 主入口，为了保证整体可维护性，主要功能分散在api下各个程序中
from fastapi import FastAPI,status,HTTPException
from . import api
app = FastAPI()

# Hello World 
@app.get("/")
def hello():
    return {"resp":"Hello World"}

# /version
# 输出版本信息
@app.get("/version")
def version():
    return {
        "version":"NamePicker API Server v0.0.1",
        "codename":"Elysia",
        "protocol":"v1"
    }

# /pick
# 抽选
@app.get("/pick/{name_list}")
def choose(name_list,sex_favor:int=-1,num_favor:int=-1,allow_repeat:bool=False,num:int=1):
    res = api.name.choose(name_list,sex_favor,num_favor,allow_repeat,num)
    if res ==  "nothing":
        raise HTTPException(404)
    else:
        rx = []
        for i in res:
            rx.append(i)
        return {"result":rx}

# /list
# 名单管理