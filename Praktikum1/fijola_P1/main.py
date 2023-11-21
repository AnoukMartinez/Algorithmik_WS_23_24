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

    print("my_dict get:", my_dict.get("eighty-four"))


# print_all(my_dict.get_all())


def direct_acc_map(filename: str):
    my_dict = DirectAccessMap()
    my_dict.put_from_csv(filename)

    print("direct_acc_map get: ", my_dict.get("eighty-four"))
    print("dict_acc_map get_key: ", my_dict.get_key("eighty-four"))
    # print_all(my_dict.get_all())


def avl(filename: str):
    my_avl = AcNg.AutocompleteNgrams(filename)
    # x.avl_tree.print_tree()
    print("my_avl: height: ", my_avl.avl_tree.height())

    # csv 1
    # print("my_avl get", my_avl.get("eighty-four"))
    # csv 2
    # print("my_avl get: ", my_avl.get("and hungry"))
    # csv 3
    # print("my_avl get: ", my_avl.get("it from attacking"))
    # csv 4
    print("my_avl get: ", my_avl.get("i quickly discovered that"))



if __name__ == '__main__':
  #  linked_dict("csv/1_gram.csv")
  #  direct_acc_map("csv/1_gram.csv")
    avl("csv/4_gram.csv")
