from BinaryTree import *


class BST(BinaryTree):

    def __init__(self, numbers: list[int]):
        self.root: Node | None = None
        self.insert(numbers)
        super().__init__(self.root)
