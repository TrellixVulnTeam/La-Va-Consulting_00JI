"""
This script runs the FlaskWebProject1 application using a development server. -> see config.py for changing that with outcommenting ~LM
"""


from os import environ
from FlaskWebProject1 import app


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
