import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.moment import Moment

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configure database
app.config['SECRET_KEY'] = '\xfe\xd0>\xf2\x9ds\x1b\xa6N#;\xfd\xec#\x8a\xa7\xd3g\x93\t~\xe8l\xb1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = None
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)

# for displaying timestamps
moment = Moment(app)

import thermos.views
import thermos.models

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
