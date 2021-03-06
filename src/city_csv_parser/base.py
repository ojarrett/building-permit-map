import pandas as pd

class CityCsvParser:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def parse(self):
        self.original_df = pd.read_csv(self.csv_file)
        self.current_df = self.original_df
