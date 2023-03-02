from flask import Flask
import pymongo
from flask import  render_template, request,url_for, session
from flask import flash
#from flask import redirect

import bcrypt

app = Flask(__name__)
# bcrypt = Bcrypt(app)



app = Flask(__name__) # assigning an variable to the flask whith that we can do routes
app.secret_key = 'your_secret_key_here' # setting secret key


client = pymongo.MongoClient('mongodb://localhost:27017/')

'''@app.route('/')
def hello():
    return '<h1>Hello, Worl!</h1>' '''


@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signUp')
def signUp():
    return render_template('signUp.html')


#create data base
db = client['user_details']  #data base name
collection = db['Users']      # collection name


def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def check_password(entered_password, hashed_password):
    return bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password)

@app.route('/signUp_form', methods=['POST'])              # for sign up
def signUp_form():
    dname = request.form['dname']
    uname = request.form['uname']
    mail = request.form['mail']
    password = request.form['password']
        # Hash the password
    hashed_password = hash_password(password)

    data = {'dname': dname, 'uname': uname, 'mail': mail,'password':hashed_password}
    collection.insert_one(data)
    flash("sucessfully signed in click to continue")
    return render_template('welcome.html')

def check_user(uname, password):
    user = db.Users.find_one({'uname': uname})
    if user:
        # Retrieve the stored hashed password
        hashed_password = user['password']

        # Check if the entered password matches the stored hashed password
        if check_password(password, hashed_password):
            return True
    return False





@app.route('/login_form', methods=['POST'])               # for login
def login_form():

    if request.method == 'POST':
        uname = request.form['uname']
        password = request.form['password']
        if check_user(uname, password):
            session['uname'] = uname
            # dat = { 'uname': uname,'password':password}
            # collection.insert_one(dat)
            return render_template('welcome.html')
        else:
            flash('Invalid username or password')
            return render_template('login.html')
    else:
        return render_template('login.html'),
    # uname = request.form['uname']
    
    # password = request.form['password']
    
    
    # return render_template('welcome.html')          # return to welcome page if the user sucessfully logged in





