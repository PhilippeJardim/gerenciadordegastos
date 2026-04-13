Controle-se é uma aplicação simples criada para ajudar na organização dos gastos pessoais de pessoas que tem dificuldade em registrar suas despesas.
A aplicação adiciona, edita e exclui as despesas desejadas pelo cliente. Pode-se listar as despesas registradas na aplicação e usar filtros para selecionar as categorias que deseja ver para poder saber os gastos totais gerais e, também, os gastos de cada categoria.

# Tecnologias utilizadas
Python 3.13;

Django 4.2;

SQLite;

pytest / pytest-django;

ruff;

GitHub Actions;

# Guia para instalação:
# Clone o repositório
git clone https://github.com/PhilippeJardim/gerenciadordegastos

cd https://github.com/PhilippeJardim/gerenciadordegastos

# Crie e ative o ambiente virtual
python -m venv .venv

.venv\Scripts\activate  # Windows

source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Execução

python manage.py runserver

Acesse em: http://127.0.0.1:8000

# Testes

pytest

# Lint

ruff check .

# Versão
1.0.0

# Autor
Philippe Santos Lopes Jardim — (https://github.com/PhilippeJardim)

# Repositório
(https://github.com/PhilippeJardim/gerenciadordegastos)