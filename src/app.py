from datetime import datetime

from flask import Flask, request
from models import todo  # call model file

app = Flask(__name__)

todo = todo.Todo()


# todo routes

@app.route('/todos/', methods=['GET'])
def get_tasks():
    return todo.find({})


@app.route('/todos/', methods=['POST'])
def add_tasks():
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        created = datetime.now()
        response = todo.create({'title': title, 'body': body, 'created': created})
        return response, 201


if __name__ == '__main__':
    app.run()
