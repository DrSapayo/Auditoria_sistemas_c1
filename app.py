from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from controller import book_controllers
from database.database import lifespan

load_dotenv()

app = FastAPI(title="Auditoria en sistemas Liberia", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_ORIGIN", "*").split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_controllers.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the ReLib API"}