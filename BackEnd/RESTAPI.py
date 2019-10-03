"""
@package RESTAPI
RESTful implementation for a backend support to a TicTacToe game.
"""
from flask import Flask, jsonify, request, json
from flask_cors import CORS

from BackEnd.ComputerIA import ComputerIA

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def get_computer_move():
    request_args = request.args
    request_dict = request_args.to_dict(flat=False)
    if not request_dict:
        return jsonify({'error': 'Need player positions'})
    cia = ComputerIA(set(request_dict['computer[]']), set(request_dict['player[]']))
    return jsonify(cia.move())
