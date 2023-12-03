import timeit


class AVLNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.height = 1


class AVLTree:

    # BASE SETUP

    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        self.update_height(z)
        self.update_height(y)

        return y

    def rotate_left(self, y):
        x = y.right
        T2 = x.left

        x.left = y
        y.right = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def insert(self, node, key, data):
        if node is None:
            return AVLNode(key, data)

        if key < node.key:
            node.left = self.insert(node.left, key, data)
        elif key > node.key:
            node.right = self.insert(node.right, key, data)
        else:
            node.data = data
            return node

        self.update_height(node)

        balance = self.balance_factor(node)

        # Links
        if balance > 1:
            if key < node.left.key:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        # Rechts
        if balance < -1:
            if key > node.right.key:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    # BASE SETUP END

    # CSV TO DATA

    def insert_csv_data(self, csv_file):  # Mit CSV Daten fuellen
        import csv
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Erste Skippen
            for row in csv_reader:
                sentence = row[0]
                count = int(row[1])
                key = sentence
                self.root = self.insert(self.root, key, count)

    def insert_csv_data_TIME(self, csv_file):  # Mit CSV Daten fuellen
        start_time = timeit.default_timer()
        import csv
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Erste Skippen
            for row in csv_reader:
                sentence = row[0]
                count = int(row[1])
                key = sentence
                self.root = self.insert(self.root, key, count)

        end_time = timeit.default_timer()
        gone_time = end_time - start_time

        return gone_time

    # CSV TO DATA END

    def get(self, key):  # Pruefe ob Wort in Daten
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.key
        elif key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)

    def _get_k_possible_suggestions(self, node, preword, k, suggestions):  # O(log(n)) - O(n) - best/worstss
        # case - je nachdem ob balanced tree oder nicht

        CountFound = 0  # stellt sicher das genau (k) gefunden werden
        count = 0  # Anzahl untersuchter Nodes

        while node is not None:

            count += 1

            if node.key.startswith(preword):
                suggestions.append((node.key, node.data))
                CountFound += 1
                if CountFound == k:
                    break
                node = node.left
            elif preword < node.key:
                node = node.left
            else:
                node = node.right

        return count

    def get_k_possible_suggestions(self, preword, k):
        suggestions = []
        count = self._get_k_possible_suggestions(self.root, preword, k,  suggestions)
        sorted_suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)  # O(k log k)
        return sorted_suggestions[:k], count

    # WITH TIMER

    def _get_k_possible_suggestions_TIME(self, node, preword, k, suggestions):
        start_time = timeit.default_timer()

        CountFound = 0  # stellt sicher das genau (k) gefunden werden
        count = 0  # Anzahl untersuchter Nodes

        while node is not None:

            count += 1

            if node.key.startswith(preword):
                suggestions.append((node.key, node.data))
                CountFound += 1
                if CountFound == k:
                    break
                node = node.left
            elif preword < node.key:
                node = node.left
            else:
                node = node.right

        end_time = timeit.default_timer()
        gone_time = end_time - start_time

        return count, gone_time

    def get_k_possible_suggestions_TIME(self, preword, k):
        suggestions = []
        count, gone_time = self._get_k_possible_suggestions_TIME(self.root, preword, k, suggestions)
        sorted_suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)
        return sorted_suggestions[:k], count, gone_time
