from city_csv_parser.base import CityCsvParser

class SeattleCsvParser(CityCsvParser):
    def extract_all_long_lat_locations(self):
        return self.df[self.df['Longitude'].notna()][self.df['Latitude'].notna()][['Longitude', 'Latitude']].values
