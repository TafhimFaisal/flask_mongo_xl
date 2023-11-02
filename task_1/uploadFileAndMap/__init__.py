from flask import Flask
from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values()
app = Flask(__name__)
app.config['SECRET_KEY'] = config['SECRET_KEY']
client = MongoClient(config['MONGO_DB'])
db = client[config['DB_NAME']]

from uploadFileAndMap import controller
