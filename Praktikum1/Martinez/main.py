from LibraryHash import LibraryHash
from LinkedHash import LinkedHashTable
from AutoComplete_WordWeigh import AutocompleteNgrams


def linked_hash():
    print("====== Start linkedHash =======")
    linkedHash = LinkedHashTable()
    linkedHash.read_csv_file("1_gram.csv")
    print(linkedHash.get("dimwit"))
    print(linkedHash.get("midwit"))


def library_hash():
    print("======== Start libraryHash =========")
    libraryHash = LibraryHash()
    libraryHash.read_csv_file("1_gram.csv")
    print(libraryHash.get("dimwit"))
    print(libraryHash.get("midwit"))


def autocomplete():
    print("======== Start autocomplete =========")
    autocomplete = AutocompleteNgrams()
    autocomplete.read_csv_file("../csv/1_gram.csv")
    print(autocomplete.get("dimwit"))
    print(autocomplete.get("midwit"))

    suggestions, searched_nodes = autocomplete.get_k_possible_suggestions("tom", 10)
    print(suggestions)
    print(searched_nodes)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # linked_hash()
    # library_hash()
    autocomplete()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
