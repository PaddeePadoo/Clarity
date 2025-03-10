#app/routes/api_auth.py

from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "Login endpoint (to be implemented)"}
