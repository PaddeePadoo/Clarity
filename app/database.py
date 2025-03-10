# app/database.py
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
import os

# Define Base before creating the engine
Base = declarative_base()

# Generate the database URL dynamically
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://myuser:mypassword@db:5432/mydatabase"
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)

# Create an async session maker
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
