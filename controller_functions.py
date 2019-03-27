from flask import render_template, request
from config import db
from models import Task

def index():
    return render_template('index.html')

def create_task():
    task = Task(task=request.form['task'])
    print(task)
    db.session.add(task)
    db.session.commit()
    return "SUCCESS"

def task_list():
    task_list = Task.query.all()
    print(task_list)
    return render_template('partials/list.html', tasks=task_list)

def update_task(id):
    task = Task.query.get(id)
    change = request.form['change']
    task.task = change
    db.session.commit()
    return "SUCCESS"

def finish_task(id):
    task = Task.query.get(id)
    task.finished = True
    db.session.commit()
    return "SUCCESS"
