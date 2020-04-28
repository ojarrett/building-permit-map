from city_csv_parser.specific.seattle import SeattleCsvParser
from city_csv_parser.utils import write_points_to_geojson

import sys

class SeattleWorkflow:
    def __init__(self, csv_file, out_file):
        self.csv_file = csv_file
        self.out_file = out_file

    def convert_csv_coords_to_geojson(self):
        parser = SeattleCsvParser(self.csv_file)
        parser.parse()
        write_points_to_geojson(parser.extract_all_long_lat_locations(), self.out_file)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python seattle.py <csv-file> <out-file>")
        sys.exit(1)

    workflow = SeattleWorkflow(csv_file=sys.argv[1], out_file=sys.argv[2])
    workflow.convert_csv_coords_to_geojson()
