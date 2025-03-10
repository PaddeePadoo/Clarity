# app/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Document
from app.schemas import DocumentCreate, DocumentUpdate
from app.render import render_markdown_to_html

# Create a new document
async def create_document(db: AsyncSession, document: DocumentCreate):
    db_document = Document(
        title=document.title,
        content=document.content,
        html_content=render_markdown_to_html(document.content),  # ✅ Correctly setting HTML before saving
        needs_rerender=False
    )
    db.add(db_document)
    await db.commit()
    await db.refresh(db_document)
    return db_document

# Update an existing document
async def update_document(db: AsyncSession, document_id: int, document: DocumentUpdate):
    db_document = await db.get(Document, document_id)
    if db_document:
        if document.title:
            db_document.title = document.title
        if document.content:
            db_document.content = document.content
            db_document.html_content = render_markdown_to_html(document.content)  # ✅ Correctly re-rendering HTML
        await db.commit()
        await db.refresh(db_document)
        return db_document
    return None

# Delete a document
async def delete_document(db: AsyncSession, document_id: int):
    db_document = await db.get(Document, document_id)
    if db_document:
        await db.delete(db_document)
        await db.commit()
        return db_document
    return None

# Get all documents
async def get_documents(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Document).offset(skip).limit(limit))
    return result.scalars().all()

# Get a single document by ID
async def get_document(db: AsyncSession, document_id: int):
    result = await db.execute(select(Document).filter(Document.id == document_id))
    return result.scalar_one_or_none()