from flask import Flask, jsonify, request, render_template
from models import Session, Task
from sqlalchemy import desc

app = Flask(__name__)

# 1. Serve the Dashboard
@app.route('/')
def index():
    return render_template('index.html')

# 2. API: Add a Task
@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.json
    session = Session()
    try:
        new_task = Task(task_name=data.get('name', 'New Task'))
        session.add(new_task)
        session.commit()
        return jsonify({"success": True, "id": new_task.id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

# 3. API: Get All Tasks (For live updates)
@app.route('/tasks')
def get_tasks():
    session = Session()
    try:
        # Get the last 10 tasks, newest first
        tasks = session.query(Task).order_by(desc(Task.id)).limit(10).all()
        return jsonify([t.to_dict() for t in tasks])
    finally:
        session.close()
        
# 4. API: Clear all tasks
@app.route('/tasks', methods=['DELETE'])
def clear_tasks():
    session = Session()
    try:
        # Delete all rows in the tasks table
        session.query(Task).delete()
        session.commit()
        return jsonify({"success": True, "message": "All tasks cleared."})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000)