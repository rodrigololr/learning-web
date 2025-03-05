from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tarefas = []  # array para guardar todas as tarefas
contador_id = 1  # variavel para criar id's

# class de tarefa para guardar o titulo e outras informações se quiser


class Tarefa(BaseModel):
    titulo: str

# class para atualizar tarefas


class TarefaAtualizada(BaseModel):
    titulo: str


# criar a tarefa
# recebe a tarefa e cria um id para ela automaticamente
@app.post("/tarefas/")
def criar_tarefa(tarefa: Tarefa):
    global contador_id
    nova_tarefa = {"id": contador_id, "titulo": tarefa.titulo}
    tarefas.append(nova_tarefa)
    contador_id += 1
    return {"mensagem": "Tarefa adiciona!", "tarefa": tarefa.titulo, "id": contador_id - 1}

# Listar as tarefas


@app.get("/tarefas/")
def listar_tarefas():
    return {"tarefas": tarefas}


# deletar a tarefa
@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    global tarefas
    # permite iterar sobre uma lista e, ao mesmo tempo, pegar o índice de cada item
    for i, tarefa in enumerate(tarefas):
        if tarefa["id"] == id:
            del tarefas[i]
            return {"mensagem": "Tarefa removida com sucesso!"}
    return {"erro": "Tarefa não encontrada!"}


# Editar a tarefa
@app.put("/tarefas/{id}/")
def editar(id: int, nova_tarefa: TarefaAtualizada):
    global tarefas
    for i, tarefa in enumerate(tarefas):
        if tarefa["id"] == id:

            tarefas[i]["titulo"] = nova_tarefa.titulo

            return {"mensagem": "Tarefa editada!", "tarefa": tarefas[i]}
    return {"erro": "Erro ao editar tarefa"}
