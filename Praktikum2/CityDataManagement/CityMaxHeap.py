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
        # TODO: implement me!
        ...

    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        # TODO: implement me!
        ...

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
