import os as os


class CityDataImporter:
    """
    Class with the responsibility to read the data of the cities from a given tsv file inside the Project.

    Simple Way to Read TSV Files in Python using split even more easy would be to use panda
    but for the purpose of this lecture we try to minimize the amount of external imports.
    """

    def get_path_to_file(self):
        """
        Path to the file to be read based on the local location of this project.
        """
        # Project Location
        project_dir = os.path.dirname(os.path.realpath('__file__'))
        # Modul Location
        module_name = "CityDataImport"
        # Name of File
        file_name = "cities.tsv"
        path_to_file = os.path.join(project_dir, module_name, file_name)

        return path_to_file

    def import_from_file(self):
        """
        Importing the data from the TSV file based on the passed location in the file system
        """
        data_list = []

        # open .tsv file
        with open(self.get_path_to_file(), encoding="utf-8") as f:
            # Read data line by line
            for line in f:
                # split data by tab and store it in list
                l = line.split('\t')
                # remove '\n'
                cleaned_line = [i.strip('\n') for i in l]

                # append list to ans
                data_list.append(cleaned_line)

        return data_list
