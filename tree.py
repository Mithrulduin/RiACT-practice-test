class Node:

    def __init__(self, name, *args):
        """
        Initializes a node with a name and at least 1 child

        :param name: name of the node
        :param args: sequence of nodes of children
        """
        if len(args) == 0 and not isinstance(self, Leaf):
            raise TypeError

        self.name = name
        self.children = []

        for arg in args:
            self.children.append(arg)

        self.parent = None

        for c in self.children:
            c.parent = self

    def accept(self):
        return self.name


class Leaf(Node):

    def __init__(self, name):
        """
        Initializes a leaf with a name

        :param name: name of the leaf
        """
        super().__init__(name)


class Visitor:

    def traverse(self, tree):
        """
        Virtual function which performs an operation on a node with respect to its children.

        :type tree: Node
        """
        pass

    def visit(self, tree):
        pass
