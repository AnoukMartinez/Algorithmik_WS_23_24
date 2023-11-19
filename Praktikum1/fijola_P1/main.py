import AutocompleteNgrams as AcNg
import AVLTree as ATree
from LinkedDictionary import LinkedDictionary
from DirectAccessMap import DirectAccessMap


def print_all(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")


def linked_dict(filename: str):
    my_dict = LinkedDictionary()
    my_dict.put_from_csv(filename)

    print(my_dict.get("eighty-four"))


# print_all(my_dict.get_all())


def direct_acc_map(filename: str):
    my_dict = DirectAccessMap()
    my_dict.put_from_csv(filename)

    #  print(my_dict.get("eighty-four"))
    print(my_dict.get_key("eighty-four"))
    # print_all(my_dict.get_all())


if __name__ == '__main__':
    linked_dict("csv/1_gram.csv")
    direct_acc_map("csv/1_gram.csv")
