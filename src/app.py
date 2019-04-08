from flask import Flask, request, jsonify
from models import todo  # call model file
from flask_cors import CORS  # to avoid cors error in different frontend like react js or any other

app = Flask(__name__)
CORS(app)

todo = todo.Todo()


# todo routes
@app.route('/todos/', methods=['GET'])
def get_tasks():
    return jsonify(todo.find({})), 200


@app.route('/todos/<string:todo_id>/', methods=['GET'])
def get_task(todo_id):
    return todo.find_by_id(todo_id), 200


@app.route('/todos/', methods=['POST'])
def add_tasks():
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        response = todo.create({'title': title, 'body': body})
        return response, 201


@app.route('/todos/<string:todo_id>/', methods=['PUT'])
def update_tasks(todo_id):
    if request.method == "PUT":
        title = request.form['title']
        body = request.form['body']
        response = todo.update(todo_id, {'title': title, 'body': body})
        return response, 201


@app.route('/todos/<string:todo_id>/', methods=['DELETE'])
def delete_tasks(todo_id):
    if request.method == "DELETE":
        todo.delete(todo_id)
        return "Record Deleted"


if __name__ == '__main__':
    app.run(debug=True)
