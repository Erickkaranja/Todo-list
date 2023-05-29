#!/usr/bin/python3
import flask
from flask import Flask, jsonify
app = Flask(__name__)
task = [
    {'id':1, 'title':u'Buy groceries', 'description':'Milk, cheese, Pizza, fruit, Tylenol', 'done':False},
    {'id':2, 'title':u'Learn python', 'description':'Need to find a good pythontutorial from the web', 'done':False}]
'''simple RESTapi that uses a memory structure due to its simplisty.'''
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks':task})

if __name__ == "__main__":
    app.run(debug=True)
