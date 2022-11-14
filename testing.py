import unittest
import inspect

from tree import Leaf, Node, Visitor
from print_tree import PrintTree, NodeStyle
from expr_tree import EvaluateExpression, PrintExpression, Add, Integer, Divide, Multiply, Float, Negative

expressions = [
            Integer(42),
            Negative(Integer(23)),
            Divide(Integer(5), Integer(2)),
            Divide(Float(5), Integer(2)),
            Add(Integer(2), Divide(Multiply(Float(5.0), Negative(Integer(3))), Float(10.0)))
        ]

visitor = PrintTree(NodeStyle.TREE)

print(visitor.traverse(trees[0]))