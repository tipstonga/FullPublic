from flask import Flask, render_template
import requests
import numpy as numpy
import os
import matplotlib
import matplotlib.pyplot as plt

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
## trabajo generar y salvar grafico
    print('genero grafico')
    plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])
    plt.xlabel('Months')
    plt.ylabel('Books Read')
    print('salvo grafico sin mostrar')
    # plt.show()
    plt.savefig('https://fullpublic-production.up.railway.app/figUno.png')
    # plt.savefig('templates/figUno.png')
    # plt.savefig('templates/figUno.jpg')


## trabajo basico web videos
    datosObtenidos=requests.get('https://api.dailymotion.com/videos?channel=sport&limit=10')
    datosFormatoJSON=datosObtenidos.json()
    print(datosFormatoJSON)
    print("version 04 -----------")

    return render_template('index.html',datos=datosFormatoJSON['list'])

if __name__ == '__main__':
    app.run(host=hostvalue, port=portvalue, debug=True)
##     

