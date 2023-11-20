import csv
import os

# Eine Hashmap, die die Python Dictionary Bibliothek verwendet.
# Deutlich schneller als meine selbstgebackene Implementierung, und weniger Kollisionen.
# Worst Case ist ebenfalls O(n), aber nur wenn viele Wörter in den selben Bucket gehasht wurden.

class LibraryHash:
    def __init__(self):
        self.table = {}

    '''
    def hash(self, key):
        output = 0
        for c in key:
            output += ord(c)
        return output % self.size
    '''

    def insert(self, key, value):
        self.table[key] = value

    def read_csv_file(self, filename: str):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, filename)

        numberOfWords = 0
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                numberOfWords += 1
                self.insert(row[0], row[1])

        print("Fertig mit insgesamt %d Worten" % (numberOfWords))

    def get(self, word: str):
        try:
            node = self.table[word]
            return word
        except:
            return None

linkedHash = LibraryHash()
linkedHash.read_csv_file("1_gram.csv")
print(linkedHash.get("dimwit"))
print(linkedHash.get("midwit"))