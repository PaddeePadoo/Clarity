app/
│
├── main.py              # Entry point for the FastAPI app
├── models.py            # SQLAlchemy models
├── database.py          # Database setup and session management
├── crud.py              # CRUD operations
├── schemas.py           # Pydantic schemas
├── render.py            # Logic for rendering documents
└── __init__.py          # Makes the directory a package
    routes/
    │
    ├── document_routes.py
    alembic/
    │
    ├── env.py               # Alembic migration configuration

docker-compose.yml       # Docker compose file
Dockerfile               # Docker setup file
wait-for-it.sh           # Script to wait for the DB to be ready before app starts
.env                     # dot env file for storing environment variables