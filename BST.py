from math import log2

from BST_Node import Node


class BST:
    def __init__(self, numbers: list[int]):
        self.root: Node | None = None
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
        if self.root is not None:
            return '\n'.join(inner(self.root))
        else:
            return 'Tree is empty!'

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

    def delete(self):
        if self.root is None:
            print('Tree has no nodes to delete!')
        else:
            self._delete(self.root)

    def _delete(self, current_node: Node):
        if current_node is not None:
            self._delete(current_node.left)
            self._delete(current_node.right)
            self._delete_node(current_node)

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
        else:
            print('Tree is empty!')

    def _print(self, current_node: Node, pre_order: list[str], in_order: list[str], post_order: list[str]) -> tuple:
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

    def rebalance(self):  # TODO
        def degenerate():
            node = self.root
            counter = 1
            if not node:
                return counter

            while node:
                if node.left:
                    self._right_rotate(node)
                    node = node.parent
                else:
                    counter += 1
                    node = node.right
            return counter

        def balance(node: Node):
            pass

        if self.root is None:
            print('Tree has no nodes!')
            return

    def _left_rotate(self, node: Node):
        relative_root: Node | None = node.parent
        old_right: Node = node.right
        new_right: Node | None = node.right.left

        node.right = new_right
        if new_right is not None:
            new_right.parent = node

        old_right.left, node.parent = node, old_right
        if relative_root is None:
            self.root, old_right.parent = old_right, None
        elif relative_root.right == node:
            relative_root.right, old_right.parent = old_right, relative_root
        else:
            relative_root.left, old_right.parent = old_right, relative_root

    def _right_rotate(self, node: Node):
        relative_root: Node | None = node.parent
        old_left: Node = node.left
        new_left: Node | None = node.left.right

        node.left = new_left
        if new_left is not None:
            new_left.parent = node

        old_left.right, node.parent = node, old_left
        if relative_root is None:
            self.root, old_left.parent = old_left, None
        elif relative_root.right == node:
            relative_root.right, old_left.parent = old_left, relative_root
        else:
            relative_root.left, old_left.parent = old_left, relative_root

    def export(self):
        return (f'''
\\begin{{tikzpicture}}
\\node{{{self.root.value}}}
{self._export(self.root.left) if self.root.left else "    child[missing]"}
{self._export(self.root.right) if self.root.right else "    child[missing]"};
\\end{{tikzpicture}}
''')

    def _export(self, node: Node, indent: int = 1):
        if not node.left and not node.right:
            return '    '*indent + f'child {{node {{{node.value}}}}}'
        sub_left = f'{self._export(node.left, indent+1)}' if node.left else '    '*(indent+1) + 'child[missing]'
        sub_right = f'{self._export(node.right, indent+1)}' if node.right else '    '*(indent+1) + 'child[missing]'
        return '    '*indent + f'child {{node {{{node.value}}}\n{sub_left}\n{sub_right}}}'

