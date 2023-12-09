from typing import List
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
        # TODO: implement me! CHECK if correct
        ...

        # get last inserted
        requested_node = self.heapStorage[self.currentHeapLastIndex]

        # print("requwest node: ", requested_node)

        #  print("~~START CITY MAX HEAP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(self.currentHeapLastIndex)
        #  print(self.heapStorage[self.currentHeapLastIndex])
        #  print(self.heapStorage[self.currentHeapLastIndex].name)
        #  print(self.heapStorage[self.currentHeapLastIndex].population)
        #  print(self.heapStorage[self.currentHeapLastIndex].country)

        #   print("~~END CITY MAX HEAP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        # check if node had parent
        while (self.has_parent(self.heapStorage.index(requested_node)) and requested_node.population >
               self.heapStorage[self.get_parent_index(self.heapStorage.index(requested_node))].population):
            #    print(" ########## i have parent")
            parent_index = self.get_parent_index(self.heapStorage.index(requested_node))
            #   print("current root bevore is: ", self.get_root_city())
            #   print("my parent is: ", parent_index)
            #   print("my parent name and poup: ", self.heapStorage[parent_index].name, " ", self.heapStorage[parent_index].population)
            #   print("my name and poup is: ", requested_node.name, " ", requested_node.population)
            self.swap_nodes(parent_index, self.heapStorage.index(requested_node))
            requested_node = self.heapStorage[parent_index]
        #   print("curent root after: ", self.get_root_city())

    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        # TODO: implement me! CHECK IF CORRECT
        ...

        # print("curent root bevore: ", self.get_root_city())

        requwest_node = self.heapStorage[index]
        parent_index = 0

        # rufe diese funktion selbst auf
        if self.has_parent(index) and index >= 0:
            parent_index = self.get_parent_index(index)
            # print("recusive up index and city and popup: ", index, " ", requwest_node.name, " ", requwest_node.population)
            # print("recusive up parent_index and parent_city and popup: ", parent_index, " ", self.heapStorage[parent_index].name, " ", self.heapStorage[parent_index].population)
            self.heapify_up_recursive(parent_index)

        self.swap_nodes(parent_index, index)

        # print("curent root after: ", self.get_root_city())

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

        # get parent, watch left child and watch right child
        # if one bigger swap
    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        # TODO: implement me!
        ...
    '''
    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        # TODO: implement me!
        ...

        for cit in self.heapStorage:
            indes = self.heapStorage.index(cit)
            if self.heapStorage[indes] != 0:
                # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                print(" ~~~~~~ ", indes)
                print(" ~~~~~~ Meine Stadt heißt: ", self.heapStorage[indes].name)
                self.currentHeapLastIndex = indes
                print("cur heap las in: ", self.currentHeapLastIndex)

        print("curent root bevore: ", self.heapStorage[0])

        print("curent last bevore: ", self.heapStorage[self.currentHeapLastIndex])

        self.swap_nodes(0, self.currentHeapLastIndex)
        self.heapStorage.pop(self.currentHeapLastIndex)

        for cit in self.heapStorage:
           # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            indes = self.heapStorage.index(cit)
            if self.heapStorage[indes] != 0:
                print(" ~~~~~~ ", indes)
                print(" ~~~~~~ Meine Stadt 2 heißt: ", self.heapStorage[indes].name)
                self.currentHeapLastIndex = indes
                print("cur heap 2 las in: ", self.currentHeapLastIndex)

        print("curent root after: ", self.heapStorage[0])
        print("curent last after: ", self.heapStorage[self.currentHeapLastIndex])

        if self.currentHeapLastIndex > 0:
            print("now sort heap after remove")
            self.heapify_down_recursive(0)
    '''