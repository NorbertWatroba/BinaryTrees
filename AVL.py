from BinaryTree import *


class AVL(BinaryTree):
    def __init__(self, numbers: list[int]):
        if len(numbers) != len(set(numbers)):
            print('Duplicates has been omitted!')
        numbers = sorted(set(numbers))
        mid_index = len(numbers) // 2
        median = numbers[mid_index]
        self.root = Node(median)
        self.root.left = self._create(numbers[:mid_index], self.root)
        self.root.right = self._create(numbers[mid_index+1:], self.root)
        super().__init__(self.root)

    def _create(self, numbers: list[int], parent: Node) -> Node | None:
        if not numbers:
            return None
        mid_index = len(numbers) // 2
        median = numbers[mid_index]
        node = Node(median, parent)
        node.left = self._create(numbers[:mid_index], parent)
        node.right = self._create(numbers[mid_index + 1:], parent)
        return node

    def insert(self, values: list[int]):
        super().insert(values)
        if not self._balanced(self.root):
            self.rebalance()

    def remove_values(self, values: list[int] | map):
        super().remove_values(values)
        if not self._balanced(self.root):
            self.rebalance()

    def _balanced(self, node: Node) -> bool:
        def get_height(n: Node) -> int:
            if n:
                return max(get_height(n.left), get_height(n.right)) + 1
            else:
                return 0
        if not node:
            return True
        if abs(get_height(node.left) - get_height(node.right)) > 1:
            return False
        return all([self._balanced(node.left), self._balanced(node.right)])

