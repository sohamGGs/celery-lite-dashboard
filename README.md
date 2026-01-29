# Lightweight Task Queue & Dashboard

This project is an asynchronous task queue system designed to offload time-consuming processes from a web server to background workers, ensuring a responsive user interface.

## 🚀 Features
* **Task Submission:** Users can submit tasks via a web dashboard.
* **Background Processing:** Tasks are queued in a database and handled by separate worker processes.
* **Real-Time Monitoring:** A live dashboard polls a REST API every second to provide instant status updates (**Pending**, **Processing**, **Completed**).

## 🛠 Tech Stack
* **Backend:** Python, Flask
* **Database & ORM:** SQLite, SQLAlchemy
* **Frontend:** JavaScript (AJAX/Polling), HTML5, CSS3

## 📦 Installation
1. Clone the repo: `git clone [YOUR_URL]`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python app.py`
4. Run the worker: `python worker.py`
