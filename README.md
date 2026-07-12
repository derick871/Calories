# Calories
A simple, user-friendly web application built with Django to track daily food intake and calculate total caloric consumption.

## Features
User Authentication: Secure signup and login to track personal data.

*Food Logging:* Add food items consumed throughout the day.

*Calorie Calculation:* Automatically calculates the total daily intake.

*Dashboard:* Visual overview of daily nutritional progress.

*Search/Database:* [e.g., Search through a predefined list of foods with calorie data].

## Tech Stack
Backend: Python, Django

Database: [e.g., SQLite / PostgreSQL]

Frontend: HTML5, CSS3, [e.g., Bootstrap / Tailwind CSS]

Tools: Git, VS Code

## Installation & Setup
Clone the repository:

**Bash**
git clone [your-repository-url]
cd [your-project-folder]
Create a virtual environment:

**Bash**
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
Install dependencies:

**Bash**
pip install -r requirements.txt
Run migrations:

**Bash**
python manage.py migrate
Start the server:

**Bash**
python manage.py runserver
Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Usage
Register an account or login.

. Navigate to the Dashboard to view today's logs.

. Use the "Add Food" form to input item names and calories.

The system will automatically update your daily total in the sidebar/header.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
