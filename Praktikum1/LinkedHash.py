import csv
import os

# Eine Linked Hashmap die ich selbst implementiert habe.
# Hat allerdings eine Laufzeit von O(n) aufgrund der while Schleife in get()

class Node:
    def __init__(self, next, key, value):
        self.next = next
        self.data = (key, value)

class LinkedHashTable:
    def __init__(self):
        self.size = 997 # Könnte vielleicht auch von Größe der .csv abhängig gemacht werden?
        self.table = [None] * self.size

    # siehe Vorlesung 4, Folie 37
    def hash(self, key):
        output = 0
        for c in key:
            output += ord(c)
        return output % self.size

    def insert(self, key, value):
        index = self.hash(key)

        # Ich inserte den neuen Node hier am Anfang statt am Ende, damit ich
        # keine while Schleife benutzen muss (die hat sehr sehr lange gebraucht)
        if self.table[index] is None:
            self.table[index] = Node(None, key, value)
        else:
            node = self.table[index]
            self.table[index] = Node(node, key, value)

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
        index = self.hash(word)
        node = self.table[index]
        if node == None:
            return None
        if node.data[0] == word:
            return word
        else:
            while node.next != None:
                node = node.next
                if node.data[0] == word:
                    return word
        return None

linkedHash = LinkedHashTable()
linkedHash.read_csv_file("1_gram.csv")
print(linkedHash.get("dimwit"))
print(linkedHash.get("midwit"))