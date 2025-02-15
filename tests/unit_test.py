import pytest
from fastapi.testclient import TestClient
from main import app
from database import Base, SessionLocal
from sqlalchemy.orm import Session

client = TestClient(app)

def clear_db():
    # REMOVE ALL DATA FROM DATABASE
    with SessionLocal() as db:
        db.query(Base.metadata.tables["obrigacoes_acessorias"]).delete()
        db.query(Base.metadata.tables["empresas"]).delete()
        db.commit()

# FIXTURES TO CLEAR DATABASE BEFORE AND AFTER TESTS
@pytest.fixture(autouse=True)
def run_around_tests():
    clear_db()
    yield
    clear_db()

### TESTS EMPRESA ###

def test_create_empresa():
    response = client.post("/empresas/", json={
        "nome": "Empresa Teste",
        "cnpj": "11111111111111",
        "endereco": "Rua Teste, 123",
        "email": "teste@empresa.com",
        "telefone": "11999999999"
    })
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["nome"] == "Empresa Teste"

def test_get_empresa():
    # CREATE EMPRESA
    response = client.post("/empresas/", json={
        "nome": "Empresa Get",
        "cnpj": "22222222222222",
        "endereco": "Rua Get, 456",
        "email": "get@empresa.com",
        "telefone": "11988888888"
    })
    assert response.status_code == 200
    empresa_id = response.json()["id"]

    # GET EMPRESA
    get_response = client.get(f"/empresas/{empresa_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["nome"] == "Empresa Get"

def test_update_empresa():
    # CREATE EMPRESA
    response = client.post("/empresas/", json={
        "nome": "Empresa Update",
        "cnpj": "33333333333333",
        "endereco": "Rua Update, 789",
        "email": "update@empresa.com",
        "telefone": "11977777777"
    })
    assert response.status_code == 200
    empresa_id = response.json()["id"]

    # UPDATE EMPRESA
    update_data = {
        "nome": "Empresa Update Modified",
        "cnpj": "33333333333333",
        "endereco": "Rua Update, 789",
        "email": "update@empresa.com",
        "telefone": "11977777777"
    }
    update_response = client.put(f"/empresas/{empresa_id}", json=update_data)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["nome"] == "Empresa Update Modified"

def test_delete_empresa():
    # CREATE EMPRESA
    response = client.post("/empresas/", json={
        "nome": "Empresa Delete",
        "cnpj": "44444444444444",
        "endereco": "Rua Delete, 101",
        "email": "delete@empresa.com",
        "telefone": "11966666666"
    })
    assert response.status_code == 200
    empresa_id = response.json()["id"]

    # DELETE EMPRESA
    delete_response = client.delete(f"/empresas/{empresa_id}")
    assert delete_response.status_code == 200

    # VERIFY THAT EMPRESA DOES NOT EXIST
    get_response = client.get(f"/empresas/{empresa_id}")
    assert get_response.status_code == 404

### TESTS Obrigações ###

def test_create_obrigacao():
    # CREATE EMPRESA
    response = client.post("/empresas/", json={
        "nome": "Empresa Obrigacao",
        "cnpj": "55555555555555",
        "endereco": "Rua Obrigacao, 202",
        "email": "obrigacao@empresa.com",
        "telefone": "11955555555"
    })
    assert response.status_code == 200
    empresa_id = response.json()["id"]

    # CREATE OBRIGACAO
    obrigacao_data = {
        "nome": "Obrigacao Teste",
        "periodicidade": "Mensal",
        "empresa_id": empresa_id
    }
    obrigacao_response = client.post("/obrigacoes/", json=obrigacao_data)
    assert obrigacao_response.status_code == 200
    data = obrigacao_response.json()
    assert data["nome"] == "Obrigacao Teste"
    assert data["periodicidade"] == "Mensal"

def test_update_and_delete_obrigacao():
    # CREATE EMPRESA
    response = client.post("/empresas/", json={
        "nome": "Empresa Obrigacao 2",
        "cnpj": "66666666666666",
        "endereco": "Rua Obrigacao, 303",
        "email": "obrigacao2@empresa.com",
        "telefone": "11944444444"
    })
    assert response.status_code == 200
    empresa_id = response.json()["id"]

    # CREATE OBRIGACAO
    obrigacao_data = {
        "nome": "Obrigacao Para Atualizar",
        "periodicidade": "Semanal",
        "empresa_id": empresa_id
    }
    obrigacao_response = client.post("/obrigacoes/", json=obrigacao_data)
    assert obrigacao_response.status_code == 200
    obrigacao_id = obrigacao_response.json()["id"]

    # UPDATE OBRIGACAO
    update_data = {
        "nome": "Obrigacao Atualizada",
        "periodicidade": "Diária",
        "empresa_id": empresa_id
    }
    update_response = client.put(f"/obrigacoes/{obrigacao_id}", json=update_data)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["nome"] == "Obrigacao Atualizada"
    assert data["periodicidade"] == "Diária"

    # DELETE OBRIGACAO
    delete_response = client.delete(f"/obrigacoes/{obrigacao_id}")
    assert delete_response.status_code == 200

    # VERIFY THAT OBRIGACAO DOES NOT EXIST
    get_response = client.get(f"/obrigacoes/{obrigacao_id}")
    assert get_response.status_code == 404
