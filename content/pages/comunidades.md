Title: Comunidades

<link rel="stylesheet" href="//unpkg.com/leaflet@1.0.3/dist/leaflet.css"
  integrity="sha512-07I2e+7D8p6he1SIM+1twR5TIrhUQn9+I6yjqD53JQjFiMf8EtC93ty0/5vJTZGF8aAocvHYNEDJajGdNx1IsQ"
  crossorigin=""/>
<script src="//unpkg.com/leaflet@1.0.3/dist/leaflet.js"
  integrity="sha512-A7vV8IFfih/D732iSSKi20u/ooOfj/AGehOKq0f4vLT1Zr2Y+RX7C+w8A1gaSasGtRUZpF/NZgzSAu4/Gc41Lg"
  crossorigin=""></script>

Aquí puedes encontrar las comunidades de Python en España. Si crees que falta alguna, [¡puedes añadirla!](https://github.com/python-spain/python-spain.github.io/edit/master/content/pages/comunidades.md)

<div id="map" style="height: 600px"></div>

<script>
var map = L.map('map', {
    center: [36.014, -5.120],
    zoom: 5
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

function addLocation(loc_data) {
    var title = loc_data[2];
    var popupText = title;

    if (loc_data.length > 3) {
      var link = loc_data[3];
      popupText = `<a href="${link}" title="${title}">${title}</a>`;
    }

    var icon = L.icon({
      iconUrl: '/images/python-marker.png',
      iconSize: [20, 28],
      iconAnchor: [10, 28],
      popupAnchor: [0, -28]
    });

    L.marker([loc_data[0], loc_data[1]], {icon: icon})
        .bindPopup(popupText)
        .addTo(map);
}

var locations = [
    [40.41664, -3.70381, 'Python Madrid', 'http://www.python-madrid.es/'],
    [42.1986, -8.7726, 'Python Vigo', 'http://www.python-vigo.es/'],
    [36.7644, -4.4242, 'Python Málaga', 'https://www.meetup.com/es-ES/python_malaga/'],
    [39.4227, -0.3525, 'Python Valencia', 'http://www.meetup.com/es-ES/Python-Valencia-Meetup/'],
    [41.3929, 2.1404, 'PyBCN', 'http://pybcn.org/'],
    [39.6602, 2.9862, 'Python Mallorca', 'http://www.meetup.com/es-ES/Mallorca-Python-Meetup/'],
    [37.3766, -5.926, 'Python Sevilla', 'http://www.meetup.com/es-ES/Python-Sevilla/'],
    [41.692, -0.9271, 'PythonZaragoza'],
    [37.1809, -3.5983, 'Python Granada', 'http://www.python-granada.es/'],
    [28.4811, -16.3227, 'Python Canarias', 'http://pythoncanarias.es/'],
    [38.3453, -0.4831, 'Python Alicante', 'https://twitter.com/python_alc'],
    [43.2918, -1.9889, 'Python San Sebastián', 'http://pyss.org/'],
    [41.9830495, 2.8245813, 'Python Girona', 'https://pythongirona.cat/'],
    [40.4126148, -3.7138357, 'PyData Madrid', 'https://www.meetup.com/PyData-Madrid/'],
    [39.6149, 2.9527, 'PyData Mallorca', 'https://www.meetup.com/PyData-Mallorca/'],
    [36.842512, -2.457619, 'Python Almería', 'https://www.meetup.com/Python-Almeria/'],
    [40.417037, -3.702626, 'PyLadies Madrid', 'https://www.meetup.com/es-ES/PyLadiesMadrid/'],
    [40.961613, -5.667607, 'PyData Salamanca', 'https://www.meetup.com/PyData-Salamanca/'],
    [39.478848, -6.342179, 'ExtrePython', 'https://twitter.com/ExtrePython'],
    [42.81692, -1.64286, 'Python Navarra', 'https://twitter.com/pythonnavarra'],
    [37.990434, -1.133015, 'Python Murcia', 'https://twitter.com/pythonmurcia'],
    [37.883333, -4.766667, 'Python Cordoba'],
    [41.652778, -4.723611, 'Python Valladolid']
];
locations.forEach(addLocation);

</script>
