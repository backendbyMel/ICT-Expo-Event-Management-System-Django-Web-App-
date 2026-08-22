Senior High School (SHS) ICT Expo Event Management System
An interactive, full-stack web application designed to coordinate, manage, and enhance visitor engagement at an SHS ICT Expo exhibition. This system blends a robust Django backend with responsive, highly interactive frontend experiences, including a live Typing Sprint game and a customizable Photobooth module.

🚀 Key Features & Core Modules
The project is structured into self-contained Django applications, each handling a distinct functional area of the expo event:

👥 User Authentication & Management (users App)

Handles secure registration, login, session management, and profile creation for event participants, competitors, and exhibition administrators.
📸 Interactive Photobooth (photobooth App)

A guest-facing interactive feature allowing expo visitors to capture, customize, or view memorable moments from the exhibition.
⌨️ Typing Sprint Competition (typingSprint App)

An interactive, high-speed typing challenge game designed to run live at exhibition booths, tracking and displaying speed metrics to engage and challenge attendees.
📁 Asset Pipeline (staticfiles & media)

Fully pre-configured pathways to manage compiled static CSS/JS scripts and store dynamically uploaded visitor photos or media.
🛠️ Technology Stack
Backend: Python / Django (Handles business logic, routing, authentication, and database sessions)
Frontend Logic: Vanilla JavaScript (Powering interactive clients, games, and UI transitions)
Styling: CSS3 & Responsive Design layouts
Database: SQLite (Lightweight relational database ideal for single-server expo kiosks and rapid deployment)
📁 Repository Structure
Below is the directory map of the Django project:

├── .vscode/               # IDE workspace settings
├── media/                 # Directory for dynamic user uploads (e.g., photos from photobooth)
├── photobooth/            # Sub-app managing the interactive photobooth
├── shs_expo/              # Main project configuration (settings.py, urls.py, wsgi.py)
├── staticfiles/           # Directories for bundled frontend assets (JS scripts, stylesheets)
├── typingSprint/          # Sub-app running the typing game logic and scores
├── users/                 # Sub-app managing accounts, permissions, and profiles
├── db.sqlite3             # Local SQLite database pre-configured with the initial state
├── manage.py              # Django command-line execution utility
⚙️ Installation & Local Setup
To deploy this event system on your local machine or an expo booth kiosk, follow these steps:

Prerequisites
Python 3.10+ installed globally on your machine.
Git (optional, for cloning).
Steps
Clone the Repository

git clone https://github.com/backendbyMel/ICT-Expo-Event-Management-System-Django-Web-App-.git
cd ICT-Expo-Event-Management-System-Django-Web-App-
Initialize a Virtual Environment Isolate your project dependencies by creating a python virtual environment:

# Create the virtual environment
python -m venv venv
Activate the Virtual Environment

Windows (Command Prompt):
venv\Scripts\activate
Windows (PowerShell):
.\venv\Scripts\activate
macOS / Linux:
source venv/bin/activate
Install Django Ensure Django is installed in your isolated virtual environment:

python -m pip install django
Apply Database Migrations Initialize the local SQLite database schemas:

python manage.py migrate
Run the Development Server

python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/ to access the expo home screen.

🎓 Technical & Architectural Learning Outcomes
This codebase serves as an exceptional template for developers studying intermediate full-stack Django patterns:

Monolithic Multi-App Architecture: Demonstrates how to organize an event-driven platform by decoupling discrete features (Users, Games, Utilities) into independent Django applications under a shared settings framework.
Heavy Client-Side Integration: Showcases a hybrid architecture where Django manages state and security, while heavy client-side JavaScript (constituting over 44% of the codebase) coordinates fast-paced interactive elements like typing tests and image operations.
Kiosk-Ready State Management: Demonstrates lightweight relational modeling suited for self-contained, offline exhibition kiosks using an embedded SQLite database.
