from flask import Flask, jsonify, request
from util.config import Config
from models.models import db

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{Config.PG_USER}:{Config.PG_PASSWORD}@{Config.PG_URI}:{Config.PG_PORT}/{Config.PG_DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def get_all():
    return jsonify({'message': 'jeaa'})

if __name__ == '__main__':
    app.run(port=Config.PORT)