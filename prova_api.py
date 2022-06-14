from flask import request, jsonify, Flask
import os, requests
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/', methods=['GET'])
def home():
    uri = f"https://api.openweathermap.org/data/2.5/weather?lat={app.config['LAT']}&lon={app.config['LONG']}&appid={app.config['APIKEY']}&units=m"
    res = requests.get(uri)
    if res.status_code == 200:

        data = res.json()
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        city = data['name']
        durée = sunset-sunrise
        meteo = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        ressentie = data['main']['feels_like']
        vent = data['wind']['speed']
        pays = data['sys']['country']

        html = """
            <p><b> Latitude </b> : """+ str(latitude) +""" °</p>
            <p><b> Longitude </b> : """+ str(longitude) +""" °</p>
            <p><b> Pays </b> : """+ str(pays) +"""</p>
            <p><b> Ville </b> : """+ str(city) +"""</p>
            <p><b> Température </b> :"""+ str(temp) +""" °C</p>
            <p><b> Température ressentie </b> : """+ str(ressentie) +""" °C</p>
            <p><b> Temps </b> : """+ str(meteo) +"""</p>
            <p><b> Description du temps </b> : """+ str(description) +"""</p>
            <p><b> Force du vent </b> : """+ str(vent) +"""</p>
            <p><b> Heure du lever du soleil </b> : """+ str(sunrise) +"""</p>
            <p><b> Heure du coucher du soleil </b> : """+ str(sunset) +"""</p>
            <p><b> Durée de soleil </b> : """+ str(durée) +"""</p>"""
            
    return html
