from flask import Flask
from mapbox import Geocoder
app = Flask(__name__)


def get_coordinates(address):
    geo = Geocoder()
    resp = geo.forward(address)
    d = resp.json()
    lng, lat = d['features'][0]['geometry']['coordinates']
    return {'longitude': lng, 'latitude': lat}

TEMPLATE =  """
    <h1>{address}</h1>
    <p>Longitude: {lng}</p>
    <p>Latitude: {lat}</p>
    """


@app.route('/geocode/<addr>')
def geopage(addr):
    c = get_coordinates(addr)
    return TEMPLATE.format(address=addr, lng=c['longitude'], lat=c['latitude'])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
