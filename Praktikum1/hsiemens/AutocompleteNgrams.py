import csv
from AVLTree import AVLTree


class AutocompleteNgrams:

    def __init__(self, filename: str):
        """ Initialisiert AutocompleteNgrams

        :param filename: Der Dateipfad zum csv file
        """
        self.avl_tree: AVLTree = AVLTree()
        self.read_csv_file(filename)

    def read_csv_file(self, filename: str):
        """ Liest die Daten von einem csv file und fügt sie dem self.avl_tree hinzu.

        :param filename: Der Dateipfad zum csv file
        """
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)

            for row in csv_reader:
                # TODO: Fügen Sie jede Reihe dem AVL Baum hinzu:
                if not row:
                    continue

                key, value = row[0], int(row[1])
                self.avl_tree.insert(key, value)

        """
        :param ngram: Das N-gram, welches gefunden werden soll.
        :return: Wenn das ngram gefunden wurde, wird die Frequenz des N-grams zurückgegeben,
                falls es nicht gefunden werden konnte wird None zurückgegeben.
        """

    def get(self, ngram: str):
        node = self.avl_tree.find(ngram)

        return ngram if node else None

    def get_most_likely_ngrams(self, word: str):
        suggestions, searched_nodes = self.avl_tree.find_most_likely_ngrams(word)
        return suggestions, searched_nodes

    def get_k_possible_suggestions(self, input_string: str, k: int):
        """
        :param input_string: Der String für den Fortsetzungen vorgeschlagen werden.
        :param k: Die Anzahl an gewünschten Vorschlägen.
        :return: Eine Liste mit den k Vorschlägen,
                die Anzahl untersuchter Nodes im AVL Baum.
        """
        # TODO: Implementieren Sie diese Methode
        suggestions, searched_nodes = self.get_most_likely_ngrams(input_string)

        # Sort suggestions based on frequency
        sorted_suggestions = sorted(suggestions.items(), key=lambda x: len(x[1]), reverse=True)

        # Get the top k suggestions
        top_k_suggestions = sorted_suggestions[:k]

        return top_k_suggestions, searched_nodes

