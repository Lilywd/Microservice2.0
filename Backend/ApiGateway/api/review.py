from flask import Blueprint, jsonify, request, abort
import requests

review = Blueprint("review", __name__)

@review.route("/")
def home():
    return jsonify({"message": "hello  review"})


@review.route("/comments/<string:id>", methods=["GET", "POST", "PATCH", "DELETE"])
def comments(id):
    if request.method == 'GET':
        url = f"http://localhost:8002/single_product/{id}"
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify(response.reason), response.status_code
        return jsonify(response.json()), response.status_code
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            abort(400, description = "invalid credentials")
        url = "http://localhost:8001/api/v1/users/me"
        user = requests.get(url, json = data, headers = request.headers)
        if user.status_code != 200:
            return jsonify(user.reason), user.status_code
        user = user.json()
        data["userID"] = user["id"]
        data["productID"] = id
        url = "http://localhost:8002/product_comment"
        comment = requests.post(url, json = data)
        if comment.status_code != 200:
            return jsonify(comment.reason), comment.status_code
        return jsonify(comment.json()), comment.status_code
    if request.method == 'PATCH':
        data = request.get_json()
        if not data:
            abort(400, description = "invalid credentials")
        url = "http://localhost:8001/api/v1/users/me"
        user = requests.get(url, json = data, headers = request.headers)
        if user.status_code != 200:
            return jsonify(user.reason), user.status_code
        user = user.json()
        user_id = user["id"]
        url = f"http://localhost:8002/single_comment/{id}/{user_id}"
        comment = requests.patch(url, json = data)
        if comment.status_code != 200:
            return jsonify(comment.reason), comment.status_code
        return jsonify(comment.json()), comment.status_code
    if request.method == 'DELETE':
        url = "http://localhost:8001/api/v1/users/me"
        user = requests.get(url, json = data, headers = request.headers)
        if user.status_code != 200:
            return jsonify(user.reason), user.status_code
        user = user.json()
        user_id = user["id"]
        url = f"http://localhost:8002/single_comment/{id}/{user_id}"
        comment = requests.delete(url)
        if comment.status_code != 200:
            return jsonify(comment.reason), comment.status_code
        return jsonify(comment.json()), comment.status_code
