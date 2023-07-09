# from fastapi import FastAPI 
# from config.config import initiate_database

# app = FastAPI()

# @app.on_event("startup")
# async def start_database():
#     print(f"STARTUP-EVENT")
#     await initiate_database()


# @app.get("/", tags=["Root"])
# async def read_root():
#     return {"message": "Welcome to this fantastic app."}

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import inspect 

app = FastAPI()

client = AsyncIOMotorClient('mongodb://aiv-mongodb:27017')

@app.get('/get-databases')
async def read_item():
    try:
        databases = await client.list_database_names()
        # db = await client.get_default_database()
    except Exception as e:
        print(f"Error: {e}")

    print(f"* [{inspect.currentframe().f_code.co_name}]")
    print(f"    - Databases: {databases}")
    return databases
    
@app.on_event("startup")
async def start_database():
    print(f"=============================================================")
    print(f"* [{inspect.currentframe().f_code.co_name}]")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fastapi app."}
