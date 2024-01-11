import csv
from AVLTree_WordWeigh import AVLTree
import os


class AutocompleteNgrams:
    def __init__(self):
        self.array = [AVLTree() for _ in range(26)]

    def read_csv_file(self, filename: str):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, filename)

        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)

            number_of_words = 0
            for row in csv_reader:
                if len(row[0]) > 0:
                    first_letter = row[0][0]
                    letter_in_array = ord(first_letter) - 97

                    self.array[letter_in_array].insert(row[0], row[1])
                    number_of_words += 1
                else:
                    print("Leere Zeile gefunden in %d" % number_of_words)
                    # Optionales TODO: Balanciere Baum nach jedem Schritt
            print("Finished with %d words" % number_of_words)

    def get(self, ngram: str):
        first_letter = ngram[0]
        letter_in_array = ord(first_letter) - 97
        found_node = self.array[letter_in_array].find(ngram)
        if found_node is None:
            return None  # ngram nicht gefunden
        else:
            return found_node.value  # ngram gefunden, frequenz zurückgeben

    def get_k_possible_suggestions(self, input_string: str, k: int):
        first_letter = input_string[0]
        letter_in_array = ord(first_letter) - 97
        tree = self.array[letter_in_array]
        ngrams_array, searched_nodes = tree.find_most_likely_ngrams(input_string, tree.root)

        ngrams_array = filter(lambda x: x[0] != input_string, ngrams_array)
        ngrams_array = sorted(ngrams_array, key=lambda x: int(x[1]), reverse=True)

        return ngrams_array[:k], searched_nodes

# autocomplete = AutocompleteNgrams()
# autocomplete.read_csv_file("1_gram.csv")
# print(autocomplete.get("dimwit"))
# print(autocomplete.get("midwit"))

# suggestions, searched_nodes = autocomplete.get_k_possible_suggestions("tom", 10)
# print(suggestions)
# print(searched_nodes)
