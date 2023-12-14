from flask import *

user = Blueprint("user",__name__)

@user.route("/user/", methods=["GET","POST"])

def users():
    if request.method == "POST":
        # return request.form
        return redirect(url_for("user.create"))
    else:
        return render_template('users/index.html')

@user.route("/user/create")

def create():
    return render_template("users/create.html")

@user.route("/user/<int:userID>")

def userinfo(userID):
    return render_template('users/show.html',id=userID)