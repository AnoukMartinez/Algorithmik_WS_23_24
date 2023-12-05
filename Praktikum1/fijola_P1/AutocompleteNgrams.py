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

        anzahl = 0
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
                anzahl = anzahl + 1
        print("Anzahl an WORTEN IM FILE: ", anzahl)

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
        print("Anzahl an Vorschlägen: ", k)
        print("Mögliche Fortsetzungen:", result)
        print("Anzahl der untersuchten Nodes:", nodes)

        # Filtern nach den meisten Aufrufen
        sorted_suggestions = sorted(result.items(), key=lambda x: int(x[1]), reverse=True)
        top_k_suggestions = sorted_suggestions[:k]

        suggestions = [item[0] for item in top_k_suggestions]
        searched_nodes = nodes

        return suggestions, searched_nodes

    def get_k_possible_suggestions_alphabetical_asc(self, input_string: str, k: int):
        """
        :param input_string: Der String für den Fortsetzungen vorgeschlagen werden.
        :param k: Die Anzahl an gewünschten Vorschlägen.
        :return: Eine Liste mit den k Vorschlägen,
                die Anzahl untersuchter Nodes im AVL Baum.
        """

        # Initialisiere die Variablen für Vorschläge und untersuchte Nodes
        suggestions = None
        searched_nodes = None

        # Rufe die Methode find_most_likely_ngrams des AVL-Baums auf
        result, nodes = self.avl_tree.find_most_likely_ngrams(input_string)

        # Debug-Ausgabe für gegebenes Wort, Anzahl der Vorschläge und mögliche Fortsetzungen
        print("Gegebenes Wort: ", input_string)
        print("Anzahl an Vorschlägen: ", k)
        print("Mögliche Fortsetzungen:", result)
        print("Anzahl der untersuchten Nodes:", nodes)

        # Sortiere die Vorschläge nach der beschriebenen Logik:
        # 1. Sortiere absteigend nach der Häufigkeit (Value) der Vorschläge (-int(node[1]))
        # 2. Wenn zwei Vorschläge die gleiche Häufigkeit haben, sortiere aufsteigend nach dem Vorschlagswort (node[0]).
        #    Das bedeutet, dass Wörter mit dem gleichen Häufigkeitswert alphabetisch aufsteigend sortiert werden.
        # 3. Begrenze die sortierte Liste auf die ersten k Elemente, um nur die gewünschte Anzahl an Vorschlägen zu erhalten.

        suggestions = [key for key, _ in sorted(result.items(), key=lambda node: (-int(node[1]), node[0]))[:k]]

        # Überprüfe, ob der Key im input_string ist und füge ihn am Anfang der Liste hinzu
        if input_string in suggestions:
            suggestions.remove(input_string)
            suggestions.insert(0, input_string)

        searched_nodes = nodes

        # Gib die Vorschläge und die Anzahl der untersuchten Nodes zurück
        return suggestions, searched_nodes

    def get_k_possible_suggestions_alphabetical_desc(self, input_string: str, k: int):
        """
        :param input_string: Der String für den Fortsetzungen vorgeschlagen werden.
        :param k: Die Anzahl an gewünschten Vorschlägen.
        :return: Eine Liste mit den k Vorschlägen,
                die Anzahl untersuchter Nodes im AVL Baum.
        """

        # Initialisiere die Variablen für Vorschläge und untersuchte Nodes
        suggestions = None
        searched_nodes = None

        # Rufe die Methode find_most_likely_ngrams des AVL-Baums auf
        result, nodes = self.avl_tree.find_most_likely_ngrams(input_string)

        # Debug-Ausgabe für gegebenes Wort, Anzahl der Vorschläge und mögliche Fortsetzungen
        print("Gegebenes Wort: ", input_string)
        print("Anzahl an Vorschlägen: ", k)
        print("Mögliche Fortsetzungen:", result)
        print("Anzahl der untersuchten Nodes:", nodes)

        # Sortiere die Vorschläge nach der angepassten Logik:
        # 1. Sortiere absteigend nach der Häufigkeit (Value) der Vorschläge (-int(node[1]))
        # 2. Wenn zwei Vorschläge die gleiche Häufigkeit haben, sortiere aufsteigend nach dem ersten Buchstaben des Vorschlagswortes (node[0]).
        #    Das bedeutet, dass Wörter mit dem gleichen Häufigkeitswert alphabetisch aufsteigend sortiert werden.
        # 3. Begrenze die sortierte Liste auf die ersten k Elemente, um nur die gewünschte Anzahl an Vorschlägen zu erhalten.

        suggestions = [key for key, _ in sorted(result.items(), key=lambda node: (-int(node[1]), node[0][0]))[:k]]

        # Überprüfe, ob der Key im input_string ist und füge ihn am Anfang der Liste hinzu
        if input_string in suggestions:
            suggestions.remove(input_string)
            suggestions.insert(0, input_string)

        searched_nodes = nodes

        # Gib die Vorschläge und die Anzahl der untersuchten Nodes zurück
        return suggestions, searched_nodes  # Geschätzte Laufzeitkomplexität: O(n * log(n)), wobei n die Anzahl der Einträge im AVL-Baum ist.
