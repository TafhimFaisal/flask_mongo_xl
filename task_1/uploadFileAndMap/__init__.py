from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
client = MongoClient('mongodb://localhost:27017/')
db = client['product_data']

from uploadFileAndMap import controller
