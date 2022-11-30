from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '180c94f58b6f71921179d1775bc0fb5954c300e6f78932222fd97e64560383f37f'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/pythonncs"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# al the last would be routes
from PythonNCS import routes