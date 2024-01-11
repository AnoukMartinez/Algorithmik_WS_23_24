from abc import ABC, abstractmethod
from typing import List
from CityDataManagement.City import City


class ICityDataManagerAccess(ABC):
    """
    Interface with the responsibility to offer CRUD operations to a City Heap.
    """

    @abstractmethod
    def create_new_max_city_heap(self, city_data: List[City], recursive: bool, floyd: bool):
        """
        Creation of a Max-City-Heap.

        Info: This is part of the exercise.

        Param:
        ------
        cityData:    A unsorted List of Cities

        recursive:    Should the heapify be recursive? False = use the iterative approach; True = Recursiv approach
        
        floyd:       Should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.
                            For removal the approach specified in :param recursiv will be used.
        """
        pass

    @abstractmethod
    def get_max_heap_as_list(self) -> List[City]:
        """
        Return the maxHeap as a List of Cities. If the heap is empty, return the unsorted Data.

        Info: This is part of the exercise.
        """
        pass

    @abstractmethod
    def insert_new_city_into_max_city_heap(self, name, country, population):
        """
        Insertion of a new City into the Max-City-Heap.
        """
        pass

    @abstractmethod
    def delete_max_city_heap(self):
        """
        Removal of the Max-City-Heap.
        """
        pass

    @abstractmethod
    def get_highest_population_city(self):
        """
        Return the City with the highest Population.

        Info: This is part of the exercise.
        """
        pass

    @abstractmethod
    def remove_city_with_highest_population(self):
        """
        Removal of the City with the highest Population.

        Info: This is part of the exercise.
        """
        pass

    @abstractmethod
    def transform_raw_city_data_to_unsorted_list_of_cities(self, city_data):
        """
        Transformation of the raw city data to a unsorted List of Cities without heap sort.

        Hint:
        ------
        This method is for educational purposes only and should only be used for timing and visualization of unsorted data.
        """
        pass
