# login_system-using-flask-and-mongo-db
Complete frontend end and  backend flask application for login system using python

This project is a simple user authentication system using Flask and MongoDB. It allows users to sign up, log in, and access a protected page, with everything secured using hashed passwords and session management.

## Key Features:
Signup: Users can create an account by entering a display name, username, email, and password. The password gets hashed using generate_password_hash before being stored in MongoDB.

Login: Users log in with their username and password. The password is checked using check_password_hash to match the hashed version in the database. If the login is successful, the session is set, and they are redirected to the welcome page.

## Session Management: 
I use Flask's session to keep track of whether a user is logged in. I also created a login_required decorator to protect routes that should only be accessible when logged in.

## Logout: 
Users can log out, which clears their session and sends them back to the home page.

## Techniques:
Flask for setting up the routes and handling requests.
MongoDB (via PyMongo) for storing user info, including hashed passwords.
Werkzeug's password hashing to securely hash and verify passwords.
Session management to handle user login status.
Flash messages to give feedback like "Signup successful" or "Invalid username or password."

## DEMO:

https://github.com/user-attachments/assets/6cc40f6b-810c-41f8-af6a-75c71444d962

