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

@app.route('/signal', methods=['GET'])
def obt():
    data = arduino.readline().decode('utf-8').strip()
    
    try:
        int_data = int(data)
        if int_data == 1:
            return jsonify({'status': 'success', 'message': '1'})
        else:
            return jsonify({'status': 'error', 'message': 'Data is not 1'})
    except ValueError:
        return jsonify({'status': 'error', 'message': 'Invalid data'})

