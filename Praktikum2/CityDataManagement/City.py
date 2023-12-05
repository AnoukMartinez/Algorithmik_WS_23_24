class City:
    """
    Class with the responsibility to represent a city.

    Param:
    name: Name of the City
    country: Country of the City
    population: Population of the City
    """
    name = "No data available"
    country = "No data available"
    population = "No data available"

    def __init__(self, name, country, population):
        self.name = name
        self.country = country
        self.population = int(population)

    def __str__(self):
        return "City " + self.name + " in country " + self.country + " with a population of " + str(
            self.population) + "."

    def __gt__(self, city2):
        return self.population > city2.population

    def __lt__(self, city2):
        return self.population < city2.population
