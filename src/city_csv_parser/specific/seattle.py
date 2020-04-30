from city_csv_parser.base import CityCsvParser

class SeattleCsvParser(CityCsvParser):
    def only_new_buildings(self):
        self.current_df = self.current_df[self.current_df['HousingUnitsAdded'] > 0]
        return self

    def select_buildings_most_units_added(self,count=100):
        self.current_df = self.current_df.sort_values(by="HousingUnitsAdded", ascending=False)[0:count]
        return self

    def select_most_recent(self,count=100):
        self.current_df = self.current_df.sort_values(by="AppliedDate", ascending=False)[0:count]
        return self

    def extract_all_long_lat_locations(self):
        return self.current_df[
                (self.current_df['Longitude'].notna()) & (self.current_df['Latitude'].notna())
            ][['Longitude', 'Latitude']].values
