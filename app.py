from flask import Flask, render_template, request, redirect
from task_manager import Task, TaskManager, UrgentTask
from datetime import datetime
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
manager = TaskManager()

def calculate_time_left(deadline_str):
    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
        today = datetime.now()
        delta = (deadline - today).days
        return f"{delta} day(s) left" if delta >= 0 else "Overdue"
    except:
        return "Invalid date"

@app.route('/')
def index():
    tasks = manager.get_all_tasks()
    for task in tasks:
        task["time_left"] = calculate_time_left(task["deadline"])
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    deadline = request.form['deadline']
    description = request.form.get('description', '')
    priority = request.form.get('priority', 'Normal')
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if priority == 'Urgent':
        task = UrgentTask(title=title, created_at=created_at, deadline=deadline, description=description)
    else:
        task = Task(title=title, created_at=created_at, deadline=deadline, description=description, priority=priority)
    
    manager.add_task(task)
    return redirect('/')

@app.route('/done/<task_id>')
def mark_done(task_id):
    manager.mark_done(ObjectId(task_id))
    return redirect('/')

@app.route('/delete/<task_id>')
def delete_task(task_id):
    manager.delete_task(ObjectId(task_id))
    return redirect('/')

@app.route('/filter/priority/<priority>')
def filter_by_priority(priority):
    tasks = manager.get_tasks_by_priority(priority)
    for task in tasks:
        task["time_left"] = calculate_time_left(task["deadline"])
    return render_template('index.html', tasks=tasks)

@app.route('/filter/status/<status>')
def filter_by_status(status):
    is_done = True if status == 'done' else False
    tasks = manager.get_tasks_by_status(is_done)
    for task in tasks:
        task["time_left"] = calculate_time_left(task["deadline"])
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
