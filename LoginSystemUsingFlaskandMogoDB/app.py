from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/user_db"
app.secret_key = "secretkey"
mongo = PyMongo(app)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        display_name = request.form['display_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)
        
        users_collection = mongo.db.users
        users_collection.insert_one({
            'display_name': display_name,
            'username': username,
            'email': email,
            'password': hashed_password
        })
        
        flash('Signup successful! Please login.')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users_collection = mongo.db.users
        user = users_collection.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            flash('Login successful!')
            return render_template('welcome.html')
        else:
            flash('Invalid username or password. Please try again or sign up.')
            return render_template('login.html')

            # return redirect(url_for('signup'))


    return render_template('login.html')


@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    session.pop('uname', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
