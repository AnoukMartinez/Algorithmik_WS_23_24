from typing import List

from CityDataManagement.City import City
from CityDataImport.CityDataImporter import CityDataImporter
from CityDataManagement.CityDataManager import CityDataManager
from CityDataManagement.ICityDataManagerAccess import ICityDataManagerAccess
from ExecutionTimeAnalyser.ExecutionTimeAnalyser import ExecutionTimeAnalyser
from Visualization.CityMaxHeapVisualizer import CityMaxHeapVisualizer


class HeapCreationAssembler:
    """
    Assembler class: bears the responsibility to build the required components and connect them to each other.
    """

    importer = CityDataImporter()
    cityDataManager: ICityDataManagerAccess = CityDataManager()
    executionTimeAnalyser = ExecutionTimeAnalyser()

    def run(self):
        # Creation of the given data structure for this course.
        city_data = self.importer.import_from_file()

        # create Max Heap and measure Execution Time Iterative
        self.executionTimeAnalyser.start()
        self.cityDataManager.create_new_max_city_heap(city_data, False, False)
        self.executionTimeAnalyser.stop("MaxHeap Execution time Iterative: ")

        # create Max Heap and measure Execution Time Recursive
        self.executionTimeAnalyser.start()
        self.cityDataManager.create_new_max_city_heap(city_data, True, False)
        self.executionTimeAnalyser.stop("MaxHeap Execution time Recursive: ")

        # create Max Heap and measure Execution Time for Floyds Algorithm
        self.executionTimeAnalyser.start()
        self.cityDataManager.create_new_max_city_heap(city_data, True, True)
        self.executionTimeAnalyser.stop("MaxHeap Execution time with Floyd's Algorithm: ")

        # Further Execution Time measurement
        self.measure_tim_sort_execution_time(city_data)
        self.measure_max_heap_execution_time_via_timeit(10)

        # Node add
        self.cityDataManager.insert_new_city_into_max_city_heap("Hobbiton", "the Shire", 80000000000)
        print("This should be removed!")

        # Node removal
        self.cityDataManager.remove_city_with_highest_population()

        # Visualisation
        data_to_visualize: List[City] = self.cityDataManager.get_max_heap_as_list()
        amount_of_nodes_to_create = 1023
        # amount_of_nodes_to_create = len(city_data) #all cities, use this for science at the price of performance ;)
        self.visualize_heap(data_to_visualize, amount_of_nodes_to_create, city_data)

    def measure_tim_sort_execution_time(self, city_data):
        """
        Measuring the execution time for sorting cities using Python's TimSort.
        """
        self.executionTimeAnalyser.start()
        unsorted_cities_list = self.cityDataManager.transform_raw_city_data_to_unsorted_list_of_cities(city_data)
        unsorted_cities_list.sort(reverse=True)
        self.executionTimeAnalyser.stop("TimSort Execution time: ")

    def measure_max_heap_execution_time_via_timeit(self, repetitions):
        """
        Alternative, more expensive (due to several repetitions) but
        also more accurate measurement of the execution time.
        """
        self.executionTimeAnalyser.measure_execution_time_via_timeit(repetitions)

    def visualize_heap(self, data_to_visualize: List[City], amount_of_nodes_to_create: int, city_data):
        """
        Triggering and building the visualisation of the heap.

        Param:
        ------
        dataToVisualize: List[City]: List of Cities

        amountOfNodesToCreate: int: the first N nodes of the dataToVisualize list to be visualized

        useUnsorted: bool:  Using unsorted Data? This is used in the case that the list representing
                            the heap is still empty.

        cityData: raw City Data.    This is used in the case that the list representing the heap is still empty.
                                    Instead, this Data will be used.

        """
        unsorted = False
        if data_to_visualize is None or data_to_visualize[0] == 0:
            data_to_visualize = self.cityDataManager.transform_raw_city_data_to_unsorted_list_of_cities(city_data)
            unsorted = True
        city_max_heap_visualizer = CityMaxHeapVisualizer()
        city_max_heap_visualizer.create_radial_tree_visualisation(amount_of_nodes_to_create, data_to_visualize,
                                                                  unsorted)


if __name__ == '__main__':
    heapAssembler = HeapCreationAssembler()
    heapAssembler.run()
