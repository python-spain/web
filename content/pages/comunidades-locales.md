Title: Comunidades locales

<link rel="stylesheet" href="//unpkg.com/leaflet@1.0.3/dist/leaflet.css"
  integrity="sha512-07I2e+7D8p6he1SIM+1twR5TIrhUQn9+I6yjqD53JQjFiMf8EtC93ty0/5vJTZGF8aAocvHYNEDJajGdNx1IsQ"
  crossorigin=""/>
<link rel="stylesheet" href="//unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.css"
  integrity="sha384-lPzjPsFQL6te2x+VxmV6q1DpRxpRk0tmnl2cpwAO5y04ESyc752tnEWPKDfl1olr" crossorigin=""/>
<link rel="stylesheet" href="//unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.Default.css"
  integrity="sha384-5kMSQJ6S4Qj5i09mtMNrWpSi8iXw230pKU76xTmrpezGnNJQzj0NzXjQLLg+jE7k" crossorigin=""/>

<script src="//unpkg.com/leaflet@1.0.3/dist/leaflet.js"
  integrity="sha512-A7vV8IFfih/D732iSSKi20u/ooOfj/AGehOKq0f4vLT1Zr2Y+RX7C+w8A1gaSasGtRUZpF/NZgzSAu4/Gc41Lg"
  crossorigin=""></script>
<script src="//unpkg.com/leaflet.markercluster@1.4.1/dist/leaflet.markercluster.js"
  integrity="sha384-RLIyj5q1b5XJTn0tqUhucRZe40nFTocRP91R/NkRJHwAe4XxnTV77FXy/vGLiec2" crossorigin=""></script>

<style>
.groupPopup {
    text-align: center;
}
.groupPopup a {
    text-decoration: none !important;
    font-size: large;
    color: #000;
}
</style>

¡Python se disfruta mejor en compañía! Aquí puedes ver las comunidades locales de Python en España, enlaces a sus redes sociales y vídeo de presentación. Encuentra el grupo que más cerca te queda y conecta con gente como tú.

¿Crees que falta alguna? [¡Puedes añadirla!](https://github.com/python-spain/python-spain.github.io/edit/master/content/pages/comunidades-locales.md)

¿No hay un grupo en tu zona y te gustaría crearlo? Escríbenos a [contacto@es.python.org](mailto:contacto@es.python.org) y te ayudaremos en todo lo que podamos. :)

<div id="map" style="height: 600px"></div>

<script>
const map = L.map('map', {
    center: [36.014, -5.120],
    zoom: 5
});

const markers = L.markerClusterGroup({maxClusterRadius: 10});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


const icon = L.icon({
    iconUrl: '/images/python-marker.png',
    iconSize: [20, 28],
    iconAnchor: [10, 28],
    popupAnchor: [0, -28]
});

function addGroup(group) {
    let socials = []
    if (group.web) {
        socials.push(`<a title="web" class="fas fa-globe-americas" href="${group.web}" target="_blank"></a>`)
    }
    if (group.meetup) {
        socials.push(`<a title="meetup" class="fab fa-meetup" href="${group.meetup}" target="_blank"></a>`)
    }
    if (group.twitter) {
        socials.push(`<a title="twitter" class="fab fa-twitter" href="${group.twitter}" target="_blank"></a>`)
    }
    if (group.telegram) {
        socials.push(`<a title="telegram" class="fab fa-telegram" href="${group.telegram}" target="_blank"></a>`)
    }
    if (group.email) {
        socials.push(`<a title="email" class="fa fa-envelope-open-text" href="mailto:${group.email}" target="_blank"></a>`)
    }
    if (group.video) {
        socials.push(`<a title="video" class="fas fa-video" href="${group.video}" target="_blank"></a>`)
    }
    const socialsString = socials.join(" ");

    const popupText = `<div class="groupPopup"><b>${group.name}</b><br />${socialsString}</div>`;

    const marker = L.marker([group.latitude, group.longitude], {icon: icon}).bindPopup(popupText);

    markers.addLayer(marker);
}

const groups = [
    {
        name: 'Python Vigo',
        latitude: 42.19864,
        longitude: -8.7726,
        web: 'http://www.python-vigo.es/',
        twitter: 'https://twitter.com/python_vigo',
        telegram: 'https://t.me/joinchat/AAAAAAfW2-q8miOKsVGjCg',
        email: 'vigo@lists.es.python.org',
    },
    {
        name: 'Python Málaga',
        latitude: 36.7644,
        longitude: -4.4242,
        web: 'https://www.python-malaga.es/',
        meetup: 'https://www.meetup.com/es-ES/python_malaga/',
        twitter: 'https://twitter.com/python_malaga',
        telegram: 'https://t.me/python_malaga',
        email: 'python.malaga@gmail.com',
        video: 'https://www.youtube.com/watch?v=wnhtNjsSLe8',
    },
    {
        name: 'Python Valencia',
        latitude: 39.4227,
        longitude: -0.3525,
        web: 'http://www.meetup.com/es-ES/Python-Valencia-Meetup/',
        twitter: 'https://twitter.com/python_vlc',
    },
    {
        name: 'PyBCN',
        latitude: 41.3929,
        longitude: 2.1404,
        web: 'http://pybcn.org/',
        meetup: 'https://www.meetup.com/es-ES/python-barcelona/',
        twitter: 'https://twitter.com/PyBCN',
        email: 'pybcn@googlegroups.com',
        video: 'https://www.youtube.com/watch?v=JYCcPr4QW_k',
    },
    {
        name: 'Mallorca Python',
        latitude: 39.6602,
        longitude: 2.9862,
        meetup: 'https://www.meetup.com/es-ES/Mallorca-Python-Meetup/',
        twitter: 'https://twitter.com/MallorcaPython',
        video: 'https://www.youtube.com/watch?v=CDmqQBreRmk',
    },
    {
        name: 'Python Sevilla',
        latitude: 37.3766,
        longitude: -5.926,
        web: 'https://python-sevilla.github.io/',
        meetup: 'https://www.meetup.com/es-ES/Python-Sevilla/',
        twitter: 'https://twitter.com/python_sevilla',
        telegram: 'https://t.me/pythonsevilla',
        video: 'https://www.youtube.com/watch?v=x0YF9q1pJcY',
    },
    {
        name: 'Python Granada',
        latitude: 37.1809,
        longitude: -3.5983,
        twitter: 'https://twitter.com/python_granada',
        email: 'pythongranada@gmail.com',
        video: 'https://www.youtube.com/watch?v=pgKXhg0cDyE',
    },
    {
        name: 'Python Canarias',
        latitude: 28.4811,
        longitude: -16.3227,
        web: 'http://pythoncanarias.es/',
        twitter: 'https://twitter.com/pythoncanarias',
        telegram: 'https://t.me/joinchat/AJ7pmT-X0xZVPgWDIzGA-A',
        email: 'info@pythoncanarias.es',
        video: 'https://www.youtube.com/watch?v=6QxgyXe7_RA',
    },
    {
        name: 'Python Alicante',
        latitude: 38.3453,
        longitude: -0.4831,
        meetup: 'https://www.meetup.com/es-ES/python_alc/',
        twitter: 'https://twitter.com/python_alc',
        telegram: 'https://t.me/python_alc',
        discord: 'https://discord.gg/5AZkkC9egw',
        email: 'pyalicante@gmail.com',
        video: 'https://www.youtube.com/watch?v=Om2kcuqvAsM',
    },
    {
        name: 'Python San Sebastián',
        latitude: 43.2918,
        longitude: -1.9889,
        web: 'https://pyss.org/',
        twitter: 'https://twitter.com/acpyss',
    },
    {
        name: 'Python Girona',
        latitude: 41.9830495,
        longitude: 2.8245813,
        web: 'https://pythongirona.cat',
        meetup: 'https://www.meetup.com/es-ES/PythonGirona/',
        twitter: 'https://twitter.com/PythonGirona',
        email: 'info@pythongirona.cat',
    },
    {
        name: 'Python Madrid',
        latitude: 40.41664,
        longitude: -3.70381,
        web: 'https://www.python-madrid.es/',
        meetup: 'https://www.meetup.com/python-madrid/',
        twitter: 'https://twitter.com/python_madrid',
        video: 'https://www.youtube.com/watch?v=kaJTW_yZDm0',
    },
    {
        name: 'PyLadies Madrid',
        latitude: 40.417037,
        longitude: -3.702626,
        web: 'http://madrid.pyladies.com/',
        meetup: 'https://www.meetup.com/es-ES/PyLadiesMadrid/',
        twitter: 'https://twitter.com/pyladiesmadrid',
        email: 'madrid@pyladies.com',
        video: 'https://www.youtube.com/watch?v=2H6wASZfGxQ',
    },
    {
        name: 'PyData Mallorca',
        latitude: 39.6149,
        longitude: 2.9527,
        meetup: 'https://www.meetup.com/PyData-Mallorca/',
        twitter: 'https://twitter.com/PyDataMallorca',
    },
    {
        name: 'Python Almería',
        latitude: 36.842512,
        longitude: -2.457619,
        meetup: 'https://www.meetup.com/Python-Almeria/',
        video: 'https://www.youtube.com/watch?v=Doub2vARmrc',
    },
    {
        name: 'PyData Salamanca',
        latitude: 40.961613,
        longitude: -5.667607,
        meetup: 'https://www.meetup.com/es-ES/PyData-Salamanca/',
        twitter: 'https://twitter.com/pydatalabUSAL',
        email: 'coordinaciondatalab@gmail.com',
        video: 'https://www.youtube.com/watch?v=WeGSIZ-3SI8',
    },
    {
        name: 'ExtrePython',
        latitude: 39.478848,
        longitude: -6.342179,
        twitter: 'https://twitter.com/ExtrePython',
    },
    {
        name: 'Python Navarra',
        latitude: 42.81692,
        longitude: -1.64286,
        twitter: 'https://twitter.com/pythonnavarra',
        email: 'pythonnavarra@gmail.com',
        video: 'https://www.youtube.com/watch?v=C-vdmYFfWck',
    },
    {
        name: 'Python Murcia',
        latitude: 37.990434,
        longitude: -1.133015,
        twitter: 'https://twitter.com/pythonmurcia',
        telegram: 'https://t.me/pythonmurcia',
        email: 'pythonmurcia@gmail.com',
        video: 'https://www.youtube.com/watch?v=BgnbYAZTMDQ',
    },
    {
        name: 'Python Córdoba',
        latitude: 37.883333,
        longitude: -4.766667,
        meetup: 'https://www.meetup.com/es-ES/Meetup-de-Python-en-Cordoba/',
    },
    {
        name: 'Python CyL',
        latitude: 41.652778,
        longitude: -4.723611,
        telegram: 'https://t.me/PyCyL',
        video: 'https://www.youtube.com/watch?v=WeGSIZ-3SI8',
    },
    {
        name: 'PyLadies Barcelona',
        latitude: 41.3959,
        longitude: 2.1404,
        web: 'https://pybcn.org/pyladies_bcn/about/',
        meetup: 'https://www.meetup.com/PyLadies-BCN/',
        twitter: 'https://twitter.com/PyLadies_BCN',
        mail: 'pyladies-bcn@googlegroups.com',
        video: 'https://www.youtube.com/watch?v=JYCcPr4QW_k',
    },
]

groups.forEach(addGroup);
map.addLayer(markers);

</script>
