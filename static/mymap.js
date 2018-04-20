

function myfoo(token, longitude, latitude){
  L.mapbox.accessToken = token;
  var geojson = [
    {
      type: 'Feature',
      geometry: {
        type: 'Point',
        coordinates: [longitude, latitude]
      },
      properties: {
        'marker-color': '#3bb2d0',
        'marker-size': 'large',
        'marker-symbol': 'rocket'
      }
    }
  ];

  var mapSimple = L.mapbox.map('map_simple', 'mapbox.light')
    .setView([37.8, -96], 4);
  var myLayer = L.mapbox.featureLayer().setGeoJSON(geojson).addTo(mapSimple);
  mapSimple.scrollWheelZoom.disable();
}
