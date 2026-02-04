from fastapi import FastAPI
import json
import os

app = FastAPI()

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)


tarefas = carregar_tarefas()

@app.get("/")
def home():
    return {"mensagem": "API de tarefas Mag rodando 🚀"}

@app.get("/tarefas")
def listar_tarefas():
    return tarefas

@app.post("/tarefas")
def criar_tarefa(titulo: str):
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    return nova_tarefa


@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefas.remove(tarefa)
            return {"mensagem": "Tarefa removida com sucesso"}
    return {"erro": "Tarefa não encontrada"}

@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, titulo: str):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["titulo"] = titulo
            return tarefa
    return {"erro": "Tarefa não encontrada"}

