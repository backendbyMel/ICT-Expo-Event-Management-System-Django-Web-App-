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
