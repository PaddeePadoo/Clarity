# app/main.py
from fastapi import FastAPI
from app.routes import document_routes

app = FastAPI()

# Include routes from document_routes
app.include_router(document_routes.router)

# Any other necessary configurations (middleware, etc.) can go here.