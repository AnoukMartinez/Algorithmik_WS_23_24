from typing import List, Optional

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, key, value):
        if self.root is None:
            new_node = self.create_new_node(key, value)
            self.root = new_node
            return new_node
        else:
            return self._insert(key, value, self.root)

    def _insert(self, key, value, cur_node):
        if key < cur_node.key:
            if cur_node.left_child is None:
                new_node = self.create_new_node(key, value)
                cur_node.left_child = new_node
                cur_node.left_child.parent = cur_node  # set parent
                self._inspect_insertion(cur_node.left_child)
                return new_node
            else:
                return self._insert(key, value, cur_node.left_child)
        elif key > cur_node.key:
            if cur_node.right_child is None:
                new_node = self.create_new_node(key, value)
                cur_node.right_child = new_node
                cur_node.right_child.parent = cur_node  # set parent
                self._inspect_insertion(cur_node.right_child)
                return new_node
            else:
                return self._insert(key, value, cur_node.right_child)
        elif key == cur_node.key:
            updated_node = self.update_node(cur_node, value)
            return updated_node

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print('%s, h=%d' % (str(cur_node.key), cur_node.height))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None: return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    # find und search waren beinahe identisch, von daher habe ich search gelöscht
    def find(self, key):
        if self.root is not None:
            return self._find(key, self.root)
        else:
            return None

    def _find(self, key, cur_node):
        if key == cur_node.key:
            return cur_node
        elif key < cur_node.key and cur_node.left_child is not None:
            return self._find(key, cur_node.left_child)
        elif key > cur_node.key and cur_node.right_child is not None:
            return self._find(key, cur_node.right_child)

    def parse_tree(self, ngrams_array, curr_node, searched_nodes, word):
        if curr_node is not None:
            searched_nodes += 1
            if curr_node.key.startswith(word):
                ngrams_array.append((curr_node.key, curr_node.value))
            
            if curr_node.left_child is not None:
                ngrams_array, searched_nodes = self.parse_tree(ngrams_array, curr_node.left_child, searched_nodes, word)

            if curr_node.right_child is not None:
                ngrams_array, searched_nodes = self.parse_tree(ngrams_array, curr_node.right_child, searched_nodes, word)
        return ngrams_array, searched_nodes

    def find_most_likely_ngrams(self, word: str, root):
        ngrams_array = []
        searched_nodes = 0

        ngrams_array, searched_nodes = self.parse_tree(ngrams_array, root, searched_nodes, word)
        return ngrams_array, searched_nodes

    # OTHER AVL TREE FUNCTIONS

    def _inspect_insertion(self, cur_node, path=None):
        if path is None:
            path = []
        if cur_node.parent is None: return
        path = [cur_node] + path

        left_height = self.get_height(cur_node.parent.left_child)
        right_height = self.get_height(cur_node.parent.right_child)

        if abs(left_height - right_height) > 1:
            path = [cur_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    def _inspect_deletion(self, cur_node):
        if cur_node is None: return

        left_height = self.get_height(cur_node.left_child)
        right_height = self.get_height(cur_node.right_child)

        if abs(left_height - right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self, z, y, x):
        if y == z.left_child and x == y.left_child:
            self._right_rotate(z)
        elif y == z.left_child and x == y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right_child and x == y.right_child:
            self._left_rotate(z)
        elif y == z.right_child and x == y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: z,y,x Node configuration not recognized!')

    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left_child
        t3 = y.right_child
        y.right_child = z
        z.parent = y
        z.left_child = t3
        if t3 is not None: t3.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(self.get_height(z.left_child),
                           self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child),
                           self.get_height(y.right_child))

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right_child
        t2 = y.left_child
        y.left_child = z
        z.parent = y
        z.right_child = t2
        if t2 is not None: t2.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(self.get_height(z.left_child),
                           self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child),
                           self.get_height(y.right_child))

    def get_height(self, cur_node):
        if cur_node is None: return 0
        return cur_node.height

    def taller_child(self, cur_node):
        left = self.get_height(cur_node.left_child)
        right = self.get_height(cur_node.right_child)
        return cur_node.left_child if left >= right else cur_node.right_child

    def create_new_node(self, key, value):
        new_node = Node(key, value)
        return new_node

    def update_node(self, node_to_update, path_to_image):
        node_to_update.add_value(path_to_image)
        return node_to_update