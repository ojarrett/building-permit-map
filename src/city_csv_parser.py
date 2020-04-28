import pandas as pd

class CityCsvParser:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def parse(self):
        return pd.read_csv(self.csv_file)
