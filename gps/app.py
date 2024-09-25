from flask import Flask, render_template, request, jsonify
from tspa import obtenerruta
from coord import coord

app = Flask(__name__)