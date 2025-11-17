from flask import Flask, render_template, request, redirect, url_for
import json

DATA_FILE = "storage.json"

app = Flask(__name__)


def get_data():
    """Fetch data from the JSON file"""
    with open(DATA_FILE, "r", encoding="utf-8") as handle:
        return json.load(handle)


def save_data(data):
    """Update data in JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=4)


@app.route('/')
def index():
    """Display all blog posts"""
    blog_posts = get_data()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Display the form for adding a new blog post.
    Add a new blog post to the JSON file.
    Redirect the user to the index page."""

    posts = get_data()

    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']
        new_id = max([post["id"] for post in posts], default=0) + 1

        new_post = {"id": new_id, "author": author, "title": title, "content": content}

        posts.append(new_post)
        save_data(posts)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    """Find the post by its ID and delete it from storage.json
    Redirect the user to the index page"""

    posts = get_data()

    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            break

    save_data(posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Display the form for updating a blog post.
    Update the title and content of the blog.
    Redirect the user to the index page."""

    posts = get_data()

    post = None
    for p in posts:
        if p["id"] == post_id:
            post = p
            break

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        author = request.form.get('author', post["author"])
        title = request.form.get('title', post["title"])
        content = request.form.get('content', post["content"])

        post["author"] = author
        post["title"] = title
        post["content"] = content

        save_data(posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)