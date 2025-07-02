# 📝 Job Application Tracker

A simple and powerful Flask web application to help users manage and track their job applications effectively.

## 🚀 Features

- User Registration and Login
- Add job applications (Company, Role, Status, Deadline, Notes)
- Edit and delete existing job entries
- View all applications on the dashboard
- Filter by user – private dashboard
- Flash messages for feedback
- Bootstrap UI for clean and responsive design

## 🧱 Tech Stack

- Python 3
- Flask
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy
- SQLite (default database)
- Bootstrap (via CDN)

## 📂 Project Structure

job-tracker-flask/
│
├── app.py
├── config.py
├── models.py
├── forms.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── add_job.html
│ └── edit_job.html



## ⚙️ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/job-tracker-flask.git
cd job-tracker-flask


#Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\\Scripts\\activate


# 3. Install dependencies:
pip install -r requirements.txt


# 4. Run the application:
python app.py





