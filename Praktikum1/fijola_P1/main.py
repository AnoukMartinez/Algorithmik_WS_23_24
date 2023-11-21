import AutocompleteNgrams as AcNg
import AVLTree as ATree
from LinkedDictionary import LinkedDictionary
from DirectAccessMap import DirectAccessMap


def print_all(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")


def linked_dict(filename: str, csv_no: str):
    my_linked_dict = LinkedDictionary()
    my_linked_dict.put_from_csv(filename)

    if csv_no == 'csv01':
        # CSV1
        print("BLOCK CSV01")
        print("my_linked_dict get: ", my_linked_dict.get("eighty-four"))
        print("my_linked_dict get_key: ", my_linked_dict.get_key("eighty-four"))
    elif csv_no == 'csv02':
        # CSV2
        print("BLOCK CSV02")
        print("my_linked_dict get: ", my_linked_dict.get("and hungry"))
        print("my_linked_dict get_key: ", my_linked_dict.get_key("and hungry"))
    elif csv_no == 'csv03':
        # CSV3
        print("BLOCK CSV03")
        print("my_linked_dict get: ", my_linked_dict.get("it from attacking"))
        print("my_linked_dict get_key: ", my_linked_dict.get_key("it from attacking"))
    elif csv_no == 'csv04':
        # CSV4
        print("BLOCK CSV04")
        print("my_linked_dict get: ", my_linked_dict.get("i quickly discovered that"))
        print("my_linked_dict get_key: ", my_linked_dict.get_key("i quickly discovered that"))

    # print("my_linked_dict get:", my_linked_dict.get("eighty-four"))


# print_all(my_linked_dict.get_all())


def direct_acc_map(filename: str, csv_no: str):
    my_direct_acc_map = DirectAccessMap()
    my_direct_acc_map.put_from_csv(filename)

    if csv_no == 'csv01':
        # CSV1
        print("BLOCK CSV01")
        print("my_direct_acc_map get: ", my_direct_acc_map.get("eighty-four"))
        print("my_dict_acc_map get_key: ", my_direct_acc_map.get_key("eighty-four"))
    elif csv_no == 'csv02':
        # CSV2
        print("BLOCK CSV02")
        print("my_direct_acc_map get: ", my_direct_acc_map.get("and hungry"))
        print("my_direct_acc_map get_key: ", my_direct_acc_map.get_key("and hungry"))
    elif csv_no == 'csv03':
        # CSV3
        print("BLOCK CSV03")
        print("my_direct_acc_map get: ", my_direct_acc_map.get("it from attacking"))
        print("my_direct_acc_map get_key: ", my_direct_acc_map.get_key("it from attacking"))
    elif csv_no == 'csv04':
        # CSV4
        print("BLOCK CSV04")
        print("my_direct_acc_map get: ", my_direct_acc_map.get("i quickly discovered that"))
        print("my_direct_acc_map get_key: ", my_direct_acc_map.get_key("i quickly discovered that"))

    # print_all(my_direct_acc_map.get_all())


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
    # print("my_avl get: ", my_avl.get("i quickly discovered that"))


def avl_suggest(filename: str):
    my_avl = AcNg.AutocompleteNgrams(filename)
    print("my_avl: height: ", my_avl.avl_tree.height())


if __name__ == '__main__':
    linked_dict("csv/1_gram.csv", "csv01")
    linked_dict("csv/2_gram.csv", "csv02")
    linked_dict("csv/3_gram.csv", "csv03")
    linked_dict("csv/4_gram.csv", "csv04")

    direct_acc_map("csv/1_gram.csv", "csv01")
    direct_acc_map("csv/2_gram.csv", "csv02")
    direct_acc_map("csv/3_gram.csv", "csv03")
    direct_acc_map("csv/4_gram.csv", "csv04")

    #  avl("csv/1_gram.csv")
    # avl_suggest("csv/1_gram.csv")
