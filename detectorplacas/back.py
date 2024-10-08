from flask import Flask, render_template, request, jsonify
import Recog as Re
import conector as cn
import serial
import time

app = Flask(__name__)

arduino = serial.Serial('/dev/cu.usbserial-130', 9600, timeout=1)

@app.route('/')
def index():
    return render_template('index.html')

