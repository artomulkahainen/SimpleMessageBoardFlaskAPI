from flask import Flask, jsonify, request
from util.config import Config
from models.models import db
from models.models import Post

app = Flask(__name__)

app.config["DEBUG"] = True
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{Config.PG_USER}:{Config.PG_PASSWORD}@{Config.PG_URI}:{Config.PG_PORT}/{Config.PG_DATABASE}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/api/posts", methods=["POST", "GET"])
def handle_posts():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            print("printing data:")
            print(data["post"])
            new_post = Post(post=data["post"])
            print("printing new post:")
            print(new_post)
            db.session.add(new_post)
            db.session.commit()
            return {
                "message": f"New post with id {new_post.post} has been created successfully."
            }
        else:
            return {"error": "The request payload is not in JSON format"}
    elif request.method == "GET":
        posts = Post.query.all()
        results = [{"id": post.id, "post": post.post} for post in posts]

        return {"count": len(results), "posts": results}


if __name__ == "__main__":
    app.run(port=Config.PORT)