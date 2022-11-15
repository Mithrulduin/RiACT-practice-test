from tree import Leaf, Node, Visitor
from print_tree import PrintTree, NodeStyle
from expr_tree import EvaluateExpression, PrintExpression, Add, Integer, Divide, Multiply, Float, Negative

trees = [
            Leaf("Scene"),
            Node("Scene", Leaf("Table"), Leaf("Object")),
            Node("Scene", Node("Robot", Node("Flange", Node("Gripper", Leaf("Object"))), Leaf("Camera")), Node("Table", Leaf("Box")))
        ]
expected = [
            "Scene",
            "Scene\n  Table\n  Object",
            "Scene\n  Robot\n    Flange\n      Gripper\n        Object\n    Camera\n  Table\n    Box"
        ]
visitor = PrintTree(NodeStyle.INDENT)

print(visitor.traverse(trees[2]))

