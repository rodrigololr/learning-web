from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tarefas = []
contador_id = 1


class Tarefa(BaseModel):
    titulo: str
    id: int


@app.post("/tarefas/")
def criar_tarefa(tarefa: Tarefa):
    global contador_id
    nova_tarefa = {"id": contador_id, "titulo": tarefa.titulo} 
    tarefas.append(nova_tarefa) 
    contador_id += 1
    return {"mensagem": "Tarefa adiciona!", "tarefa": tarefa.titulo, "id": tarefa.id}


@app.get("/tarefas/")
def listar_tarefas():
    return {"tarefas": tarefas}
