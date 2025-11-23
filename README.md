# Flask Blog App 📝

A simple CRUD (Create, Read, Update, Delete) blog application built with **Flask** and **JSON file storage**.  
Users can create blog posts, edit them, delete them, and like posts.  
The interface is styled using soft pastel UI elements for a clean and friendly look.

---

## 🚀 Features

- View all blog posts
- Add new posts (with author, title, and content)
- Update existing posts
- Delete posts
- Like posts (stored persistently)
- Persistent storage using `storage.json`
- Clean, responsive UI with modern pastel styling
- Validation prevents empty or whitespace-only posts
- Line breaks in content are preserved visually
- Delete actions ask for confirmation to prevent accidents

---

## 🗂️ Project Structure

```
project/
│
├── app.py                 # Main Flask application
├── storage.json           # JSON file storing blog posts
│
├── templates/
│   ├── index.html         # Homepage showing all posts
│   ├── add.html           # Form for creating a new post
│   └── update.html        # Form for editing an existing post
│
└── static/
    └── style.css          # Application styling
```

---

## 🧰 Requirements

- Python 3.8+
- Flask

Install Flask using:

```bash
pip install flask
```

---

## ▶️ How to Run

1. Open your terminal in the project folder
2. Run:

```bash
python app.py
```

3. Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📦 Data Storage

All blog posts are stored in a JSON file named `storage.json`.  
Each post has the following structure:

```json
{
    "id": 1,
    "author": "Alice",
    "title": "My First Post",
    "content": "Hello, World!",
    "like": 0
}
```

Before saving, user input is trimmed to remove unnecessary whitespace.
Content line breaks are converted to `<br>` tags so posts display exactly as typed.

---

## 💡 Future Improvements (optional ideas)

- Flash messages for success & error feedback
- Form validation feedback
- Pagination
- Convert JSON storage to SQLite using SQLAlchemy
- Authentication (login / logout)
- REST API version of the blog
- Dark / light theme switch

---

## ✔️ Status

**Completed with enhancements**, but open for future improvements.

Feel free to fork, modify, and experiment!

---

## 🤝 License

This project is for educational use.

---

## 🧑‍💻 Author
Created as a learning project while studying **Flask, templates, web forms, and styling**

by **[margarita-bykadorova](https://github.com/margarita-bykadorova)**  
