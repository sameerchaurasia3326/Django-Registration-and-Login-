# Django Login & Email Notification System

This is a web application built with the Django framework that provides a complete user authentication system. It allows users to register for a new account and log in. Upon a successful login, the system automatically sends an email notification to a predefined administrator email address.

## Features

-   **User Registration**: New users can create an account.
-   **User Login/Logout**: Secure session-based authentication for users.
-   **Email Notification**: Automatically sends an email to the site administrator whenever a user logs in.

## Installation & Setup

1.  **Clone the Repository** and navigate into the directory.
2.  **Create and Activate a Virtual Environment**.
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  **Install Dependencies** from a `requirements.txt` file.
    ```
    Django
    python-dotenv
    ```
    Then run:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create a `.env` file** in the root directory for your secret email credentials:
    ```env
    EMAIL_HOST_USER="your-email@example.com"
    EMAIL_HOST_PASSWORD="your-email-app-password"
    ```
5.  **Configure `settings.py`** to use these credentials for sending emails.
6.  **Run Database Migrations**:
    ```bash
    python manage.py migrate
    ```
7.  **Create a Superuser** to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

## Usage

1.  **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
2.  Navigate to `http://127.0.0.1:8000/` to register and log in.
