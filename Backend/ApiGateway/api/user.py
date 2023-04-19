from flask import Blueprint, jsonify, request, abort
import requests

user = Blueprint("user", __name__)

@user.route("/")
def home():
    return jsonify({"message": "hello"})

@user.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data.get("email") or not data.get("password")or not data.get("first_name")or not data.get("last_name"):
        abort(400, description = "invalid credentials")
    url = "http://localhost:8001/api/v1/users/"
    response = requests.post(url, json = data)
    if response.status_code != 201:
        return jsonify(response.reason), response.status_code
    return jsonify(response.json()), response.status_code

@user.route("/token", methods=["POST"])
def token():
    data = request.get_json()
    if not data.get("email") or not data.get("password"):
        abort(400, description = "invalid credentials")
    url = "http://localhost:8001/api/v1/jwt/create/"
    response = requests.post(url, json = data)
    if response.status_code != 200:
        return jsonify(response.reason), response.status_code
    return jsonify(response.json()), response.status_code

@user.route("/refresh", methods=["POST"])
def refresh():
    data = request.get_json()
    if not data.get("refresh"):
        abort(400, description = "invalid credentials")
    url = "http://localhost:8001/api/v1/jwt/refresh/"
    response = requests.post(url, json = data)
    if response.status_code != 200:
        return jsonify(response.reason), response.status_code
    return jsonify(response.json()), response.status_code

@user.route("/verify", methods=["POST"])
def verify():
    data = request.get_json()
    if not data.get("token"):
        abort(400, description = "invalid credentials")
    url = "http://localhost:8001/api/v1/jwt/verify/"
    response = requests.post(url, json = data)
    if response.status_code != 200:
        return jsonify(response.reason), response.status_code
    return jsonify(response.json()), response.status_code

@user.route("/make_admin", methods=["POST"])
def make_admin():
    data = request.get_json()
    if not data.get("email"):
        abort(400, description = "invalid credentials")
    url = "http://localhost:8001/addAdmin"
    response = requests.post(url, json = data, headers = request.headers)
    if response.status_code != 200:
        return jsonify(response.reason), response.status_code
    return jsonify({}), response.status_code

@user.route("/remove_admin", methods=["POST"])
def remove_admin():
    data = request.get_json()
    if not data.get("email"):
        abort(400, description = "invalid credentials")
    url = "http://localhost:8001/removeAdmin"
    response = requests.post(url, json = data, headers = request.headers)
    if response.status_code != 200:
        return jsonify(response.reason), response.status_code
    return jsonify({}), response.status_code


@user.route("/make_staff", methods=["POST"])
def make_staff():
    data = request.get_json()
    if not data.get("email"):
        abort(400, description = "invalid credentials")
    url = "http://localhost:8001/addStaff"
    response = requests.post(url, json = data, headers = request.headers)
    if response.status_code != 200:
        return jsonify(response.reason), response.status_code
    return jsonify({}), response.status_code

@user.route("/remove_staff", methods=["POST"])
def remove_staff():
    data = request.get_json()
    if not data.get("email"):
        abort(400, description = "invalid credentials")
    url = "http://localhost:8001/removeStaff"
    response = requests.post(url, json = data, headers = request.headers)
    if response.status_code != 200:
        return jsonify(response.reason), response.status_code
    return jsonify({}), response.status_code

@user.route("/delete_account", methods=["POST"])
def delete_account():
    data = request.get_json()
    if not data.get("email"):
        abort(400, description = "invalid credentials")
    url = "http://localhost:8001/deleteUser"
    response = requests.post(url, json = data, headers = request.headers)
    if response.status_code != 200:
        return jsonify(response.reason), response.status_code
    return jsonify({}), response.status_code

@user.route("/profile_update", methods=["PATCH"])
def profile_update():
    data = request.get_data()
    if not data:
        abort(400, description = "invalid credentials")
    url = "http://localhost:8001/update_profile"
    response = requests.patch(url, data = data, headers = request.headers)
    if response.status_code != 200:
        return jsonify(response.reason), response.status_code
    return jsonify(response.json()), response.status_code