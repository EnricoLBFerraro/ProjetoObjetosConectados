from flask import Flask, jsonify, render_template
import serial

app = Flask(__name__)

try:
    ser = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta correta
except serial.SerialException as e:
    print(f"Erro ao abrir a porta serial: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    try:
        line = ser.readline().decode('utf-8').strip()
        if line.startswith("BPM: "):
            bpm = line.split(": ")[1]
            return jsonify(bpm=bpm)
    except serial.SerialException as e:
        print(f"Erro ao ler da porta serial: {e}")
    return jsonify(bpm=None)

if __name__ == '__main__':
    app.run(debug=True)


