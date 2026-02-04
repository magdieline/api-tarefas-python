from fastapi import FastAPI

app = FastAPI()

tarefas = []

@app.get("/")
def home():
    return {"mensagem": "API de tarefas Mag rodando 🚀"}

@app.get("/tarefas")
def listar_tarefas():
    return tarefas

@app.post("/tarefas")
def criar_tarefa(titulo: str):
    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo
    }
    tarefas.append(tarefa)
    return tarefa

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefas.remove(tarefa)
            return {"mensagem": "Tarefa removida com sucesso"}
    return {"erro": "Tarefa não encontrada"}
