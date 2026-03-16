#!/usr/bin/env python3
from flask import Flask, jsonify

API_ENDPOINT = '/api/weather'

app = Flask(__name__)

# Hard-coded JSON data, as we don't want other third 
# parties involve in this challenge.
WEATHER_INFORMATION = {
    'location': 'The Hong Kong Polytechnic University - NuttyShell HQ',
    'description': 'Partly cloudy',
    'temperature': '23',
    'humidity': 78,
}

@app.route(API_ENDPOINT, methods=['GET'])
def getWeatherInformation():
    return jsonify(WEATHER_INFORMATION)

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=False)