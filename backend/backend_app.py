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
    
    sort = request.args.get("sort")
    direction = request.args.get("direction", "asc")
    
    if sort is not None and sort not in ["title", "content"]:
        return jsonify({"Error": "Invalid sort. Use 'title' or 'content'."}), 400
    if direction not in ["asc", "desc"]:
        return jsonify({"Error": "Invalid direction. Use 'asc' or 'desc'."}), 400
    if direction == "asc":
        direction = False
    elif direction == "desc":
        direction = True
    if sort == "title":
        return jsonify(sorted(POSTS, key=lambda post: post["title"], reverse = direction))
    if sort == "content":
        return jsonify(sorted(POSTS, key=lambda post: post["content"], reverse = direction))

    return jsonify(POSTS), 200


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
    return jsonify(new_post), 201


@app.route("/api/posts/<int:id>", methods=["DELETE"])
def delete_post(id):
    for post in POSTS:
        if post["id"] == id:
            POSTS.remove(post)
            return (
                jsonify(
                    {"message": f"Post with id {id} has been deleted successfully."}
                ),
                200,
            )
    return jsonify({"Error": "Post ID not found"}), 404


@app.route("/api/posts/<int:id>", methods=["PUT"])
def update_post(id):
    new_post = request.get_json()
    for post in POSTS:
        if post["id"] == id:
            if "title" in new_post:
                post["title"] = new_post["title"]
            if "content" in new_post:
                post["content"] = new_post["content"]
            return jsonify(post), 200
    return jsonify({"Error": "Post ID not found"}), 404


@app.route("/api/posts/search", methods=["GET"])
def search_post():
    title_search = request.args.get("title", "").strip().lower()
    content_search = request.args.get("content", "").strip().lower()

    found_posts = []
    for post in POSTS:
        title_post = post.get("title", "").lower()
        content_post = post.get("content", "").lower()

        title_match = title_search in title_post or not title_search
        content_match = content_search in content_post or not content_search
        if title_match and content_match:
            found_posts.append(post)
    return jsonify(found_posts), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
