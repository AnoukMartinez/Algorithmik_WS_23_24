from typing import List
from CityDataManagement.City import City
from CityDataManagement.CityMaxHeap import CityMaxHeap
from CityDataManagement.ICityDataManagerAccess import ICityDataManagerAccess


class CityDataManager(ICityDataManagerAccess):
    """
    Class with the responsibility to manage the unsorted and sorted data of the cities.


    """

    cityMaxHeap: CityMaxHeap = None
    cityData: List[City]

    def create_new_max_city_heap(self, city_data: List[City], recursive: bool, floyd: bool):
        self.cityData: List[City] = city_data
        unsorted_cities_list = self._convert_raw_city_data_to_city_list(city_data)
        self.cityMaxHeap = self._create_city_max_heap(unsorted_cities_list, recursive, floyd)

    def insert_new_city_into_max_city_heap(self, name, country, population):
        if self.cityMaxHeap is not None:
            new_city = City(name, country, population)
            self.cityMaxHeap.insert(new_city)
            print("City of " + name + " with a population of " + str(
                population) + " in the country of " + country + " has been created.")
        else:
            print("No Data Available")

    def delete_max_city_heap(self):
        self.cityMaxHeap = None

    def get_highest_population_city(self):
        if self.cityMaxHeap is not None:
            return self.cityMaxHeap.get_root_city()
        else:
            print("No Data Available")

    def remove_city_with_highest_population(self):
        if self.cityMaxHeap is not None:
            removed_city = self.cityMaxHeap.remove()
            if removed_city is not None:
                print("City of "
                      + removed_city.name
                      + " with the highest population of "
                      + str(removed_city.population)
                      + " has been removed.")
        else:
            print("No Data Available")

    def transform_raw_city_data_to_unsorted_list_of_cities(self, city_data):
        return self._convert_raw_city_data_to_city_list(city_data)

    def get_max_heap_as_list(self) -> List[City]:

        if self.cityMaxHeap is not None and len(self.cityMaxHeap.get_heap_data()) > 1:
            return self.cityMaxHeap.get_heap_data()

    # ------Private Methods

    def _convert_raw_city_data_to_city_list(self, city_data):
        """
        Convert raw City Data into a Unsorted List of City Objects.
        """
        unsorted_cities_list: List[City] = []
        for cityEntry in city_data:
            try:
                new_city = City(cityEntry[0], cityEntry[1], cityEntry[2])
                self._add_city_to_unsorted_cities(new_city, unsorted_cities_list)
            except IndexError:
                # Index Out Of Bound
                print("Entry does not exist in City Data. Structure should be: Name / Country / Population")
        return unsorted_cities_list

    def _add_city_to_unsorted_cities(self, new_city, unsorted_cities_list):
        """
        Add a city to the Dictonary of unsorted cities.

        Key = Name of the city
        Value = City Object
        """
        unsorted_cities_list.append(new_city)

    def _create_city_max_heap(self, unsorted_cities_list: List[City], recursive: bool, floyd: bool):
        """
        Create a new City Max Heap based on the given List of City Objects
        """
        return CityMaxHeap(unsorted_cities_list, recursive, floyd)
