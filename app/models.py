
# app/models.py
from sqlalchemy import Column, Integer, String, Text, Boolean
from app.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    html_content = Column(Text)  # Stores rendered HTML content
    needs_rerender = Column(Boolean, default=False)  # Flag to check if re-render is needed