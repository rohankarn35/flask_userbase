from flask import Flask, Blueprint,request

user = Blueprint("user",__name__)

@user.route("/user/", methods=["GET","POST"])

def users():
    if request.method == "POST":
        return "Create new user"
    else:
        return "Hello all user"

@user.route("/user/<int:userID>")

def userinfo(userID):
    return f"<h2>User Info: {userID}</h2>"