from flask import Blueprint, render_template, url_for, jsonify
from ..data.typechart import typechart

pokemon_bp = Blueprint("pokemon_bp", __name__)

@pokemon_bp.route('/')
def home():
    return render_template('/pokemon/pokemon.html')

@pokemon_bp.route('/typechart-quiz')
def quiz_typechart():
    return render_template('/pokemon/quiz_typechart.html')

# @pokemon_bp.route('/test')
# def test():
#     return jsonify(typechart)