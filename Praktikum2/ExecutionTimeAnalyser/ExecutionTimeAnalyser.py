import time
import timeit


class ExecutionTimeAnalyser:
    """
    Class with the responsibility to offer a time measurement in milliseconds.
    """

    startTime = 0
    endTime = 0
    elapsed_time_ms = 0

    def start(self):
        """
        Begin time measurement.
        """
        self.startTime = time.time()

    def stop(self, message=""):
        """
        Stop time measurement and trigger calculation and print to console.
        """
        self.endTime = time.time()
        self._calculate_elapsed_time_in_ms()
        self._print_elapsed_time_to_console(message)

    def _calculate_elapsed_time_in_ms(self):
        """
        Calculate measured time in milliseconds.
        """
        self.elapsed_time_ms = (self.endTime - self.startTime) * 1000

    def _print_elapsed_time_to_console(self, message):
        """
        Print Data to console.
        """
        print(message, self.elapsed_time_ms, " milliseconds")

    def measure_execution_time_via_timeit(self, repetitions):
        """
        Alternative, more expensive (due to several repetitions) but also more accurate measurement of the execution time.
        """

        setup_code = """
from math import factorial
from CityDataImport.CityDataImporter import CityDataImporter 
from CityDataManagement.CityDataManager import CityDataManager
        """

        statement = """
importer = CityDataImporter()
city_manager = CityDataManager()
city_data = importer.import_from_file()
city_manager.create_new_max_city_heap(city_data, False, True)"""

        execution_time = timeit.timeit(setup=setup_code, stmt=statement, number=repetitions)
        print("Timeit MaxHeap Execution time via Floyd's: ", execution_time / repetitions * 1000, " milliseconds")
