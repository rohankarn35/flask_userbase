from flask import Flask, request
from app.blueprints import home,user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
app = Flask(__name__)

app.register_blueprint(home.home)
app.register_blueprint(user.user)
