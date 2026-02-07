from flask import Blueprint, request

tasks_bp = Blueprint("tasks", __name__)

#Temp in memory store of task data

TASKS = []
NEXT_TASK_ID = 1

@tasks_bp.get("/")
def list_tasks():
    return TASKS

@tasks_bp.post("/")
def create_task():
    global NEXT_TASK_ID
    data = request.get_json(silent=True) or {}

    author_user_id = data.get("author_user_id")
    helper_user_id = data.get("helper_user_id")
    title = data.get("title")

    if not author_user_id or not title:
        return {"error": "author_user_id and title are required"}, 400
    
    task = {
        "id": NEXT_TASK_ID,
        "author_user_id": author_user_id,
        "helper_user_id": helper_user_id,
        "title": title
    }
    TASKS.append(task)
    NEXT_TASK_ID += 1

    return task, 201