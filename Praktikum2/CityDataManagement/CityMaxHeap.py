from time import sleep
from typing import List

import numba

from Praktikum2.CityDataManagement.City import City
from Praktikum2.CityDataManagement.AbstractCityHeap import AbstractCityHeap


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
        # TODO: implement me! CHECK if finish
        ...

        node_index = self.currentHeapLastIndex
        requested_node = self.heapStorage[node_index]

        while (self.has_parent(node_index) and requested_node.population >
               self.heapStorage[self.get_parent_index(node_index)].population):
            parent_index = self.get_parent_index(node_index)
            self.swap_nodes(parent_index, node_index)
            node_index = parent_index

    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        # Exercise
        ...
        if self.has_parent(index) and index >= 0:
            parent_index = self.get_parent_index(index)
            if self.get_city_population(parent_index) < self.get_city_population(index):
                self.swap_nodes(parent_index, index)
            self.heapify_up_recursive(parent_index)

    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions for a Max-Heap via Floyds Heap Construction Algorithmus.

        """
        # TODO: implement me! Check if finish
        ...

        self.heapify_down_iterative()

        '''
        last_leaf_index = index

        # Find the last leaf node with children
        while last_leaf_index >= 0 and not (
                self.has_left_child(last_leaf_index) or self.has_right_child(last_leaf_index)):
            last_leaf_index -= 1

        # Start building the heap from the last non-leaf node
        # for index in range(last_leaf_index, -1, -1):
        #    self.heapify_down_recursive(index)
        '''

    def heapify_down_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative downwards.
        """
        # Exercise

        heap_size = self.maximumHeapCapacity

        # Start from the last non-leaf node and go up to the root
        for index in range((heap_size // 2) - 1, -1, -1):
            while True:
                largest = index

                left_child_index = None
                right_child_index = None

                if self.has_left_child(index):
                    left_child_index = self.get_left_child_index(index)
                if self.has_right_child(index):
                    right_child_index = self.get_right_child_index(index)

                # Check if left child exists and is greater than the current largest
                if left_child_index is not None and self.heapStorage[
                    left_child_index] > self.heapStorage[largest]:
                    largest = left_child_index

                # Check if right child exists and is greater than the current largest
                if right_child_index is not None and self.heapStorage[
                    right_child_index] > self.heapStorage[largest]:
                    largest = right_child_index

                # If the largest element is the current element, no swap is needed
                if largest == index:
                    break

                # Swap the current node with the largest child
                self.swap_nodes(index, largest)

                # Update the index for the next iteration
                index = largest

    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        # Exercise

        largest = index
        left_child_index = None
        if self.has_left_child(index):
            left_child_index = self.get_left_child_index(index)
        right_child_index = None
        if self.has_right_child(index):
            right_child_index = self.get_right_child_index(index)

        # Check if left child exists and is greater than the current largest
        if left_child_index is not None and self.get_left_child_population(index) > self.get_city_population(largest):
            largest = left_child_index

        # Check if right child exists and is greater than the current largest
        if right_child_index is not None and self.get_right_child_population(index) > self.get_city_population(largest):
            largest = right_child_index

        # Swap the current node with the largest child if needed
        if largest != index:
            self.swap_nodes(index, largest)
            # Recursively heapify the affected sub-tree
            self.heapify_down_recursive(largest)

    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        # Exercise
        ...
        # 0. expect that heap is sorted
        my_dex = self.currentHeapLastIndex - 1
        # 1. swap first with last
        self.swap_nodes(0, my_dex)
        # 2. remove at last index
        #   pop remove on last index and return removed city
        removed_city = self.heapStorage.pop()
        self.currentHeapLastIndex = self.currentHeapLastIndex - 1
        # restore maxHeap
        if self.recursive or self.floyd:
            self.heapify_down_recursive(0)
        else:
            self.heapify_down_iterative()
        # return removed_city
        return removed_city
