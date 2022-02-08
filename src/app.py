from flask import Flask
from figures.models import test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/chess.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/test', methods=['GET'])
def index():
    result = test()
    return '123'
