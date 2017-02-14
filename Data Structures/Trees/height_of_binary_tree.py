from binarytree import bst, tree, pprint


def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1


if __name__ == '__main__':
    my_tree = tree(height=3)
    pprint(my_tree)
    print('Height is: {}\n'.format(height(my_tree)))

    my_bst = bst()
    pprint(my_bst)
    print('Height is {}\n'.format(height(my_bst)))
