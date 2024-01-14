from flask import Flask, redirect, url_for, render_template, request, abort, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
# from flask_session import Session
from flask_restful import Api, Resource
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# api =   Api(app)
# bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"


# # app = Flask(__name__)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# @app.route("/")
# def index():
#     if not session.get("name"):
#         return redirect("/login")
#     return render_template('index.html')


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         session["name"] = request.form.get("name")
#         return redirect("/")
#     return render_template("login.html")


# @app.route("/logout")
# def logout():
#     session["name"] = None
#     return redirect("/")


# @app.route('/returnjson', methods = ['GET'])
# def ReturnJSON():
#     if(request.method == 'GET'):
#         data = {
#             "Modules" : 15,
#             "Subject" : "Data Structures and Algorithms",
#         }

#         return jsonify(data)

# class returnjson(Resource):
#     def get(self):
#         data={
#             "Modules": 15, 
#             "Subject": "Data Structures and Algorithms"
#         }
#         return data

# api.add_resource(returnjson,'/returnjson')


################################################################################################
# app.secret_key = 'GeeksForGeeks'

# # Set MySQL data
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'user-table'

# mysql = MySQL(app)


# @app.route('/')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     message = ''
#     if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
#         email = request.form['email']
#         password = request.form['password']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute(
#             'SELECT * FROM user WHERE email = % s AND password = % s',
#                   (email, password, ))
#         user = cursor.fetchone()
#         if user:
#             session['loggedin'] = True
#             session['userid'] = user['userid']
#             session['name'] = user['name']
#             session['email'] = user['email']
#             message = 'Logged in successfully !'
#             return render_template('user.html',
#                                    message=message)
#         else:
#             message = 'Please enter correct email / password !'
#     return render_template('login.html',
#                            message=message)


# # Make function for logout session
# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('userid', None)
#     session.pop('email', None)
#     return redirect(url_for('login'))


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     message = ''
#     if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
#         userName = request.form['name']
#         password = request.form['password']
#         email = request.form['email']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
#         account = cursor.fetchone()
#         if account:
#             message = 'Account already exists !'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             message = 'Invalid email address !'
#         elif not userName or not password or not email:
#             message = 'Please fill out the form !'
#         else:
#             cursor.execute(
#                 'INSERT INTO user VALUES (NULL, % s, % s, % s)',
#                       (userName, email, password ))
#             mysql.connection.commit()
#             message = 'You have successfully registered !'
#     elif request.method == 'POST':
#         message = 'Please fill out the form !'
#     return render_template('register.html', message=message)


# @app.route('/')
# def index():
#     password = 'password'
#     hashed_password = bcrypt.generate_password_hash (password).decode('utf-8')
#     is_valid = bcrypt.check_password_hash(hashed_password, password)
#     return f"Password: {password}<br>Hashed Password: {hashed_password}<br>Is Valid: {is_valid}"


# @app.route('/register')
# def register():
#     return render_template("register.html")

# @app.route('/user')
# def user():
#     return render_template("user.html")

# @app.route('/login')
# def login():
#     return render_template("login.html")

# @app.route('/success')
# def success():
#     return "logged in successfully"

# @app.route("/login", methods=["POST", "GET"])
# def login():

#     # if the method is POST and Username is admin then
#     # it will redirects to success url.
#     if request.method == "POST" and request.form["username"] == "admin":
#         return redirect(url_for("success"))
#     return redirect(url_for('index'))

# @app.route('/<username>')
# def index(username):
#     if username[0].isdigit():
#         abort(400)
#     return '<h1>Good Username</h1>'

# @app.route('/hello/<name>')
# def hello_name(name):
#     return "Hello %s!" % name

# @app.route('/user/<username>')
# def show_user(username):
#     # Greet the user
#     return f'Hello {username} !'

# @app.route('/post/<int:id>')
# def show_post(id):
#     # Shows the post with given id.
#     return f'This post has the id {id}'

# def show_user(username):
#     # Greet the user
#     return f'Hello {username} !'

# app.add_url_rule('/user/<username>', 'show_user', show_user)

# @app.route("/")
# def index():
#     return "Toyin is my love"

# @app.route('/')
# def msg():
#     return "Welcome"

# @app.route('/vint/<int:age>')
# def vint(age):
#     return "I am %d years old " % age

# @app.route('/vfloat/<float:balance>')
# def vfloat(balance):
#     return "My Account Balance %f" % balance

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success', name=user))
#     else:
#         user = request.form['nm']
#         return redirect(url_for('success', name=user))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
