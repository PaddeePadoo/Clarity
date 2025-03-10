# schemas.py
from pydantic import BaseModel

class DocumentBase(BaseModel):
    title: str
    content: str

class DocumentCreate(DocumentBase):
    pass  # No `html_content` (backend generates it)

class DocumentUpdate(BaseModel):
    title: str | None = None
    content: str | None = None

class Document(DocumentBase):
    id: int
    html_content: str  # This is included in responses

    class Config:
        from_attributes = True