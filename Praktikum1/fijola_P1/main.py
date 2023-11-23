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
        print("==========================================")
        print("==========================================")
        print("my_linked_dict get: ", my_linked_dict.get("eighty-four"))
        print("==========================================")
        print("my_linked_dict get_key: ", my_linked_dict.get_key("eighty-four"))
        print("==========================================")
    elif csv_no == 'csv02':
        # CSV2
        print("BLOCK CSV02")
        print("==========================================")
        print("==========================================")
        print("my_linked_dict get: ", my_linked_dict.get("and hungry"))
        print("==========================================")
        print("my_linked_dict get_key: ", my_linked_dict.get_key("and hungry"))
        print("==========================================")
    elif csv_no == 'csv03':
        # CSV3
        print("BLOCK CSV03")
        print("==========================================")
        print("==========================================")
        print("my_linked_dict get: ", my_linked_dict.get("it from attacking"))
        print("==========================================")
        print("my_linked_dict get_key: ", my_linked_dict.get_key("it from attacking"))
        print("==========================================")
    elif csv_no == 'csv04':
        # CSV4
        print("BLOCK CSV04")
        print("==========================================")
        print("==========================================")
        print("my_linked_dict get: ", my_linked_dict.get("i quickly discovered that"))
        print("==========================================")
        print("my_linked_dict get_key: ", my_linked_dict.get_key("i quickly discovered that"))
        print("==========================================")

    # print("my_linked_dict get:", my_linked_dict.get("eighty-four"))


# print_all(my_linked_dict.get_all())


def direct_acc_map(filename: str, csv_no: str):
    my_direct_acc_map = DirectAccessMap()
    my_direct_acc_map.put_from_csv(filename)

    if csv_no == 'csv01':
        # CSV1
        print("BLOCK CSV01")
        print("==========================================")
        print("==========================================")
        print("my_direct_acc_map get: ", my_direct_acc_map.get("eighty-four"))
        print("==========================================")
        print("my_dict_acc_map get_key: ", my_direct_acc_map.get_key("eighty-four"))
        print("==========================================")
    elif csv_no == 'csv02':
        # CSV2
        print("BLOCK CSV02")
        print("==========================================")
        print("==========================================")
        print("my_direct_acc_map get: ", my_direct_acc_map.get("and hungry"))
        print("==========================================")
        print("my_direct_acc_map get_key: ", my_direct_acc_map.get_key("and hungry"))
        print("==========================================")
    elif csv_no == 'csv03':
        # CSV3
        print("BLOCK CSV03")
        print("==========================================")
        print("==========================================")
        print("my_direct_acc_map get: ", my_direct_acc_map.get("it from attacking"))
        print("==========================================")
        print("my_direct_acc_map get_key: ", my_direct_acc_map.get_key("it from attacking"))
        print("==========================================")
    elif csv_no == 'csv04':
        # CSV4
        print("BLOCK CSV04")
        print("==========================================")
        print("==========================================")
        print("my_direct_acc_map get: ", my_direct_acc_map.get("i quickly discovered that"))
        print("==========================================")
        print("my_direct_acc_map get_key: ", my_direct_acc_map.get_key("i quickly discovered that"))
        print("==========================================")

    # print_all(my_direct_acc_map.get_all())


def avl(filename: str, csv_no: str):
    my_avl = AcNg.AutocompleteNgrams(filename)

    if csv_no == 'csv01':
        # CSV1
        print("BLOCK CSV01")
        print("==========================================")
        print("==========================================")
        print("my_avl: height: ", my_avl.avl_tree.height())
        print("==========================================")
        print("my_avl get: ", my_avl.get("eighty-four"))
        print("==========================================")
        # print("my_avl: get height: ", my_avl.avl_tree.get_height(my_avl.avl_tree.root))
    elif csv_no == 'csv02':
        # CSV2
        print("BLOCK CSV02")
        print("==========================================")
        print("==========================================")
        print("my_avl: height: ", my_avl.avl_tree.height())
        print("==========================================")
        print("my_avl get: ", my_avl.get("and hungry"))
        print("==========================================")
    elif csv_no == 'csv03':
        # CSV3
        print("BLOCK CSV03")
        print("==========================================")
        print("==========================================")
        print("my_avl: height: ", my_avl.avl_tree.height())
        print("==========================================")
        print("my_avl get: ", my_avl.get("it from attacking"))
        print("==========================================")
    elif csv_no == 'csv04':
        # CSV4
        print("BLOCK CSV04")
        print("==========================================")
        print("==========================================")
        print("my_avl: height: ", my_avl.avl_tree.height())
        print("==========================================")
        print("my_avl get: ", my_avl.get("i quickly discovered that"))
        print("==========================================")

    # my_avl.avl_tree.print_tree()


def avl_suggest(filename: str, csv_no: str):
    my_avl_suggest = AcNg.AutocompleteNgrams(filename)

    if csv_no == 'csv01':
        # CSV1
        print("BLOCK CSV01")
        print("==========================================")
        print("==========================================")
        print("my_avl_suggest: height: ", my_avl_suggest.avl_tree.height())
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("ei", 1))
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("ei", 2))
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("ei", 3))
        print("=================get_k_possible_suggestions_alphabetical_asc=========================")
        print("my_avl_suggest get_k_possible_suggestions_alphabetical_asc: ",
              my_avl_suggest.get_k_possible_suggestions_alphabetical_asc("ei", 3))
        print("=================get_k_possible_suggestions_alphabetical_desc=========================")
        print("my_avl_suggest get_k_possible_suggestions_alphabetical_desc: ",
              my_avl_suggest.get_k_possible_suggestions_alphabetical_desc("ei", 3))
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("ei", 5))
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("eigh", 1))
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("eighty", 1))
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("eighty", 3))
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("rog", 1))
        print("==========================================")
    elif csv_no == 'csv02':
        # CSV2
        print("BLOCK CSV02")
        print("==========================================")
        print("==========================================")
        print("my_avl_suggest: height: ", my_avl_suggest.avl_tree.height())
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("and hu", 1))
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("and hu", 5))
        print("=================get_k_possible_suggestions_alphabetical_asc=========================")
        print("my_avl_suggest get_k_possible_suggestions_alphabetical_asc: ",
              my_avl_suggest.get_k_possible_suggestions_alphabetical_asc("and hu", 1))
        print("=================get_k_possible_suggestions_alphabetical_desc=========================")
        print("my_avl_suggest get_k_possible_suggestions_alphabetical_desc: ",
              my_avl_suggest.get_k_possible_suggestions_alphabetical_desc("and hu", 5))
    elif csv_no == 'csv03':
        # CSV3
        print("BLOCK CSV03")
        print("==========================================")
        print("==========================================")
        print("my_avl_suggest: height: ", my_avl_suggest.avl_tree.height())
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("it from", 1))
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("it from", 3))
        print("=================get_k_possible_suggestions_alphabetical_asc=========================")
        print("my_avl_suggest get_k_possible_suggestions_alphabetical_asc: ",
              my_avl_suggest.get_k_possible_suggestions_alphabetical_asc("it from", 3))
        print("=================get_k_possible_suggestions_alphabetical_desc=========================")
        print("my_avl_suggest get_k_possible_suggestions_alphabetical_desc: ",
              my_avl_suggest.get_k_possible_suggestions_alphabetical_desc("it from", 3))
    elif csv_no == 'csv04':
        # CSV4
        print("BLOCK CSV04")
        print("==========================================")
        print("==========================================")
        print("my_avl_suggest: height: ", my_avl_suggest.avl_tree.height())
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("i quic", 1))
        print("==========================================")
        print("my_avl_suggest get_k_possible_suggestions: ", my_avl_suggest.get_k_possible_suggestions("i quic", 4))
        print("=================get_k_possible_suggestions_alphabetical_asc=========================")
        print("my_avl_suggest get_k_possible_suggestions_alphabetical_asc: ",
              my_avl_suggest.get_k_possible_suggestions_alphabetical_asc("i quic", 4))
        print("=================get_k_possible_suggestions_alphabetical_desc=========================")
        print("my_avl_suggest get_k_possible_suggestions_alphabetical_desc: ",
              my_avl_suggest.get_k_possible_suggestions_alphabetical_desc("i quic", 4))


if __name__ == '__main__':
    linked_dict("csv/1_gram.csv", "csv01")
    linked_dict("csv/2_gram.csv", "csv02")
    linked_dict("csv/3_gram.csv", "csv03")
    linked_dict("csv/4_gram.csv", "csv04")

    direct_acc_map("csv/1_gram.csv", "csv01")
    direct_acc_map("csv/2_gram.csv", "csv02")
    direct_acc_map("csv/3_gram.csv", "csv03")
    direct_acc_map("csv/4_gram.csv", "csv04")

    avl("csv/1_gram.csv", "csv01")
    avl("csv/2_gram.csv", "csv02")
    avl("csv/3_gram.csv", "csv03")
    avl("csv/4_gram.csv", "csv04")

    avl_suggest("csv/1_gram.csv", "csv01")
    avl_suggest("csv/2_gram.csv", "csv02")
    avl_suggest("csv/3_gram.csv", "csv03")
    avl_suggest("csv/4_gram.csv", "csv04")
