from fastapi import FastAPI
from controller.user_controllers import router as user_router
from controller.class_controllers import router as class_router
from controller.tutor_availability_controllers import router as tutor_availability_router

app = FastAPI()

# Registrar rutas
app.include_router(user_router)
app.include_router(class_router)
app.include_router(tutor_availability_router)
