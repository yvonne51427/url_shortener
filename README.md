# URL Shortener

## Introduction
This is a URL shortener web application built using Django. 
It allows users to shorten long URLs for easier sharing and management. 
The application also supports user authentication via Google and Facebook OAuth.

## Features
- **URL Shortening**: Convert long URLs into short, easy-to-share links.
- **User Authentication**: Log in with Google or Facebook.
- **URL Management**: Users can view and manage their shortened URLs.

## Installation
To get started with the project, follow these steps:

1. **Clone the repository**:
    ```
    git clone https://github.com/yvonne51427/url_shortener.git
    cd url_shortener
    ```

3. **Create and activate a virtual environment**:
    ```
    python -m venv env
    source env/bin/activate
    ```

4. **Install the required dependencies**:
    ```
    pip install -r requirements.txt
    ```

5. **Set up the environment variables**:
    Create a `.env` file in the project root directory and add the following:
    ```.env
    SECRET_KEY='your_secret_key'
    DATABASE_URL='mysql://username:password@hostname:port/database_name'
    GOOGLE_CLIENT_ID='your_google_client_id'
    GOOGLE_CLIENT_SECRET='your_google_client_secret'
    FACEBOOK_APP_ID='your_facebook_app_id'
    FACEBOOK_APP_SECRET='your_facebook_app_secret'
    ```

## Usage
To run the development server, use the following command:
```
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000`.

