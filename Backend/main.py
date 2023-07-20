from fastapi import FastAPI
from routers.consulta import router as consulta_router
from routers.historia_clinica import router as historia_router
from routers.paciente import router as paciente_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


# Configura el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes de todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todas las cabeceras
    expose_headers=["Content-Disposition"],  # Exponer el header `Content-Disposition`
)



app.include_router(consulta_router)
app.include_router(historia_router)
app.include_router(paciente_router)