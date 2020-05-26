import 'ol/ol.css';
import GeoJSON from 'ol/format/GeoJSON';
import TileLayer from 'ol/layer/Tile';
import Map from 'ol/Map';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import OSM from 'ol/source/OSM';
import View from 'ol/View';
import {fromLonLat} from 'ol/proj';

const vs = new VectorSource({
    format: new GeoJSON(),
    url: './data/permits.json'
})

new Map({
    target: 'map',
    layers: [
       new TileLayer({
            source: new OSM()
        }),
        new VectorLayer({
            source: new VectorSource({
                format: new GeoJSON(),
                url: 'http://localhost:5000/buildings',
                crossOrigin: 'anonymous',
            })
        }),
    ],
    view: new View({
        center: fromLonLat([-122.3, 47.6]),
        zoom: 4
    })
});
