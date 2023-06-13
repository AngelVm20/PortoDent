from fastapi import FastAPI
from routers import paciente, historia_clinica, consulta

app = FastAPI()

app.include_router(paciente.router)
app.include_router(historia_clinica.router)
app.include_router(consulta.router)
