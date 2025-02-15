from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import SessionLocal
from audit_logs import log_action

router = APIRouter()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoriaResponse)
def create_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = models.ObrigacaoAcessoria(
        nome=obrigacao.nome,
        periodicidade=obrigacao.periodicidade,
        empresa_id=obrigacao.empresa_id
    )
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    log_action("system", "CREATE", f"Obrigação {obrigacao.nome} criada para empresa {obrigacao.empresa_id}")
    return db_obrigacao

@router.get("/obrigacoes/", response_model=List[schemas.ObrigacaoAcessoriaResponse])
def list_obrigacoes(db: Session = Depends(get_db)):
    return db.query(models.ObrigacaoAcessoria).all()

@router.get("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoriaResponse)
def get_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return obrigacao

@router.put("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoriaResponse)
def update_obrigacao(obrigacao_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    
    for key, value in obrigacao.dict().items():
        setattr(db_obrigacao, key, value)

    db.commit()
    db.refresh(db_obrigacao)
    log_action("system", "UPDATE", f"Obrigação {obrigacao.nome} atualizada")
    return db_obrigacao

@router.delete("/obrigacoes/{obrigacao_id}")
def delete_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    
    db.delete(obrigacao)
    db.commit()
    log_action("system", "DELETE", f"Obrigação {obrigacao.nome} deletada")
    return {"message": "Obrigação deletada com sucesso"}
