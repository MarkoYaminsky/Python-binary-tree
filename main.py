from transistor import Transistor
from node import Node

transistor_1 = Transistor("p-n-p", "KT369A", 10, 10)
transistor_2 = Transistor("n-p-n", "KT369B", 8, 10)
transistor_3 = Transistor("p-n-p", "KT369A", 12, 8)
transistor_4 = Transistor("p-n-p", "KT369B", 9, 12)

root = Node(transistor_1)
root.insert(transistor_2)
root.insert(transistor_3)
root.insert(transistor_4)

print(*root.inorder_traversal(root), sep='\n')
print("*************")
print(root.find_by_amperage(12))
print("*************")
root.delete("n-p-n")
print(*root.inorder_traversal(root), sep='\n')
print("*************")
