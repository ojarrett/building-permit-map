from city_csv_parser.specific.seattle import SeattleCsvParser
from city_csv_parser.utils import write_points_to_geojson

import sys

GEO_JSON_POINT_SELECTION_TYPES = ['all', 'largest']

class SeattleWorkflow:
    def __init__(self, csv_file, out_file):
        self.out_file = out_file
        self.parser = SeattleCsvParser(csv_file)

    def convert_all_csv_coords_sampled_to_geojson(self):
        self.parser.parse()
        self.parser.only_new_buildings()
        write_points_to_geojson(self.parser.extract_all_long_lat_locations(), self.out_file, sample=10)

    def largest_recent_developments_to_geojson(self):
        self.parser.parse()
        self.parser.only_new_buildings().select_most_recent(10000).select_buildings_most_units_added(1000)
        write_points_to_geojson(self.parser.extract_all_long_lat_locations(), self.out_file)

if __name__ == '__main__':
    if len(sys.argv) != 4 or not sys.argv[3] in GEO_JSON_POINT_SELECTION_TYPES:
        print("Usage: python seattle.py <csv-file> <out-file> <all|largest>")
        sys.exit(1)

    workflow = SeattleWorkflow(csv_file=sys.argv[1], out_file=sys.argv[2])
    if sys.argv[3] == 'all':
        workflow.convert_all_csv_coords_sampled_to_geojson()
    else:
        workflow.largest_recent_developments_to_geojson()
