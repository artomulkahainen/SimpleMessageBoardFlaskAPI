from flask import Flask, jsonify, request
from util.config import Config
from flask_sqlalchemy import SQLAlchemy
from models import posts

app = Flask(__name__)

app.config.from_object(Config.CONFIG_FROM_OBJECT)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def get_all():
    return jsonify({'message': 'jeaa'})


app.run(port=Config.PORT)