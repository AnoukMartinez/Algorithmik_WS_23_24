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
        '''
        index: falls das ganze rekursiv implementiert wird (Ich habs iterativ gemacht weil es 
        generell keine Vorgabe dazu gibt)
        amount of cities: gleich maxHeapIndex, brauchen wir weil wir ja hinten anfangen wollen

        Ungefähr:
        i = maxHeapIndex # Hinten anfangen
        while i < 0:
            # Percolatedown = check node values, then swap if necessary
            currentnode = heapStorage[i]
            parentnode = heapStorage[currentnode.getparentindex]

            if currentnode.population > parentnode.population:
                swap(currentnode, parentnode)
            
            i -= 1
        '''

    def heapify_down_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative downwards.
        """
        root_node = self.heapStorage[0]
        last_node = self.heapStorage[self.currentHeapLastIndex]

        # Tausche erste und letzte Node
        self.swap_nodes(root_node, last_node)
        self.heapStorage[self.currentHeapLastIndex] = 0

        root_node = last_node # Setze Referenz von root Node auf new root
        
        while self.has_left_child(root_node) or self.has_right_child(root_node):
            if self.has_left_child(root_node):
                left_child = self.get_left_child_index(root_node)
            if self.has_right_child(root_node):
                right_child = self.get_right_child_index(root_node)

            smaller_child = 0 # Instanziiere smallerchild (KA ob man das braucht aber paranoia)

            if left_child.population < right_child.population:
                smaller_child = right_child
            else:
                smaller_child = left_child
            
            if root_node.population > smaller_child:
                return # Heap Invariante ist wieder hergestellt
            
            root_node = smaller_child
            

    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        if index == 0: # Alternativ if self.has_parent(index) oder so
            root_node = self.heapStorage[index]
            last_node = self.heapStorage[self.currentHeapLastIndex]

            self.swap_nodes(root_node, last_node) # Tausche erste und letzte Node
            self.heapStorage[self.currentHeapLastIndex] = 0 # Lösche letzten Eintrag
        
        if self.has_left_child(index):
            left_child_index = self.get_left_child_index(index)
        if self.has_right_child(index):
            right_child_index = self.get_right_child_index(index)

        smaller_child_index = None # Instanziiere smallerchild (KA ob man das braucht aber paranoia)
        if left_child_index.population < right_child_index.population:
            smaller_child_index = right_child_index
        else:
            smaller_child_index = left_child_index
        
        if root_node.population > smaller_child_index:
            return # Heap Invariante ist wieder hergestellt. Base Case...?
        else:
            self.swap_nodes(index, smaller_child_index)
            self.heapify_down_recursive(smaller_child_index)
        

    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        # Die "City" in Frage die hier removed wird ist übrigens immer die root node.
        if self.recursive:
            self.heapify_down_recursive(self.heapStorage[0])
        else:
            self.heapify_down_iterative()