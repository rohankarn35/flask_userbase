from flask import Flask, Blueprint, request

home = Blueprint("home",__name__)

@home.route("/")
def index():
    return"<h1>Hello World</h1><p>This is flask </p>"

