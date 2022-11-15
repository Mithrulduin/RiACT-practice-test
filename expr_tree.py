from tree import Node, Leaf, Visitor


class Add(Node):
    def __init__(self, l_child, r_child):

        super().__init__("Add", l_child, r_child)

    def accept(self, vis):

        if isinstance(vis, EvaluateExpression):
            return self.children[0].accept(vis) + self.children[1].accept(vis)

        elif isinstance(vis, PrintExpression):
            output = "(" + self.children[0].accept(vis) + " + " + self.children[1].accept(vis) + ")"
            return output


class Multiply(Node):

    def __init__(self, l_child, r_child):
        """
        :param l_child: 1st multiplicand
        :param r_child: 2nd multiplicand
        """
        super().__init__("Multiply", l_child, r_child)

    def accept(self, vis):

        if isinstance(vis, EvaluateExpression):
            return self.children[0].accept(vis) * self.children[1].accept(vis)

        elif isinstance(vis, PrintExpression):
            output = "(" + self.children[0].accept(vis) + " * " + self.children[1].accept(vis) + ")"
            return output


class Divide(Node):

    def __init__(self, l_child, r_child):
        """
        :param l_child: dividend
        :param r_child: divisor
        """
        super().__init__("Divide", l_child, r_child)

    def accept(self, vis):

        if isinstance(vis, EvaluateExpression):
            if isinstance(self.children[0].accept(vis), float) or isinstance(self.children[1].accept(vis), float):
                return self.children[0].accept(vis).__truediv__(self.children[1].accept(vis))
            else:
                return self.children[0].accept(vis).__floordiv__(self.children[1].accept(vis))

        elif isinstance(vis, PrintExpression):
            output = "(" + self.children[0].accept(vis) + " / " + self.children[1].accept(vis) + ")"
            return output


class Negative(Node):

    def __init__(self, child):
        super().__init__("Negative", child)

    def accept(self, vis):

        if isinstance(vis, EvaluateExpression):
            return - self.children[0].accept(vis)

        elif isinstance(vis, PrintExpression):
            output = "-" + self.children[0].accept(vis)
            return output


class Integer(Leaf):

    def __init__(self, x):
        super().__init__("Integer(" +str(x) + ")")

    def accept(self, vis):

        if isinstance(vis, EvaluateExpression):
            return int(self.name[8:-1])

        elif isinstance(vis, PrintExpression):
            return self.name[8:-1]


class Float(Leaf):

    def __init__(self, x):
        super().__init__("Float(" +str(float(x)) + ")")

    def accept(self, vis):

        if isinstance(vis, EvaluateExpression):
            return float(self.name[6:-1])

        elif isinstance(vis, PrintExpression):
            return self.name[6:-1]


# Visitor which prints mathematical expressions
class PrintExpression(Visitor):

    def traverse(self, tree):
        output = self.visit(tree)
        if output[0] == '(':
            output = output[1:]
        if output[-1] == ')':
            output = output[:-1]
        return output

    def visit(self,tree):
        output = tree.accept(self)
        return output


# Visitor which evaluates mathematical expressions
class EvaluateExpression(Visitor):

    def traverse(self, tree):
        return self.visit(tree)

    def visit(self, tree):
        return tree.accept(self)















