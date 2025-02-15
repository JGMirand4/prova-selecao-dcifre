from fastapi import FastAPI
from database import engine, Base
from routers import empresas, obrigacoes, static

# CREATE TABLES
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Gestão de Empresas", version="1.0.0")

# ROUTERS
app.include_router(static.router, tags=["Páginas"])
app.include_router(empresas.router, tags=["Empresas"])
app.include_router(obrigacoes.router, tags=["Obrigacoes"])
