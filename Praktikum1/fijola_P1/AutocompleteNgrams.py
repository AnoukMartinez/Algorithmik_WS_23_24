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
                # Prüfe, ob die Zeile leer ist
                if not row:
                    continue  # Wenn die Zeile leer ist, überspringe sie

                # Teile das erste Element der Reihe am Komma
                key_split = row[0].split(',')
                value_split = row[1].strip()
                #     print(f"SLITTING and KEY is {key_split} and VALUE is {value_split}")

                # Prüfe, ob sowohl Schlüssel als auch Wert vorhanden sind
                #  if len(key_split) == 1 & len(value_split) == 1:
                key = key_split
                value = value_split
                #    print(f"VAL is 2 and KEY is {key} and VALUE is {value}")
                self.avl_tree.insert(key, value)

    def get(self, ngram: str):
        """
        :param ngram: Das N-gram, welches gefunden werden soll.
        :return: Wenn das ngram gefunden wurde, wird die Frequenz des N-grams zurückgegeben,
                falls es nicht gefunden werden konnte wird None zurückgegeben.
        """

        # Rufe die search-Methode der AVLTree-Instanz auf
        result = self.avl_tree.search(ngram)

        if result is not None:
            print(f"Key --> {ngram} <-- found with value: {result}")
            return ngram
        else:
            print(f"Key --> {ngram} <-- not found its NONE.")
            return None

    def get_k_possible_suggestions(self, input_string: str, k: int):
        """
        :param input_string: Der String für den Fortsetzungen vorgeschlagen werden.
        :param k: Die Anzahl an gewünschten Vorschlägen.
        :return: Eine Liste mit den k Vorschlägen,
                die Anzahl untersuchter Nodes im AVL Baum.
        """

        suggestions = None
        searched_nodes = None

        result, nodes = self.avl_tree.find_most_likely_ngrams(input_string)
        print("Gegebenes Wort: ", input_string)
        print("Mögliche Fortsetzungen:", result)
        print("Anzahl der untersuchten Nodes:", nodes)

        # TODO: Filtern nach den meisten aufrufen (also der Zahlenwert im Value) und dann die k höchsten zurückgeben
        suggestions = result
        searched_nodes = nodes


        return suggestions, searched_nodes
