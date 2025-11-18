"""
A simple Flask blog application that supports creating, reading,
updating, deleting, and liking blog posts stored in a JSON file.
"""

from flask import Flask, render_template, request, redirect, url_for
import json

DATA_FILE = "storage.json"

app = Flask(__name__)


def get_data():
    """Return all saved blog posts from the JSON storage file."""
    with open(DATA_FILE, "r", encoding="utf-8") as handle:
        return json.load(handle)


def save_data(data):
    """Write updated blog posts to the JSON storage file."""
    with open(DATA_FILE, "w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=4)


@app.route('/')
def index():
    """Display a list of all blog posts."""
    posts = get_data()
    return render_template("index.html", posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Display the form and handle creation of a new blog post."""
    posts = get_data()

    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']

        new_id = max((post["id"] for post in posts), default=0) + 1
        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content,
            "like": 0
        }

        posts.append(new_post)
        save_data(posts)
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    """Remove the blog post that matches the given ID."""
    posts = get_data()

    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            break

    save_data(posts)
    return redirect(url_for("index"))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Display the update form or apply blog post changes."""
    posts = get_data()

    post_to_edit = None
    for post in posts:
        if post["id"] == post_id:
            post_to_edit = post
            break

    if post_to_edit is None:
        return "Post not found", 404

    if request.method == 'POST':
        post_to_edit["author"] = request.form.get('author', post_to_edit["author"])
        post_to_edit["title"] = request.form.get('title', post_to_edit["title"])
        post_to_edit["content"] = request.form.get('content', post_to_edit["content"])

        save_data(posts)
        return redirect(url_for("index"))

    return render_template("update.html", post=post_to_edit)


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    """Increment the like counter for the specified blog post."""
    posts = get_data()

    for post in posts:
        if post["id"] == post_id:
            post["like"] = post.get("like", 0) + 1
            break

    save_data(posts)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
