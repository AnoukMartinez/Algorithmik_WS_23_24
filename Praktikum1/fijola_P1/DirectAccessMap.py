# Aufgabe 1a get mit konstanter Laufzeit

import csv


class DirectAccessMap:
    def __init__(self):
        self.data_dict = {}

    def put(self, key, value):
        self.data_dict[key] = value

    def put_from_csv(self, filename):
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Ignoriere die erste Zeile
            for row in csv_reader:
                if len(row) >= 2:
                    key = row[0].strip()
                    value = row[1].strip()
                    self.put(key, value)

    # get Funktion hat eine Laufzeit von O(1) mit direktem Zugriff
    def get(self, key):
        return self.data_dict.get(key, None)

    def get_key(self, key):
        return key if key in self.data_dict else None

    def get_all(self):
        return self.data_dict
