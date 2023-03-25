
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
"""
program for bubblesort for ascending
"""
def bubblesort(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
list=[-2,3,4,1,5,0,-1]
bubblesort(list)
print("the sorted list in ascending order:",list)


"""ASWATHI-------,PROGRAM FOR INSERTION SORT ALGORITHM"""
l=[2,43,12,7,23]
for i in range(len(l)):
    for j in range(i+1):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)