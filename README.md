# 📝 API de Tarefas em Python

Projeto simples de uma **API REST para gerenciamento de tarefas**, desenvolvido para estudo de backend com Python e FastAPI.

---

## 🚀 Tecnologias
- Python
- FastAPI
- Uvicorn

---

## 📦 Funcionalidades
- Criar tarefas
- Listar tarefas
- Atualizar tarefas
- Deletar tarefas

---

## 📁 Estrutura do projeto
api-tarefas-python/
├── app/
│ └── main.py
├── requirements.txt
└── README.md


---

## ▶️ Como executar o projeto

### 1. Instalar dependências
```bash
pip install -r requirements.txt
2. Iniciar a aplicação
uvicorn app.main:app --reload
🌐 Endpoints disponíveis
GET /
Retorna mensagem de status da API

POST /tarefas
Cria uma nova tarefa

GET /tarefas
Lista todas as tarefas

PUT /tarefas/{id}
Atualiza uma tarefa existente

DELETE /tarefas/{id}
Remove uma tarefa

📖 Documentação interativa
Após iniciar a aplicação, acesse:

Swagger UI
http://127.0.0.1:8000/docs

🎯 Objetivo do projeto
Praticar conceitos básicos de backend

Aprender criação de APIs REST

Utilizar FastAPI de forma simples e didática
