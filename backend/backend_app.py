from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route("/api/posts", methods=["GET"])
def get_posts():
    return jsonify(POSTS)


@app.route("/api/posts", methods=["POST"])
def add_post():
    """
    {"title": "<title of the new post>",
    "content": "<content of the new post>"}
    """
    new_post = request.get_json()
    if "title" not in new_post:
        return jsonify({"Error": "Title required."}), 400
    if "content" not in new_post:
        return jsonify({"Error": "Content required."}), 400
    new_post["id"] = len(POSTS) + 1
    POSTS.append(new_post)
    return jsonify(POSTS), 201    
    
@app.route("/api/posts/<int:id>", methods=["DELETE"])
def delete_post(id):
    for post in POSTS:
        if post["id"] == id:
            POSTS.remove(post)
            return jsonify({"message": f"Post with id {id} has been deleted successfully."}), 200
    return jsonify({"Error": "Post ID not found"}), 404
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
