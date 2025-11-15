from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

cliente = None
db = None

'''LIFESPAN DA APLICACION FASTAPI PARA CONEXION A MONGODB'''
@asynccontextmanager
async def lifespan(app: FastAPI):

    global cliente, db

    mongo_uri = "mongodb+srv://admin:admin@cluster0.mkvaa9f.mongodb.net/?appName=Cluster0"
    cliente = AsyncIOMotorClient(mongo_uri)
    db = cliente["ReLib"]

    try:
        yield # Aqui corre a aplicacion
    finally:
        cliente.close()

'''FUNCION PARA INICIALIZAR LA CONEXION A LA BASE DE DATOS EN EL APP FASTAPI
def init_db(app: FastAPI, mongo_uri: str, db_name: str= 'ReLib'):
    @app.on_event("startup")
    async def startup_db_client():
        nonlocal mongo_uri
        global cliente, db
        if not mongo_uri:
            mongo_uri = "mongodb+srv://admin:admin@cluster0.mkvaa9f.mongodb.net/?appName=Cluster0"
        cliente = AsyncIOMotorClient(mongo_uri)
        db = cliente[db_name]

    @app.on_event("shutdown")
    async def shutdown_db_client():
        global cliente
        cliente.close()
'''