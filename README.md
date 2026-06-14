# Controle-se - Gerenciador de Gastos Pessoais

O **Controle-se** é uma aplicação web desenvolvida em Django projetada para facilitar o controle financeiro pessoal. A aplicação permite que o usuário registre, visualize, edite e exclua despesas diárias, acompanhe gráficos e resumos de gastos por categorias, e visualize a cotação do dólar atualizada em tempo real via integração com API externa.

---

## 🚀 Links do Projeto

*   **Repositório Oficial:** [GitHub - gerenciadordegastos](https://github.com/PhilippeJardim/gerenciadordegastos)
*   **Aplicação Publicada (Deploy):** [Controle-se no Render](https://controle-se-ypee.onrender.com/)

---

## 👥 Integrantes do Grupo

| Nome Completo | Matrícula | GitHub |
| :--- | :--- | :--- |
| Philippe Santos Lopes Jardim | 22452544 | [@PhilippeJardim](https://github.com/PhilippeJardim) |

---

## 🛠️ Tecnologias e Stack Utilizadas

*   **Backend:** Python 3.13.x / Django 4.2.x
*   **Banco de Dados:**
    *   **Desenvolvimento/Testes:** SQLite (Local)
    *   **Produção (Nuvem):** PostgreSQL (Supabase)
*   **Servidor de Arquivos Estáticos:** WhiteNoise (otimização e cache de arquivos estáticos em produção)
*   **Qualidade e Estilo de Código:** Ruff (linter rápido)
*   **Testes Automatizados:** Pytest / pytest-django
*   **Integração Contínua (CI):** GitHub Actions

---

## 💻 Guia para Execução Local

### 1. Clonar o Repositório
```bash
git clone https://github.com/PhilippeJardim/gerenciadordegastos.git
cd gerenciadordegastos
```

### 2. Configurar o Ambiente Virtual (venv)
```bash
# Criar o ambiente virtual
python -m venv .venv

# Ativar no Windows:
.venv\Scripts\activate

# Ativar no Linux/Mac:
source .venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente
Crie um arquivo chamado `.env` na raiz do projeto (mesmo diretório do `manage.py`) e adicione as seguintes chaves:
```env
# Configurações do Django
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=django-insecure-sua-chave-secreta-de-desenvolvimento

# Conexão com o Banco de Dados (PostgreSQL na Nuvem ou SQLite)
# Caso queira usar o SQLite local para desenvolvimento rápido, deixe a linha abaixo comentada.
# DATABASE_URL=postgresql://usuario:senha@seu-host.neon.tech/nome-do-banco?sslmode=require
```

### 5. Executar as Migrações do Banco de Dados
```bash
python manage.py migrate
```

### 6. Executar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```
Acesse a aplicação em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Testes e Qualidade de Código

### Rodar os Testes Automatizados
O projeto utiliza `pytest` para testes unitários e de integração:
```bash
pytest
```

### Rodar a Verificação de Linting (Ruff)
Para validar os padrões e a qualidade de estilo do código:
```bash
ruff check .
```

---

## ⚙️ Pipeline de Integração Contínua (GitHub Actions)

A pipeline de CI está configurada no arquivo `.github/workflows/ci.yml` e roda de forma automática em todo **Push** ou **Pull Request (PR)** voltados para as branches `main` e `entrega-intermediaria`.

A pipeline executa as seguintes etapas:
1. Setup do ambiente Python 3.13.
2. Instalação das dependências do `requirements.txt`.
3. Verificação de estilo com o `ruff`.
4. Execução de todos os testes automatizados com o `pytest`.

*Obs: A pipeline precisa estar "verde" (aprovada) para que os PRs possam ser mesclados na branch principal.*