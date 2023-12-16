import math
from abc import ABC, abstractmethod
from typing import List
from Praktikum2.CityDataManagement.City import City


class AbstractCityHeap(ABC):
    """
    Abstract Class with the responsibility to offer the common methods of both a Min and Max heap.

    This class is divided into two parts:

    -Abstract Methods Block (Methods necessary for both a min and a max heap but with different implementations)

    -Shared Methods Block (Methods identical for both a min and a max heap)


    Param:
    ------
    rawCityData: List[City]: raw unsorted List of City Objects

    recursiv: bool: should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
    
    floyd: bool: should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.

    Hint:   
    -----
    Think of the index of all elements in the heap as an array. Array: ([0],[1],[2],[3]...)
    The root is located at index 0, so it`s children must be on Index 1 and 2 and so on...
    """

    heapStorage: List[City] = [0]  # empty List of City Objects
    maximumHeapCapacity = 0
    currentHeapLastIndex = 0  # current last Index of the Heap based on the inserted City Objects, this is also the current Size of the Heap
    rawCityData: List[City]

    recursive: bool = False
    floyd: bool = False

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        self.rawCityData = raw_city_data
        self.maximumHeapCapacity = len(self.rawCityData)  # set Maximum Heap Capacity to the amount of City Objects
        self.heapStorage = self.heapStorage * self.maximumHeapCapacity

        self.recursive = recursive
        self.floyd = floyd

        self.insert_raw_city_data_into_heap()

    # ----Abstract Methods Block (Methods necessary for both a min and a max heap but with different implementations)--

    @abstractmethod
    def heapify_up_iterative(self):
        """
        Establish heap conditions iterative upwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_up_recursive(self, index):
        """
        Establish heap conditions recursive upwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions via Floyds Heap Construction Algorithmus
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_down_iterative(self):
        """
        Establish heap conditions iterative downwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_down_recursive(self, index):
        """
        Establish heap conditions recursive downwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def remove(self):
        """
        Remove a City from the Heap.
        """
        ...
        raise NotImplementedError

    # ------Shared Methods Block (Methods identical for both a min and a max heap)------

    def insert_raw_city_data_into_heap(self):
        """
        Insertion of all cities into the Heap.
        """

        if self.floyd:
            self.build_heap_via_floyd()
        else:
            for i in self.rawCityData:
                self.insert(i)

    def insert(self, city):
        """
        Insert a single City into the Heap.
        """
        # TODO: implement me! CHECK if FINISH
        ...
        if self.check_if_heap_is_full() is True:
            # print(" -----------> ", city)
            # print(" -----------> Heap is full, can not insert")
            # print(" -----------> Heap expand now with append")
            self.heapStorage.append(0)

        if self.recursive:
            try:
                self.heapStorage[self.currentHeapLastIndex] = city
                self.heapify_up_recursive(self.currentHeapLastIndex)
            except IndexError:
                print("Heap is full, can not insert recursive")

        else:
            try:
                self.heapStorage[self.currentHeapLastIndex] = city
                self.heapify_up_iterative()
            except IndexError:
                print("Heap is full, can not insert iterative")
        self.currentHeapLastIndex = self.currentHeapLastIndex + 1

    def build_heap_via_floyd(self):
        """
        Build a Heap via Floyds Heap Construction Algorithm from a unsorted List Of Cities.
        """
        # TODO: implement me! CHECK if FINISH
        ...
        for city in self.rawCityData:
            if self.check_if_heap_is_full() is False:
                self.heapStorage[self.currentHeapLastIndex] = city
                self.currentHeapLastIndex = self.currentHeapLastIndex + 1

        self.heapify_floyd(self.currentHeapLastIndex, 0)

    def get_root_city(self):
        """
        Return the City at the Root
        """
        # TODO: implement me! CHECK if FINISH
        ...
        return self.heapStorage[0].name

    def get_parent_index(self, index):
        """
        Return the index of the parent node.
        """
        # TODO: implement me! CHECK if FINISH
        if index > 0:
            return math.floor((index - 1) / 2)
        elif index == 0:
            return 0

    def get_left_child_index(self, index):
        """
        Return the index of the left child.
        """
        # TODO: implement me! CHECK if FINISH

        left = ((2 * index) + 1)
        try:
            self.heapStorage[left]
        except IndexError:
            return None
        return left

    def get_right_child_index(self, index):
        """
        Return the index of the right child.
        """
        # TODO: implement me! CHECK if FINISH

        right = ((2 * index) + 2)
        try:
            self.heapStorage[right]
        except IndexError:
            return None
        return right

    def has_parent(self, index) -> bool:
        """
        Check if the node has a parent. Return:

            True    = Has parent

            False   = No parent
        """
        # TODO: implement me! CHECK if FINISH
        return index > 0 and math.floor((index - 1) / 2) >= 0

        # try:
        #    par_exist = index > 0 and self.heapStorage[math.floor((index-1)/2)]
        #    print(index)
        # except IndexError:
        #    return False
        # return par_exist

    def has_left_child(self, index):
        """
        Check if the Node has a left Child. Return:

            True    = Has leftChild

            False   = No leftChild

        Hint:
        -----
        The Index of the Child can be used for this purpose.
        """
        # TODO: implement me! CHECK if FINISH

        try:
            has_child = isinstance(self.heapStorage[((2 * index) + 1)], City)
            # print("has left child: ", has_child)

        except IndexError:
            return False
        return has_child

    def has_right_child(self, index):
        """
        Check if the Node has a right Child. Return:

            True    = Has rightChild

            False   = No rightChild

        Hint:
        -----
        The Index of the Child can be used for this purpose.
        """
        # TODO: implement me! CHECK if FINISH

        try:
            has_child = isinstance(self.heapStorage[((2 * index) + 2)], City)
            # print("has right child: ", has_child)
        except IndexError:
            return False
        return has_child

    def get_city_population(self, index):
        """
        Return the Population of a City with the given index in the heap.
        """
        # TODO: implement me! CHECK if FINISH
        ...
        return self.heapStorage[index].population

    def get_parent_population(self, index):
        """
        Returns the population of the parent.

        Hint:
        -----
        We need the position of the parent in the StorageArray to extract the population from this position.
        """
        # TODO: implement me! CHECK if FINISH

        if self.has_parent(index):
            return self.heapStorage[self.get_parent_index(index)].population

    def get_left_child_population(self, index):
        """
        Return of the population of the left child.

        Hint:
        -----
        We need the position of the child in the StorageArray to extract the population from this position.
        """
        # TODO: implement me! CHECK if FINISH

        if self.has_left_child(index):
            return self.heapStorage[self.get_left_child_index(index)].population

    def get_right_child_population(self, index):
        """

        Return of the population of the right child.
        Hint:
        -----
        We need the position of the child in the StorageArray to extract the population from this position.
        """
        # TODO: implement me! CHECK if FINISH

        if self.has_right_child(index):
            return self.heapStorage[self.get_right_child_index(index)].population

    def check_if_heap_is_full(self):
        """
        Check if the heap has reached its maximum capacity. Return:

            True    = Full

            False   = Not full
        """
        # TODO: implement me! CHECK if FINISH
        ...

        return not (self.currentHeapLastIndex < len(self.heapStorage))

    def swap_nodes(self, fst_node_index, sec_node_index):
        """
        Swap two nodes specified by their index.
        """
        # TODO: implement me! CHECK if FINISH
        ...

        first = None
        if len(self.heapStorage) > fst_node_index:
            first = self.heapStorage[fst_node_index]
        second = None
        if len(self.heapStorage) > sec_node_index:
            second = self.heapStorage[sec_node_index]

        if second is not None and first is not None:
            self.heapStorage[sec_node_index] = first
            self.heapStorage[fst_node_index] = second

    def get_heap_data(self) -> List[City]:
        """
        Return the sorted List of City Objects

        return
        ------
        List[City]:
        """
        return self.heapStorage
