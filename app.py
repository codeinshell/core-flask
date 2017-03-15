from flask import Flask, render_template, url_for, redirect, request
from os import path, urandom
from binascii import hexlify


def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = hexlify(urandom(32))

    @app.route("/tests")
    def tests():
        return "Working"


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000, host="0.0.0.0")
