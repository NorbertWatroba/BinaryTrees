class Node:
    def __init__(self, value, parent=None):
        self.value: int = int(value)
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = parent
