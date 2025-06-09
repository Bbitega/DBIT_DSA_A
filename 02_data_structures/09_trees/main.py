from binary_search_tree import *


bst = BinarySearchTree()
values = [11, 6, 16, 4, 8, 13, 18]
for value in values:
    bst.insert(value)

print("Inorder Traversal (Sorted):")
bst.inorder(bst.root)
print("\n")

print("Preorder Traversal (Make a copy):")
bst.preorder(bst.root)
print("\n")

print("Postorder Traversal (Delete):")
bst.postorder(bst.root)
print("\n")

print("Search for 12:", bst.search(12))
print("Search for 20:", bst.search(20))
