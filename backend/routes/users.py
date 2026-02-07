from flask import Blueprint, request
users_bp = Blueprint("users", __name__)

#Temp in memory store of user data
USERS = []
NEXT_USER_ID = 1

@users_bp.get("/")
def list_users():
    return[{"id": u["id"], "username": u["username"]} for u in USERS]

@users_bp.post("/")
def create_user():
    global NEXT_USER_ID
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "username and password are required"}, 400
    
    if any(u["username"] == username for u in USERS):
        return {"error": "username already exists"}, 409
    
    user = {"id": NEXT_USER_ID, "username": username, "hash": f"not-hashed:{password}"}
    USERS.append(user)
    NEXT_USER_ID += 1

    return {"id": user["id"], "username": user["username"]}, 201