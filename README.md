# API de Gestão de Empresas 🏢

Esta API fornece endpoints para gerenciar empresas e suas obrigações acessórias, além de funcionalidades de upload de arquivos e auditoria de logs.

## Sumário

- [Recursos](#recursos)
- [Organização](#organização)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Execução](#instalação-e-execução)
- [Estrutura de Pastas](#estrutura-de-pastas)
- [Documentação](#documentação)
- [Testes](#testes)
- [Docker](#docker)
- [Sugestões de Melhoria](#sugestões-de-melhoria)
- [Licença](#licença)

---

## Organização

prova-selecao-dcifre/
├── __pycache__/
├── .pytest_cache/
├── routers/
│   ├── __pycache__/
│   ├── empresas.py
│   ├── obrigacoes.py
│   ├── static.py
│   └── uploads.py
├── static/
│   ├── cadastro_empresa.html
│   ├── cadastro_obrigacao.html
│   ├── index.html
│   ├── list_empresa.html
│   └── list_obrigacoes.html
├── venv/                      
├── .gitignore
├── audit_logs.py
├── audit.log
├── Dockerfile
├── main.py
├── make_migrations.py
├── models.py
├── readme.md
├── requirements_test.txt
├── schemas.py
├── requirements.txt
├── test.py
└── database.py


## Recursos

- **Empresas**: 
  - Criar, listar, buscar por ID, atualizar e excluir empresas.
- **Obrigações Acessórias**:
  - Criar, listar, buscar por ID, atualizar e excluir obrigações acessórias.
- **Upload de Arquivos**:
  - Enviar arquivos para o servidor e armazená-los em uma pasta específica (`uploads/`).
- **Auditoria de Logs**:
  - Registra ações (criação, atualização e exclusão) realizadas na aplicação.
- **Suporte a Deploy com Docker**:
  - Possibilidade de executar toda a aplicação em um container Docker.

---

## Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- (Opcional) Docker e Docker Compose para containerização

---

## Instalação e Execução

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/meu-usuario/projeto
   cd projeto

