import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")

@router.get("/cadastro-empresa.html")
async def cadastro_empresa():
    file_path = os.path.join(static_dir, "cadastro_empresa.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Página de cadastro de empresa não encontrada")

@router.get("/cadastro-obrigacao.html")
async def cadastro_obrigacao():
    file_path = os.path.join(static_dir, "cadastro_obrigacao.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Página de cadastro de obrigação não encontrada")

@router.get("/")
async def gestao_empresarial():
    file_path = os.path.join(static_dir, "index.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Página de gestão empresarial não encontrada")

@router.get("/list_obrigacoes.html")
async def list_obrigacoes_page():
    file_path = os.path.join(static_dir, "list_obrigacoes.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Página não encontrada")

@router.get("/list_empresa.html")
async def list_empresas_page():
    file_path = os.path.join(static_dir, "list_empresa.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Página não encontrada")
