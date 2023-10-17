from flask import Blueprint, render_template, url_for

views_bp = Blueprint("views", __name__)

@views_bp.route('/')
def home():
    return render_template("home.html")