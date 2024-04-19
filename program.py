from BST import BST

nums = list(map(int, input('insert> ').split()))
Tree = BST(nums)
while True:
    action = input('action> ')
    match action.strip().lower():
        case 'insert':
            try:
                Tree.insert(list(map(int, input('values> ').split())))
            except ValueError:
                print('Can only insert numbers!')
        case 'delete':
            try:
                values = map(int, input('delete> ').split())
                Tree.delete_values(values)
            except ValueError:
                print('Can only delete numbers!')
        case 'print':
            Tree.print()
        case 'str':
            print(Tree)
        case 'min/max':
            Tree.find_min_max()
        case 'quit':
            break
        case 'help':
            print('help massage')
