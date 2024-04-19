from BST_Node import Node


class BST:
    def __init__(self, numbers: list[int]):
        self.root = None
        self.insert(numbers)

    # Funkcja ze Stacka
    def __str__(self):
        def inner(node):
            if node is None:
                return []
            sdat = str(node.value)
            l, r = inner(node.left), inner(node.right)
            cl, cr = len((l or ('',))[0]), len((r or ('',))[0])
            s = max(cl, cr)
            sll, slr = (s - cl + 1) // 2, (s - cl) // 2
            srl, srr = (s - cr) // 2, (s - cr + 1) // 2
            v = [' ' * s + sdat + ' ' * s]
            v.extend([' ' * (s - i - 1) + '/' + ' ' * i + ' ' * len(sdat) +
                      ' ' * i + '\\' + ' ' * (s - i - 1) for i in range(s // 2)])
            v.extend([(' ' * sll + l[i] + ' ' * slr if i < len(l) else ' ' * s) +
                      ' ' * len(sdat) + (' ' * srl + r[i] + ' ' * srr if i < len(r) else ' ' * s)
                      for i in range(max(len(l), len(r)))])
            return v

        return '\n'.join(inner(self.root))

    def insert(self, values: list[int]):
        if self.root is None:
            self.root = Node(values.pop(0))
        for value in values:
            self._insert(value, self.root)

    def _insert(self, value: int, current_node: Node):
        if value < current_node.value:

            if current_node.left is None:
                current_node.left = Node(value, current_node)
            else:
                self._insert(value, current_node.left)

        elif value > current_node.value:

            if current_node.right is None:
                current_node.right = Node(value, current_node)
            else:
                self._insert(value, current_node.right)

        else:
            print(f"Value of {value} already exists in the tree!")

    def delete_values(self, values: list[int] | map):
        for value in values:
            self._delete_node(self.find(int(value)))

    def _delete_node(self, node: Node):
        def number_of_children(n: Node):
            child_num = 0
            if n.right is not None:
                child_num += 1
            if n.left is not None:
                child_num += 1
            return child_num

        if node is None:
            print('Node not found in the tree!')
            return

        parent_node: Node = node.parent
        num_of_children = number_of_children(node)

        # Breaking code into 3 cases based on number of children

        if num_of_children == 0:

            if parent_node is not None:  # checking for root deletion
                if parent_node.left == node:
                    parent_node.left = None
                else:
                    parent_node.right = None
            else:
                self.root = None

        if num_of_children == 1:

            # picking child node
            if node.left is not None:
                child_node = node.left
            else:
                child_node = node.right

            if parent_node is not None:  # checking for root deletion
                if parent_node.left == node:
                    parent_node.left = child_node
                else:
                    parent_node.right = child_node
            else:
                self.root = child_node

            # correcting parent pointer
            child_node.parent = parent_node

        if num_of_children == 2:
            # getting next biggest value and replacing the node
            successor = self._min(node.right)
            node.value = successor.value
            self._delete_node(successor)

    def find(self, value: int) -> Node | None:
        if self.root is not None:
            return self._find(value, self.root)

    def _find(self, value: int, current_node: Node) -> Node | None:
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left is not None:
            return self._find(value, current_node.left)
        elif value > current_node.value and current_node.right is not None:
            return self._find(value, current_node.right)

    def print(self):
        if self.root is not None:
            pre_order, in_order, post_order = self._print(self.root, [], [], [])
            print(f'''  In-order: {", ".join(in_order)}\nPost-order: \
{", ".join(post_order)}\n Pre-order: {", ".join(pre_order)}''')

    def _print(self, current_node: Node, pre_order: list, in_order: list, post_order: list) -> tuple:
        if current_node is not None:
            pre_order.append(str(current_node.value))

            self._print(current_node.left, pre_order, in_order, post_order)

            in_order.append(str(current_node.value))

            self._print(current_node.right, pre_order, in_order, post_order)

            post_order.append(str(current_node.value))

            return pre_order, in_order, post_order

    def find_min_max(self):
        if self.root is not None:
            min_value = str(self._min(self.root).value)
            max_value = str(self._max(self.root).value)
            print(f'Min: {min_value}\nMax: {max_value}')
        else:
            print('Tree is empty!')

    @staticmethod
    def _min(current_node: Node) -> Node:
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    @staticmethod
    def _max(current_node: Node) -> Node:
        while current_node.right is not None:
            current_node = current_node.right
        return current_node
