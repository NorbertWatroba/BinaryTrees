from BST import BST
from AVL import AVL
from os import system, name
import argparse
from time import time


def clear():
    system('cls') if name == 'nt' else system('clear')


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tree', default='AVL', help='choose tree type BST/AVL',
                    choices=['BST', 'AVL'], type=str.upper)
args = parser.parse_args()

clear()
while True:
    try:
        nums = list(map(int, input('insert> ').split()))
        break
    except ValueError:
        print('Can only insert integer values!')

if args.tree.upper() == 'AVL':
    Tree = AVL(nums)
else:
    Tree = BST(nums)

while True:
    action = input('action> ')
    clear()
    match action.strip().lower():
        case 'insert' | 'i':
            try:
                Tree.insert(list(map(int, input('values> ').split())))
            except ValueError:
                print('Can only insert integer numbers!')
        case 'remove' | 'r':
            try:
                values = map(int, input('delete> ').split())
                Tree.remove_values(values)
            except ValueError:
                print('Can only delete integer numbers!')
        case 'delete' | 'd':
            Tree.delete()
        case 'rebalance' | 'reb':
            Tree.rebalance()
        case 'print' | 'p':
            Tree.print()
        case 'show' | 's':
            print(Tree)
        case 'minmax' | 'm':
            Tree.find_min_max()
        case 'export' | 'e':
            path = input('(optional) file name>')
            if path:
                with open(path, 'w') as file:
                    print(Tree.export(), file=file)
            else:
                print(Tree.export())
        case 'exit' | 'q':
            break
        case 'help' | 'h':
            print('''
+==============================================================================+
|  Help        |  h  |   Show this message                                     |
|  Print       |  p  |   Print the tree usin In-order, Pre-order, Post-order   |
|  Show        |  s  |   Tree representation in terminal                       |
|  MinMax      |  m  |   Find minimum and maximum values                       |
|  Insert      |  i  |   Add new elements to the tree                          |
|  Remove      |  r  |   Remove elements of the tree                           |
|  Delete      |  d  |   Delete whole tree                                     |
|  Rebalance   | reb |   Rebalance the tree                                    |
|  Export      |  e  |   Export the tree to tickzpicture (file or text)        |
|  Exit        |  q  |   Exits the program (same as ctrl+D)                    |
+==============================================================================+
''')
        case _:
            print('command not found!\nType help to see the manual')
