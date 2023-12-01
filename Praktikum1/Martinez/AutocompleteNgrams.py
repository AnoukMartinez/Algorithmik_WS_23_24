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
                ...

    def get(self, ngram: str):
        """
        :param ngram: Das N-gram, welches gefunden werden soll.
        :return: Wenn das ngram gefunden wurde, wird die Frequenz des N-grams zurückgegeben,
                falls es nicht gefunden werden konnte wird None zurückgegeben.
        """
        # TODO: Implementieren Sie diese Methode

    def get_k_possible_suggestions(self, input_string: str, k: int):
        """
        :param input_string: Der String für den Fortsetzungen vorgeschlagen werden.
        :param k: Die Anzahl an gewünschten Vorschlägen.
        :return: Eine Liste mit den k Vorschlägen,
                die Anzahl untersuchter Nodes im AVL Baum.
        """
        # TODO: Implementieren Sie diese Methode
        suggestions = None
        searched_nodes = None

        return suggestions, searched_nodes

