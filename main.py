from flask import Flask, render_template
import requests
import numpy as numpy



app = Flask(__name__)


@app.route('/')
def index():

    datosObtenidos=requests.get('https://api.dailymotion.com/videos?channel=sport&limit=10')
    datosFormatoJSON=datosObtenidos.json()
    print(datosFormatoJSON)
    print("intento 02 -----------")

    return render_template('index.html',datos=datosFormatoJSON['list'])

if __name__ == '__main__':
    app.run(debug=True)
##    app.run(host='0.0.0.0', port=$PORT, debug=True)
##    app.run(host='127.0.0.1', port=8000, debug=True)