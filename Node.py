class Node:
    def __init__(self, value: int, parent=None):
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = parent
