from flask import Flask, request


app = Flask(__name__)

todo_list = [{"id":1, "content":"ASD"}, 
{"id":2, "content":"DSA"}, {"id":3, "content":"XXD"}]

@app.route("/")
def health_check():
    return {"status": "ok"}

@app.get("/todos")
def list_todos():
    return todo_list

@app.get("/todos/<int:id>")
def list_todo(id):
    for todoitem in todo_list:
        if todoitem["id"] == id:
            return todoitem
    return {"status": "not found"},404

@app.post("/todos")
def add_todo():
    todo_item = request.json
    new_id = todo_list[-1]["id"]+1 
    todo_item["id"] = new_id
    todo_list.append(todo_item)
    return todo_item

@app.put("/todos/<int:id>")
def update_todo(id):
    updated_item = request.json
    for todoitem in todo_list:
        if todoitem["id"] == id:
            content = updated_item["content"]
            todoitem["content"] = content
            return todoitem
    return {"status": "not found"},404

@app.delete("/todos/<int:id>")
def delete_todo(id):
    for todoitem in todo_list:
        if todoitem["id"] == id:
            todo_list.remove(todoitem)
            return todoitem
    return {"status": "not found"},404