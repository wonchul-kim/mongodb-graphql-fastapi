from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

# import models as models

import asyncio


class Settings(BaseSettings):
    # database configurations
    MONGODB_URL: Optional[str] = None

    # JWT
    secret_key: str = "secret"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev"
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient(Settings().MONGODB_URL)
    print(f"=====================================================")
    print(f"* URL: {Settings().MONGODB_URL}")
    databases = await client.get_default_database()
    # print(f"* Databases: {databases}")

    # await init_beanie(
    #     database=client.get_default_database(), #document_models=models.__all__
    # )