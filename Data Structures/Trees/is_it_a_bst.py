from binarytree import bst, tree, pprint


def in_order(node):
    if node.left:
        for x in in_order(node.left):
            yield x
    yield node.value
    if node.right:
        for x in in_order(node.right):
            yield x


def check_binary_search_tree_(root):
    traversed_tree = list(in_order(root))
    for i in range(1, len(traversed_tree)):
        if traversed_tree[i] <= traversed_tree[i - 1]:
            return False
    return True


if __name__ == '__main__':
    print('\n--- TREE ---')
    my_tree = tree(height=3, balanced=True)
    pprint(my_tree)
    print('In order: ', list(in_order(my_tree)))
    print('Is it a bst? : {}'.format(check_binary_search_tree_(my_tree)))

    print('\n--- BST ---')
    my_bst = bst(height=3)
    pprint(my_bst)
    print('In order: ', list(in_order(my_bst)))
    print('Is it a bst? : {}'.format(check_binary_search_tree_(my_bst)))
