from flask import *
from app import *
from app.models.user import User as Usermodel
from app.extensions import db

user = Blueprint("user",__name__)

@user.route("/user/")

def index():
        users = Usermodel.query.all()
        return render_template('users/index.html',users=users)


@user.route("/user/", methods=["POST"])
def store():
    newuser = Usermodel(
        name=request.form["name"],
        email=request.form["email"]
    )
    db.session.add(newuser)
    db.session.commit()
    return redirect(url_for("user.index"))


@user.route("/user/create")

def create():
    return render_template("users/create.html")


    
@user.route("/user/<int:id>", methods=["DELETE", "PUT"])
def user_id(id):
    if request.method == "DELETE":
        userdel = Usermodel.query.get(id)
        if userdel:
            db.session.delete(userdel)
            db.session.commit()
            return jsonify({"message": "User Deleted!"})
        else:
            return jsonify({"message": "User not found."}), 404



@user.route("/user/<int:userID>")

def userinfo(userID):
    return render_template('users/show.html',id=userID)

