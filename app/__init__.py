from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.config['SECRET_KEY'] = 'my secret key'


db = SQLAlchemy(app)
migrate = Migrate(app, db)


from . import urls
from . import models