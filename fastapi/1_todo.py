from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
todos = []


class Todo_data(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False


@app.get("/")
def home():
    return {"message": "Todo API running"}


# CREATE
@app.post("/todos")
def create_todo(todo: Todo_data):
    todos.append(todo)
    return todo


# READ All
@app.get("/todos")
def get_todos():
    return todos


# READ ONE
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo

    return {"message": "Not found"}


# UPDATE
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo_data):
    for todo in todos:
        if todo.id == todo_id:
            todo.title = updated_todo.title
            todo.description = updated_todo.description
            todo.completed = updated_todo.completed

            return todo

    return {"message": "Not found"}


# DELETE
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Deleted"}

    return {"message": "Not found"}
