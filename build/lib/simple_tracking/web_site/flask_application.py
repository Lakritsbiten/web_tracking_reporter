from flask import Flask


def create_flask_app():
    # create and configure the app
    _app = Flask(__name__)
    _app.debug = True
    return _app


if __name__ == '__main__':
    app = create_app()
    app.run()

