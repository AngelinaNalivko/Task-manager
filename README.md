# Task Manager — Flask + MongoDB

A web app for managing daily tasks. Built with **Python Flask**, **MongoDB**, and styled using **Bootstrap + custom CSS**.

## Features

- Add tasks with title, deadline, description and priority (from low to urgent)
- Visual “Time Left” calculation
- Mark tasks as done 
- Delete tasks 
- Filter by priority and status

## Tech Stack

- **Backend:** Flask (Python)
- **Database:** MongoDB (via PyMongo)
- **Frontend:** HTML, CSS, Bootstrap

## Screenshots


## Instruction how to get the app on your local machine:

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

### 5. Run the app

```bash
export FLASK_APP=app.py
flask run
```

Then open `http://127.0.0.1:5000` in your browser.
