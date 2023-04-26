from flask import Flask, render_template
import requests
import numpy as numpy
import os


## seleccion del host y port para 
## Railway o local
portname='PORT'
if portname in os.environ:
    portvalue=os.environ[portname]
    hostvalue='0.0.0.0'
    print(portname,' value is', portvalue,' ,  host is ',hostvalue)
else:
    portvalue=8000
    hostvalue='127.0.0.1'
    print(portname, 'does not exist using ', hostvalue, portvalue)

    
app = Flask(__name__)

@app.route('/')
def index():

    datosObtenidos=requests.get('https://api.dailymotion.com/videos?channel=sport&limit=10')
    datosFormatoJSON=datosObtenidos.json()
    print(datosFormatoJSON)
    print("version 03 -----------")

    return render_template('index.html',datos=datosFormatoJSON['list'])

if __name__ == '__main__':
    app.run(host=hostvalue, port=portvalue, debug=True)
##     

