from AutocompleteNgrams import AutocompleteNgrams
from AVLTree import AVLTree


def main():
    print("loading...")
    tree = AutocompleteNgrams('1_gram.csv')

    tree.read_csv_file("1_gram.csv")
    print(tree.get("home"))
    print(tree.get("ldkfjgkjl"))

    suggestions, searched_nodes = tree.get_k_possible_suggestions("am", 10)
    print(suggestions)
    print(searched_nodes)

    # most_likely = tree.get_most_likely_ngrams("fre")
    # print(most_likely)


if __name__ == '__main__':
    main()
