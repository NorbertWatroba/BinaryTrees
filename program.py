from BST import BST
from os import system, name
import argparse


def clear():
    system('cls') if name == 'nt' else system('clear')


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tree', default='BST', help='choose tree type BST/AVL',
                    choices=['BST', 'AVL'], type=str.upper)
args = parser.parse_args()

nums = list(map(int, input('insert> ').split()))

if args.tree.upper() == 'AVL':
    print('AVL available soon')
    Tree = BST(nums)
    # Tree = AVL(nums)
else:
    Tree = BST(nums)
clear()
while True:
    action = input('action> ')
    clear()
    match action.strip().lower():
        case 'insert':
            try:
                Tree.insert(list(map(int, input('values> ').split())))
            except ValueError:
                print('Can only insert integer numbers!')
        case 'remove':
            try:
                values = map(int, input('delete> ').split())
                Tree.delete_values(values)
            except ValueError:
                print('Can only delete integer numbers!')
        case 'delete':
            Tree.delete()
        case 'rebalance':
            print('Broken:(')
            # Tree.rebalance() TODO
        case 'print':
            Tree.print()
        case 'show':
            print(Tree)
        case 'minmax':
            Tree.find_min_max()
        case 'export':
            path = input('(optional) file name>')
            if path:
                with open(path, 'w') as file:
                    print(Tree.export(), file=file)
            else:
                print(Tree.export())
        case 'exit':
            break
        case 'help':
            print('''
+========================================================================+
|  Help        |   Show this message                                     |
|  Print       |   Print the tree usin In-order, Pre-order, Post-order   |
|  Show        |   Tree representation in terminal                       |
|  MinMax      |   Find minimum and maximum values                       |
|  Insert      |   Add new elements to the tree                          |
|  Remove      |   Remove elements of the tree                           |
|  Delete      |   Delete whole tree                                     |
|  Rebalance   |   Rebalance the tree                                    |
|  Export      |   Export the tree to tickzpicture (file or text)        |
|  Exit        |   Exits the program (same as ctrl+D)                    |
+========================================================================+
''')
        case _:
            print('command not found!\nType help to see the manual')
