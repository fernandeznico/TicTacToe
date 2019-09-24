"""
@package RESTAPI
RESTful implementation for a backend support to a TicTacToe game.
"""
from flask import Flask, jsonify

from BackEnd.ComputerIA import ComputerIA

server = Flask(__name__)


@server.route('/')
def get_computer_move():
    cia = ComputerIA({'a', 'b'}, {'e', 'i'})
    return jsonify(cia.move())


if __name__ == "__main__":
    server.run(debug=True)
