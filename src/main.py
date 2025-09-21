# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List


# class Todo(BaseModel):
#     id : int
#     name: str
#     descripton: str

# todos : List[Todo] = []

# api=FastAPI()

# @api.get("/")
# def home():
#     return {"message": "Hello World"}


# @api.get("/todo")
# def get_todo():
#     return todos

# @api.post("/todo")
# def post_todo(todo: Todo):
#     todos.append(todo)
#     return todos

# @api.put("/todo/{todo_id}")
# def update_todo(todo_id: int, updated_todo: Todo):
#     for index, todo in enumerate(todos):
#         if todo.id==todo_id:
#             todos[index]=updated_todo
#             return todos
#     return {"message": "error in updation"}

# @api.delete("/todo/{todo_id}")
# def delete_todo(todo_id: int):
#     for index, todo in enumerate(todos):
#         if todo.id==todo_id:
#             todos.pop(index)
#             return todos
#     return {"message": "error in deletion"}



from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    name: str
    des: str   # <-- match test field name

todos: List[Todo] = []

api = FastAPI()

@api.get("/")
def home():
    return {"Message": "Hello World"}  # <-- capital M

@api.get("/todo")
def get_todo():
    return todos

@api.post("/todo")
def post_todo(todo: Todo):
    todos.append(todo)
    return todo  # <-- return single todo

@api.put("/todo/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo  # <-- return single todo
    return {"message": "error in updation"}

@api.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            removed = todos.pop(index)
            return removed  # <-- return deleted todo
    return {"message": "error in deletion"}
