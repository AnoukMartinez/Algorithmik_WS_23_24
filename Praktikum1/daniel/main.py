import time

from Algorithmik_WS_23_24.Praktikum1.AVLTree import AVLTree


def get_suggestions_from_csv(csv_file, prefix, k):
    avl_tree = AVLTree()
    avl_tree.insert_csv_data(csv_file)

    suggestions, nodes_searched = avl_tree.get_k_possible_suggestions(prefix, k)

    print(f'Top {k} words/phrases starting with "{prefix}":')
    for word, count in suggestions:
        print(f'{word}: {count} times')

    print(f'Number of nodes searched: {nodes_searched}')

def get_from_csv(csv_file, word_to_search):
    avl_tree = AVLTree()
    avl_tree.insert_csv_data(csv_file)

    word_return = avl_tree.get(word_to_search)

    if word_return is not None:
        print(f'The word "{word_to_search}" is in the dataset')
    else:
        print(f'The word "{word_to_search}" is not in the dataset.')

#CSV - 1
get_suggestions_from_csv('csv/1_gram.csv', 'eighty', 3)
#get_from_csv('csv/1_gram.csv','eighty')

#CSV - 2
#et_suggestions_from_csv('csv/2_gram.csv', 'physi', 3)
#get_from_csv('csv/2_gram.csv','physique is')

#CSV - 3
#get_suggestions_from_csv('csv/3_gram.csv', 'i have a', 3)
#get_from_csv('csv/3_gram.csv','i have a')

#CSV - 4
#get_suggestions_from_csv('csv/4_gram.csv', 'no wa', 4)
#get_from_csv('csv/4_gram.csv','i have a q')