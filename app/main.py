"""Main entry point for CDRL service API"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routers import dd1423


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dd1423.router)


@app.get("/gov/")
async def root():
    """Create root route"""
    return {"message": "Hello CDRL service"}
