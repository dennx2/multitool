from flask import Blueprint, render_template, url_for

stock = Blueprint("stock", __name__)

@stock.route('/')
def home():
    return "Hello Stock"