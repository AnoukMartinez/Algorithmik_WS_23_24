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
        # Wir rufen diese Methode JEDES mal auf wenn eine neue Node eingefügt wird
        # Wir fangen also immer da an, wo als letztes ne Node eingefügt wurde
        # Und zwar in insert in AbstractCityHeap.py
        current_index = self.currentHeapLastIndex - 1
        parent_index = self.get_parent_index(current_index)

        while current_index > 0:
            node_population = self.heapStorage[current_index].population
            parent_population = self.heapStorage[parent_index].population

            if node_population > parent_population:
                self.swap_nodes(current_index, parent_index)
                # Setze node values neu
                current_index = parent_index
                parent_index = self.get_parent_index(current_index)
            else:
                return # Sonst: Nicht mehr größer als, kann terminieren

    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        if index == 0:
            return
        
        parent_index = self.get_parent_index(index)
        
        node_population = self.heapStorage[index].population
        parent_population = self.heapStorage[parent_index].population

        if node_population > parent_population:   
            self.swap_nodes(index, parent_index)
            self.heapify_up_recursive(parent_index)

    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions for a Max-Heap via Floyds Heap Construction Algorithmus.
        
        """
        # TODO: implement me!
        ...

    def heapify_down_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative downwards.
        """
        # TODO: implement me!
        ...

    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        # TODO: implement me!
        ...

    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        # TODO: implement me!
        ...