from flask import Flask, render_template
from pymongo import MongoClient
from pprint import pprint
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/appK')
def appK():
    return render_template('app.html')

@app.route('/how')
def how():
    return render_template('howitworks.html')

@app.route('/reserve')
def reserve():
    return render_template('reservations.html')

@app.route('/map')
def map():

    client = MongoClient('mongodb://54.190.29.49:27017/')
    db = client.KogiiDB
    collection = db.LateralData
    cursor = collection.find({})

    list = []

    for documents in cursor:
        coords = {}
        lat = str(documents['lat'])
        lon = str(documents['lon'])
        coords['lat'] = lat
        coords['lon'] = lon

        list.append(coords)
    print(list)
    return render_template('map.html', data=json.dumps(list))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
