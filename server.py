from flask import Flask, request, jsonify, send_from_directory
from generator import generate_workout_json
import json

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    days = data.get('days')
    level = data.get('level')
    equipment = data.get('equipment')
    
    workout_json = generate_workout_json(days, level, equipment)
    return workout_json, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    print("Starting Calisthenics Workout Generator...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
