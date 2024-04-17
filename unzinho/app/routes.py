from app import aplication
from flask import render_template

@aplication.route('/')
@aplication.route('/páginainicial')
def index():
    return render_template('páginainicial.html')

@aplication.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@aplication.route('/contato')
def contato():
    return render_template('contato.html')


