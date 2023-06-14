from fastapi import FastAPI
from routers.consulta import router as consulta_router
from routers.historia_clinica import router as historia_router
from routers.paciente import router as paciente_router

app = FastAPI()

app.include_router(consulta_router)
app.include_router(historia_router)
app.include_router(paciente_router)