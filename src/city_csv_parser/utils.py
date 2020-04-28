from geojson import GeometryCollection
from geojson import Point

import json

def write_points_to_geojson(points, file_name):
    geo_collection = GeometryCollection([Point(coord[0], coord[1]) for coord in points])

    with open(file_name, 'w') as out_file:
        out_file.write(json.dumps(geo_collection))
