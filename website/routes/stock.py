from flask import Blueprint, render_template, url_for

stock_bp = Blueprint("stock_bp", __name__)

@stock_bp.route('/')
def home():
    return "Hello Stock"