import 'ol/ol.css';
import GeoJSON from 'ol/format/GeoJSON';
import TileLayer from 'ol/layer/Tile';
import Map from 'ol/Map';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import View from 'ol/View';
import {fromLonLat} from 'ol/proj';

const vs = new VectorSource({
    format: new GeoJSON(),
    url: './data/countries.json'
})

new Map({
    target: 'map',
    layers: [
        new VectorLayer({
            source: new VectorSource({
                format: new GeoJSON(),
                url: './data/permits.json'
            })
        })
    ],
    view: new View({
        center: fromLonLat([-122.3, 47.6]),
        zoom: 4
    })
});
