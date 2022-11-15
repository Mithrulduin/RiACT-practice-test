from tree import Node, Leaf, Visitor


class NodeStyle:

    INDENT = []
    BULLET = ["* "]
    TREE = ["─╼ ", " ╿ ", " ├─╼ ", " └─╼ ", " ├─┮ ", " │", " └─┮ "]


class PrintTree(Visitor):

    def __init__(self, style):

        self.style = style
        self.output = ""

    def visit(self, tree, **kwargs):

        if self.style == NodeStyle.INDENT:
            if len(kwargs)==0:
                depth=0
            else:
                depth = kwargs["depth"]

            output= depth*"  "
            output += str(tree.name) + "\n"
            for c in tree.children:
                output += self.visit(c, depth=depth+1)
            return output

        elif self.style == NodeStyle.BULLET:

            if len(kwargs) == 0:
                depth = 0
            else:
                depth = kwargs["depth"]

            output = depth * "  "
            output += NodeStyle.BULLET[0]+str(tree.name) + "\n"
            for c in tree.children:
                output += self.visit(c, depth=depth + 1)
            return output

        if self.style == NodeStyle.TREE:

            if "line_ind" in kwargs.keys():
                lines = kwargs["line_ind"]
            else:
                lines = dict()

            if (tree.parent is None) and isinstance(tree, Leaf):
                return NodeStyle.TREE[0] + tree.name + " "
            else:

                if len(kwargs) == 0:
                    depth = 0
                else:
                    depth = kwargs["depth"]

                output = ""

                if tree.parent is not None:

                    if not (tree.parent.children[-1] is tree):
                        lines[depth - 1] = 1

                    if tree.parent.children[-1] is tree:
                        lines.pop(depth - 1, None)

                for i in range(depth - 1):

                    if i in lines.keys():

                        if lines[i] == 1:
                            output += NodeStyle.TREE[5]

                    else:
                        output += "  "

                if (tree.parent is None) and isinstance(tree, Node):
                    output += NodeStyle.TREE[1]
                elif not (tree.parent.children[-1] is tree) and isinstance(tree, Leaf):
                    output += NodeStyle.TREE[2]
                elif isinstance(tree, Leaf):
                    output += NodeStyle.TREE[3]
                elif not (tree.parent.children[-1] is tree) and not isinstance(tree, Leaf):
                    output += NodeStyle.TREE[4]
                elif (tree.parent.children[-1] is tree) and len(tree.children) > 0:
                    output += NodeStyle.TREE[6]

                output += str(tree.name) + "\n"

                if len(tree.children) != 0:
                    for c in tree.children:
                        output += self.visit(c, depth=depth + 1, line_ind=lines)

    def traverse(self, tree):
        self.output = self.visit(tree)
        return self.output[:-1]
