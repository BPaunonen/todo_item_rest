from flask import Flask, request
from database import get_all_todos, get_single_todo, create_todo, delete_todo, update_todo

app = Flask(__name__)

todo_list = [{"id":1, "content":"ASD"}, 
{"id":2, "content":"DSA"}, {"id":3, "content":"XXD"}]

@app.route("/")
def health_check():
    return {"status": "ok"}

@app.get("/todos")
def list_todos():
    return get_all_todos()

@app.get("/todos/<int:id>")
def list_todo(id):
    single_todo = get_single_todo(id)
    if single_todo is None:
        return {"status": "not found"},404
    return single_todo

@app.post("/todos")
def add_todo():
    input_item = request.json
    todo_id = create_todo(input_item["content"])
    single_todo = get_single_todo(todo_id)
    return single_todo


# @app.put("/todos/<int:id>")
# def update_todo(id):
#     updated_item = request.json
#     for todoitem in todo_list:
#         if todoitem["id"] == id:
#             content = updated_item["content"]
#             todoitem["content"] = content
#             return todoitem
#     return {"status": "not found"},404

@app.put("/todos/<int:id>")
def update_todo_controller(id):
    input_data = request.json
    items_updated = update_todo(input_data['content'], id)
    if items_updated >= 1:
        single_todo = get_single_todo(id)
        return single_todo
    else: 
        return {"status": "not found"},404

# @app.delete("/todos/<int:id>")
# def delete_todo(id):
#     for todoitem in todo_list:
#         if todoitem["id"] == id:
#             todo_list.remove(todoitem)
#             return todoitem
#     return {"status": "not found"},404

@app.delete("/todos/<int:id>")
def delete_a_todo(id):
    rowcount = delete_todo(id)
    print(rowcount)
    
    if rowcount >= 1:
        return "", 204
    else: 
        return {"status": "not found"},404
    
