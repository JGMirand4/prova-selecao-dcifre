from database import engine, Base
from models import *

# CREATE MIGRATIONS
print("Criando migrações no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
