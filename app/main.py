from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import form

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="KPA Form API",
    description="Implements two APIs: submit form and fetch forms by user ID",
    version="1.0.0"
)

# Include API routes
app.include_router(form.router)
