from flask import Flask, request
from app.blueprints import home,user
from flask_sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import *
from app.extensions import db




app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

app.register_blueprint(home.home)
app.register_blueprint(user.user)




with app.app_context():
    db.create_all()