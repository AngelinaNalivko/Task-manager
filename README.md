````markdown
# Task Manager — Flask + MongoDB

A minimal and beautiful web app for managing daily tasks.  
Built with **Python Flask**, **MongoDB**, and styled using **Bootstrap + custom CSS**.

---

## Features

- Add tasks with:
  - Title
  - Deadline
  - Description
  - Priority (`Low`, `Normal`, `High`, `Urgent`)
- Visual “Time Left” calculation
- Mark tasks as done 
- Delete tasks 
- Filter by:
  - Priority
  - Status (Done / Not Done)
- Tasks are stored in **MongoDB**
- Mobile-friendly UI with pastel tones 

---

## Tech Stack

- **Backend:** Flask (Python)
- **Database:** MongoDB (via PyMongo)
- **Frontend:** HTML, CSS, Bootstrap
- **Styling:** Pastel custom design with dark text accents

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/flask-task-manager.git
cd flask-task-manager
````

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run MongoDB

Make sure MongoDB is installed and running locally on `localhost:27017`.
(You can use `brew services start mongodb-community@6.0` on macOS.)

### 5. Run the app

```bash
export FLASK_APP=app.py
flask run
```

Then open `http://127.0.0.1:5000` in your browser.

---

## Screenshots
