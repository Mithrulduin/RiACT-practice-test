from tree import Node, Leaf, Visitor

# A class of styles for printing of trees with a encoded symbol scheme
class NodeStyle:

    INDENT = []
    BULLET = ["* "]
    TREE = ["─╼ ", " ╿ ", " ├─╼ ", " └─╼ ", " ├─┮ ", " │", " └─┮ "]

# Visitor class which performs printing of a tree.
class PrintTree(Visitor):

    def __init__(self, style):
        """
        Initializes the print visitor with a style

        :type style: NodeStyle
        """
        self.style = style

    def traverse(self, tree, **kwargs):
        """

        :param tree: root Node
        :param kwargs: used to pass depth for indent purposes
        :return: string
        """
        if self.style == NodeStyle.INDENT:

            if len(kwargs) == 0:
                depth = 0
            else:
                depth = kwargs["depth"]

            output = ""

            for i in range(depth):
                output += "  "

            output += str(tree.name) + "\n"

            if len(tree.children) != 0:
                for c in tree.children:
                    output += self.traverse(c, depth=depth+1)

            if depth != 0:
                return output
            else:
                return output[:-1]

        if self.style == NodeStyle.BULLET:

            if len(kwargs) == 0:
                depth = 0
            else:
                depth = kwargs["depth"]

            output = ""

            for i in range(depth):
                output += "  "

            output += NodeStyle.BULLET[0] + str(tree.name) + "\n"

            if len(tree.children) != 0:
                for c in tree.children:
                    output += self.traverse(c, depth=depth + 1)

            if depth != 0:
                return output
            else:
                return output[:-1]

        if self.style == NodeStyle.TREE:

            if "line_ind" in kwargs.keys():
                lines = kwargs["line_ind"]
            else:
                lines = dict()

            if (tree.parent is None) and isinstance(tree, Leaf):
                return NodeStyle.TREE[0]+tree.name
            else:

                if len(kwargs) == 0:
                    depth = 0
                else:
                    depth = kwargs["depth"]

                output = ""

                if tree.parent is not None:

                    if not (tree.parent.children[-1] is tree):
                        lines[depth-1] = 1

                    if tree.parent.children[-1] is tree:
                        lines.pop(depth-1, None)

                for i in range(depth-1):

                    if i in lines.keys():

                        if lines[i] == 1:
                            output += NodeStyle.TREE[5]

                    else:
                        output += "  "

                if (tree.parent is None) and isinstance(tree, Node):
                    output += NodeStyle.TREE[1]
                elif not(tree.parent.children[-1] is tree) and isinstance(tree, Leaf):
                    output += NodeStyle.TREE[2]
                elif isinstance(tree, Leaf):
                    output += NodeStyle.TREE[3]
                elif not(tree.parent.children[-1] is tree) and not isinstance(tree, Leaf):
                    output += NodeStyle.TREE[4]
                elif (tree.parent.children[-1] is tree) and len(tree.children) > 0:
                    output += NodeStyle.TREE[6]

                output += str(tree.name) + "\n"

                if len(tree.children) != 0:
                    for c in tree.children:
                        output += self.traverse(c, depth=depth + 1, line_ind=lines)

                if depth != 0:
                    return output
                else:
                    return output[:-1]
