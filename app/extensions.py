from flask_sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import *

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)