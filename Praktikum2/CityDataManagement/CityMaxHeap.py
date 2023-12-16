from typing import List
from CityDataManagement.City import City
from CityDataManagement.AbstractCityHeap import AbstractCityHeap


class CityMaxHeap(AbstractCityHeap):
    """
    Class with the responsibility to create a Max-Heap-structure based on unstructured data.
    (Every Parents Key must be greater than its children Key)

    """

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        """
        Creation of a Max-City-Heap.

        :param raw_city_data:    A unsorted List of Cities
        :param recursive:    Should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
        :param floyd:       Should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.
                            For removal the approach specified in :param recursiv will be used.
        """
        super().__init__(raw_city_data, recursive, floyd)

    def heapify_up_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative upwards.
        """
        current_index = self.currentHeapLastIndex - 1

        while current_index > 0:
            parent_index = self.get_parent_index(current_index)

            node_population = self.heapStorage[current_index].population
            parent_population = self.heapStorage[parent_index].population

            if node_population > parent_population:
                self.swap_nodes(current_index, parent_index)
                current_index = parent_index
            else:
                return

    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        if index == 0:
            return

        parent_index = self.get_parent_index(index)

        if parent_index is None:
            return  # Invalid parent index

        node_population = self.get_city_population(index)
        parent_population = self.get_city_population(parent_index)

        if node_population is not None and parent_population is not None:
            if node_population > parent_population:
                self.swap_nodes(index, parent_index)
                self.heapify_up_recursive(parent_index)


    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions for a Max-Heap via Floyd's Heap Construction Algorithm.
        """

        i = index  # Starte mit dem angegebenen Index
        while i > 0:  # Solange bis die Wurzel erreicht ist (Index 0)
            parent_index = self.get_parent_index(i)

            if parent_index is not None:
                current_node = self.heapStorage[i]
                parent_node = self.heapStorage[parent_index]

                if current_node.population > parent_node.population:
                    self.swap_nodes(i, parent_index)

            i = parent_index  # Gehe zum Elternknoten


    def heapify_down_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative downwards.
        """
        root_index = 0

        while self.has_left_child(root_index):  # Solange es mindestens ein linkes Kind gibt
            left_child_index = self.get_left_child_index(root_index)
            right_child_index = self.get_right_child_index(root_index)

            # Bestimme das Kind mit dem größten Bevölkerungswert
            if right_child_index is not None and self.get_city_population(right_child_index) > self.get_city_population(left_child_index):
                larger_child_index = right_child_index
            else:
                larger_child_index = left_child_index

            # Vergleiche den Wurzelknoten mit dem größten Kind
            if self.get_city_population(root_index) < self.get_city_population(larger_child_index):
                self.swap_nodes(root_index, larger_child_index)
                root_index = larger_child_index
            else:
                return  # Heap-Bedingung erfüllt, breche ab

    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        if index == 0:  # Base case
            return

        if not self.has_left_child(index):
            return  # No left child, heap invariant is restored

        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)

        larger_child_index = left_child_index

        if self.has_right_child(index) and self.get_city_population(right_child_index) > self.get_city_population(left_child_index):
            larger_child_index = right_child_index

        if self.get_city_population(index) < self.get_city_population(larger_child_index):
            self.swap_nodes(index, larger_child_index)
            self.heapify_down_recursive(larger_child_index)

    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        if self.recursive:
            self.heapify_down_recursive(self.heapStorage[0])
        else:
            self.heapify_down_iterative()
