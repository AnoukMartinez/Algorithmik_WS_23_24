import time

from Praktikum1.daniel.AVLTree import AVLTree


def get_suggestions_from_csv_withTime(csv_file, prefix, k):
    avl_tree = AVLTree()
    timeInsert = avl_tree.insert_csv_data_TIME(csv_file)

    print(f'Time needed insert CSV > {timeInsert}')

    suggestions, nodes_searched, time_needed = avl_tree.get_k_possible_suggestions_TIME(prefix, k)

    print(f'Top {k} words/phrases starting with "{prefix}":')
    for word, count in suggestions:
        print(f'{word}: {count} times')

    print(f'Number of nodes searched: {nodes_searched}')
    print(f'Time needed: {time_needed}')


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


# CSV - 1
#get_suggestions_from_csv('csv/1_gram.csv', 'eighty', 3)
#get_suggestions_from_csv_withTime('csv/1_gram.csv', 'eighty', 3)
#get_from_csv('csv/1_gram.csv', 'eighty')

#get_suggestions_from_csv('csv/1_gram.csv', 'tom', 200)
#get_suggestions_from_csv_withTime('csv/1_gram.csv', 'tom', 200)
#get_from_csv('csv/1_gram.csv', 'tom')

get_suggestions_from_csv('csv/4_gram.csv', 'no', 66000)
get_suggestions_from_csv_withTime('csv/4_gram.csv', 'no', 66000)
get_from_csv('csv/4_gram.csv', 'no')

# CSV - 2
# get_suggestions_from_csv_withTime('../csv/2_gram.csv', 'physi', 3)
# get_from_csv('../csv/2_gram.csv','physique is')

# CSV - 3
# get_suggestions_from_csv('csv/3_gram.csv', 'i have a', 3)
# get_from_csv('csv/3_gram.csv','i have a')

# CSV - 4
# get_suggestions_from_csv('csv/4_gram.csv', 'no wa', 4)
# get_from_csv('csv/4_gram.csv','i have a q')