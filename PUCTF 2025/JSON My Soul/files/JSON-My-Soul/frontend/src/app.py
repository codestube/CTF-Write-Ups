#!/usr/bin/env python3
import os
import requests
from flask import Flask, render_template, request, jsonify

FLAG = os.environ.get('FLAG', 'PUCTF25{fake_flag_do_not_submit}')
WHITELIST_API_URL = os.environ.get('WHITELIST_API_URL', 'http://api')

API_ENDPOINT = '/api/weather'
LOCALHOST_IP_ADDRESS = '127.0.0.1'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', WHITELIST_API_URL=WHITELIST_API_URL)

@app.route(API_ENDPOINT, methods=['GET'])
def getWeatherInformation():
    url = request.args.get('url', WHITELIST_API_URL).lower().strip()
    if not url:
        return jsonify({'message': 'Please provide a URL.'})
    if not url.startswith(WHITELIST_API_URL):
        return jsonify({'message': 'Invalid API URL.'})

    try:
        apiResponse = requests.get(f'{url}{API_ENDPOINT}', allow_redirects=False)
        apiJsonData = apiResponse.json()
    except:
        return jsonify({'message': 'Something went wrong with the API service. Sorry!'})

    return apiJsonData

@app.route('/flag', methods=['GET'])
def getFlag():
    isClientAddressLocalhost = True if request.remote_addr == LOCALHOST_IP_ADDRESS else False
    if not isClientAddressLocalhost:
        return jsonify({'message': 'Try harder :D'})
    
    return jsonify({'message': FLAG})

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=False)