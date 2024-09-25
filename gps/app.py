from flask import Flask, render_template, request, jsonify
from tspa import obtenerruta
from coord import coord

app = Flask(__name__)

@app.route('/')
def index():
    ciudades = list(coord.keys())
    return render_template('index.html', ciudades=ciudades)