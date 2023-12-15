from flask import *
from app import *
from app.models.user import User as Usermodel

user = Blueprint("user",__name__)

@user.route("/user/", methods=["GET","POST"])

def users():
    if request.method == "POST":
        # return request.form
        return redirect(url_for("user.create"))
    else:
        users = Usermodel.query.all()
        return render_template('users/index.html',users=users)

@user.route("/user/create")

def create():
    return render_template("users/create.html")

@user.route("/user/<int:userID>")

def userinfo(userID):
    return render_template('users/show.html',id=userID)