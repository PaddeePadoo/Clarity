# app/routes/document_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_db
from app.render import render_markdown_to_html

router = APIRouter()

@router.post("/documents/", response_model=schemas.Document)
async def create_document(document: schemas.DocumentCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_document(db=db, document=document)

@router.put("/documents/{document_id}", response_model=schemas.Document)
async def update_document(document: schemas.DocumentUpdate, document_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.update_document(db=db, document=document, document_id=document_id)

@router.get("/documents/{document_id}", response_model=schemas.Document)
async def get_document(document_id: int, db: AsyncSession = Depends(get_db)):
    db_document = await crud.get_document(db=db, document_id=document_id)
    if not db_document:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document

@router.get("/documents/", response_model=list[schemas.Document])
async def get_documents(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud.get_documents(db=db, skip=skip, limit=limit)


@router.delete("/documents/{document_id}", response_model=schemas.Document)
async def delete_document(document_id: int, db: AsyncSession = Depends(get_db)):
    db_document = await crud.delete_document(db=db, document_id=document_id)
    if not db_document:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document

@router.post("/documents/render_markdown", response_model=str)
async def render_markdown(document: schemas.DocumentCreate):
    return render_markdown_to_html(document.content)