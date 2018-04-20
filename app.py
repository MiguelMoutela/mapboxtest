from flask import Flask, render_template
from mapbox import Geocoder
from os import environ

app = Flask(__name__)


def get_coordinates(address):
    geo = Geocoder()
    resp = geo.forward(address)
    d = resp.json()
    lng, lat = d['features'][0]['geometry']['coordinates']
    return {'longitude': lng, 'latitude': lat}




@app.route('/geocode/<addr>')
def geopage(addr):
    c = get_coordinates(addr)
    return render_template('geocode.html', address=addr, lng=c['longitude'], lat=c['latitude'],
                           MAPBOX_ACCESS_TOKEN=environ['MAPBOX_ACCESS_TOKEN'])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
