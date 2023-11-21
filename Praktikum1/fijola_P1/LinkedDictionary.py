# Aufabe 1a get mit Konstanter Laufzeit
import csv


class Node:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.next_node = None


class LinkedDictionary:
    def __init__(self):
        self.first = None

    def put_from_csv(self, filename: str):
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Ignoriere die erste Zeile
            for row in csv_reader:
                if len(row) >= 2:  # Sicherstellen, dass die Zeile mindestens zwei Elemente hat
                    key = row[0].strip()  # Linker Teil der Zeile als Key
                    value = row[1].strip()  # Rechter Teil der Zeile als Value
                    self.put(key, value)

    def put(self, key: str, value: str):
        new_node = Node(key, value)
        new_node.next_node = self.first
        self.first = new_node

    # get Funktion hat eine Laufzeit von O(n)
    def get(self, key):
        current_node = self.first
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next_node
        return None

    def get_key(self, key):
        current_node = self.first
        while current_node is not None:
            if current_node.key == key:
                return current_node.key
            current_node = current_node.next_node
        return None

    def get_all(self):
        result = {}
        current_node = self.first
        while current_node is not None:
            result[current_node.key] = current_node.value
            current_node = current_node.next_node
        return result
