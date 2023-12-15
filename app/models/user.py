from app.extensions import db
from flask_sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import *


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String,  nullable=False)
    email: Mapped[str] = mapped_column(String,unique=True,nullable=False)