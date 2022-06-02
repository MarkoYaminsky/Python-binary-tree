from transistor import Transistor


class Node:
    def __init__(self, data: Transistor):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data: Transistor):
        if self.data:
            if data.amperage < self.data.amperage:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data.amperage > self.data.amperage:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find_by_amperage(self, value):
        if value < self.data.amperage:
            if self.left is None:
                return f'transistor with amperage {value} is not found'
            return self.left.find_by_amperage(value)
        elif value > self.data.amperage:
            if self.right is None:
                return f'transistor with amperage {value} is not found'
            return self.right.find_by_amperage(value)
        else:
            print(self.data)
            if self.left is not None:
                self.left.find_by_amperage(value)
            if self.right is not None:
                self.right.find_by_amperage(value)

    def delete(self, value):
        if value < self.data.transistor_type:
            if self.left is None:
                return f'transistor with values {value} is not found'
            self.left.delete(value)
        elif value > self.data.transistor_type:
            if self.right is None:
                return f'transistor with values {value} is not found'
            self.right.delete(value)
        else:
            self.data = self.right
            if self.left is not None:
                self.left.delete(value)
            if self.right is not None:
                self.right.delete(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(str(root.data))
            result = result + self.inorder_traversal(root.right)
        return result

    def __str__(self):
        return "Object deleted"
