from flask import Flask, Blueprint, request,render_template

home = Blueprint("home",__name__)

@home.route("/")
def index():
    return  "<h1>This is homepage</h1>"

