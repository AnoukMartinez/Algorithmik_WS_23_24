from abc import ABC, abstractmethod
from typing import List
from CityDataManagement.City import City
import math


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
        if self.check_if_heap_is_full():
            print("Heap is Full, Could Not Insert")
            return

        if self.recursive:
            self.heapify_up_recursive(self.currentHeapLastIndex)
        else:
            self.heapify_up_iterative()

        self.currentHeapLastIndex = self.currentHeapLastIndex + 1

    def build_heap_via_floyd(self):
        """
        Build a Heap via Floyds Heap Construction Algorithm from a unsorted List Of Cities.
        """
        for i in self.rawCityData:
            self.heapStorage.append(i)

        self.heapify_floyd(0, self.currentHeapLastIndex)


    def get_root_city(self):
        """
        Return the City at the Root
        """
        return self.heapStorage[0]

    def get_parent_index(self, index):
        """
        Return the index of the parent node. 
        """
        if index == 0:
            return None
        else:
            parent_index = (index - 1) / 2
            return math.floor(parent_index)

    def get_left_child_index(self, index):
        """
        Return the index of the left child. 
        """
        if self.has_left_child(index):
            return 2 * index + 1 
        return None

    def get_right_child_index(self, index):
        """
        Return the index of the right child. 
        """
        if self.has_right_child(index):
            return 2 * index + 2 
        return None
    


    def has_parent(self, index) -> bool:
        """
        Check if the node has a parent. Return:
            True    = Has parent
            False   = No parent
        """
        return index != 0

    def has_left_child(self, index):
        """
        Check if the Node has a left Child. Return:
            True    = Has leftChild
            False   = No leftChild
        """
        left_child_index = 2 * index + 1
        if left_child_index > self.maximumHeapCapacity:
            return False
        elif self.heapStorage[left_child_index] == 0:
            return False
        
        return True

    def has_right_child(self, index):
        """
        Check if the Node has a right Child. Return:
            True    = Has rightChild
            False   = No rightChild
        """
        right_child_index = 2 * index + 1
        if right_child_index > self.maximumHeapCapacity:
            return False
        elif self.heapStorage[right_child_index] == 0:
            return False
        
        return True

    def get_city_population(self, index):
        """
        Return the Population of a City with the given index in the heap.
        """
        if(self.heapStorage[index] == 0 or index == None):
            return None
        return self.heapStorage[index].population

    def get_parent_population(self, index):
        """
        Returns the population of the parent.
        """
        parent_index = self.get_parent_index(index)
        self.get_city_population(parent_index)

    def get_left_child_population(self, index):
        """
        Return of the population of the left child.
        """
        left_child_index = self.get_left_child_index(index)
        self.get_city_population(left_child_index)

    def get_right_child_population(self, index):
        """
        Return of the population of the right child.
        """
        right_child_index = self.get_right_child_index(index)
        self.get_city_population(right_child_index)

    def check_if_heap_is_full(self):
        """
        Check if the heap has reached its maximum capacity. Return:
            True    = Full
            False   = Not full
        """
        return self.currentHeapLastIndex >= self.maximumHeapCapacity

    def swap_nodes(self, fst_node_index, sec_node_index):
        """
        Swap two nodes specified by their index.
        """
        self.heapStorage[fst_node_index], self.heapStorage[sec_node_index] =\
        self.heapStorage[sec_node_index], self.heapStorage[fst_node_index]

    def swap_nodes(self, fst_node_index, sec_node_index):
        """
        Swap two nodes specified by their index.
        """
        first = self.heapStorage[fst_node_index]
        second = self.heapStorage[sec_node_index]

        if first != 0 and second != 0:
            self.heapStorage[sec_node_index] = first
            self.heapStorage[fst_node_index] = second
        else: print("Wasn't provided with 2 Nodes")

    def get_heap_data(self) -> List[City]:
        """
        Return the sorted List of City Objects

        return
        ------
        List[City]:
        """
        return self.heapStorage