from flask import Blueprint, render_template, url_for

pokemon = Blueprint("pokemon", __name__)

@pokemon.route('/')
def home():
    return render_template('pokemon.html')