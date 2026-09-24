# Case Study: Senior High School (SHS) ICT Expo Event Management System

> **Live Application**: [LIVE APP URL]  
> **Repository**: [backendbyMel/ICT-Expo-Event-Management-System-Django-Web-App-](https://github.com/backendbyMel/ICT-Expo-Event-Management-System-Django-Web-App-)  
> **Tech Stack**: Python (Django), Vanilla JavaScript, CSS3, HTML5, SQLite

---

## 1. Executive Summary & Problem Statement

School exhibitions and Senior High School (SHS) ICT Expos often struggle with coordinating visitor participation, managing event registrants, and delivering interactive booth activities within a unified platform. Traditional event management relies on fragmented tools or generic third-party forms that lack custom event branding and interactive attendee features.

The **SHS ICT Expo Event Management System** is a full-stack web application designed to centralize event coordination, user registration, and guest-facing booth activities into a single, cohesive Django-powered platform.

*(Note: Specific visitor volume metrics and event attendance figures are not recorded in the repository source).*

---

## 2. The Solution

The system combines a structured Django backend with responsive client-side JavaScript modules to power both administration and interactive visitor experiences:

* **User Authentication & Profile Management (`users`)**: Handles account creation, login authentication, user profiles, and session tracking for event participants, competitors, and administrators.
* **Interactive Photobooth Module (`photobooth`)**: A guest-facing module allowing visitors to capture, customize, and view event photos.
* **Typing Sprint Competition (`typingSprint`)**: A live, high-speed typing challenge game designed for booth engagement, tracking typing performance metrics in real time.
* **Asset Storage Pipeline (`staticfiles/`, `media/`)**: Configured directory pipelines managing compiled static UI assets and dynamically uploaded visitor media files.

---

## 3. Architecture & System Design Decisions

```
ICT-Expo-Event-Management-System-Django-Web-App-/
├── photobooth/        # Interactive photobooth app & guest media processing
├── shs_expo/          # Main Django project configuration package
├── typingSprint/      # Interactive typing competition module (JS/Django)
├── users/             # Authentication, session, and user management app
├── media/             # Storage for dynamically uploaded visitor photos
├── staticfiles/       # Storage for compiled CSS and JS static assets
├── db.sqlite3         # Embedded SQLite database
├── manage.py          # Django CLI management script
└── .vscode/           # Development environment configuration
```

### Architectural Decisions & Trade-offs

1. **Full-Stack Hybrid Architecture (Django Backend + Vanilla JavaScript)**
   * *Decision*: Pair Django's ORM, authentication system, and request routing with lightweight Vanilla JavaScript (JavaScript accounts for 44.3% and CSS 38.4% of the codebase) to drive client-side interactivity.
   * *Trade-off*: Eliminates complex frontend build steps and single-page framework overhead, making the app straightforward to deploy on local event kiosk hardware, though complex state changes must be handled manually in Vanilla JS.

2. **Decoupled Application Modules (`users`, `photobooth`, `typingSprint`)**
   * *Decision*: Divided the application into independent Django apps for authentication, photobooth logic, and the competitive typing game.
   * *Trade-off*: Ensures clean separation of concerns and maintainability, allowing interactive booth apps to function independently of core user administration.

3. **Embedded SQLite Database (`db.sqlite3`)**
   * *Decision*: Utilized SQLite as the underlying relational database.
   * *Trade-off*: Provides zero-configuration setup for local kiosk deployment during event days, though concurrent write scaling would require migration to PostgreSQL for distributed multi-server deployments.

---

## 4. Key Implementation Details

* **Live Client-Side Game Engine (`typingSprint`)**: Uses client-side JavaScript to capture real-time typing input, compute speed metrics, and drive the competition UI directly in the browser.
* **Dynamic Media Pipeline (`photobooth` + `media/`)**: Integrates Django media file management to handle image uploads, allowing visitors to view and save custom event captures.
* **Session & Account Persistence (`users`)**: Leverages Django's built-in session framework to maintain user state and access controls across registration and competition modules.

---

## 5. Engineering Challenges & Lessons Learned

* **Client-Server State Synchronization**: Balancing real-time browser game interaction in `typingSprint` with Django session persistence required maintaining precise state boundaries between client-side JavaScript and backend HTTP endpoints.
* **Handling Dynamic Kiosk Media**: Managing user-generated media from the `photobooth` module highlighted the importance of separating static assets (`staticfiles/`) from dynamic media (`media/`) in production Django settings.

---

## 6. Technical Improvement Roadmap

* **Database Migration**: Transition from embedded SQLite (`db.sqlite3`) to PostgreSQL for high-concurrency cloud deployments.
* **API Modernization**: Implement Django REST Framework (DRF) to expose structured JSON endpoints for `typingSprint` leaderboards and `photobooth` media sharing.
* **Automated Testing Coverage**: Write unit tests for user authentication, view responses, and form validations across all three Django apps.
* **Environment Security**: Externalize secret keys and sensitive configurations into environment variables (`.env`).

---

## 7. Repository Metadata

* **Repository**: `backendbyMel/ICT-Expo-Event-Management-System-Django-Web-App-`
* **Languages**: JavaScript (44.3%), CSS (38.4%), Python (11.3%), HTML (6.0%)
* **Commits**: 3 commits
* **Contributors**: `backendbyMel`, `Mel-liza31`
* **Stars / Forks / Watchers**: 0 stars, 0 forks, 0 watchers
