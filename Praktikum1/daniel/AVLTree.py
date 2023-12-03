class AVLNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

class AVLTree:
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

    def insert_csv_data(self, csv_file): # Mit CSV Daten fuellen
        import csv
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Erste Skippen
            for row in csv_reader:
                sentence = row[0]
                count = int(row[1])
                key = sentence
                self.root = self.insert(self.root, key, count)

    def get(self, key): # Pruefe ob Wort in Daten
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

    def _get_k_possible_suggestions(self, node, prefix, k, count, suggestions):
        while node is not None:
            if node.key.startswith(prefix):
                suggestions.append((node.key, node.data))
                count += 1
                if count == k:
                    break
                node = node.left
            elif prefix < node.key:
                node = node.left
            else:
                node = node.right

        if node is not None:
            count = self._get_k_possible_suggestions(node.left, prefix, k, count, suggestions)

        return count

    def get_k_possible_suggestions(self, prefix, k):
        suggestions = []
        count = self._get_k_possible_suggestions(self.root, prefix, k, 0, suggestions)
        sorted_suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)
        return sorted_suggestions[:k], count