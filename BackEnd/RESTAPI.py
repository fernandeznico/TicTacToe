"""
@package RESTAPI
RESTful implementation for a backend support to a TicTacToe game.
"""
from flask import Flask, jsonify, request

from BackEnd.ComputerIA import ComputerIA

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_computer_move():
    request_json = request.json
    cia = ComputerIA(set(request_json['computer']), set(request_json['player']))
    return jsonify(cia.move())


if __name__ == "__main__":
    app.run(debug=True)
