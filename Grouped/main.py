

"""
QUESTION:
Write a program for implementing bubblesort for ascending
"""
def bubblesort(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
list=[-2,3,4,1,5,0,-1]
bubblesort(list)
print("the sorted list in ascending order:",list)

#Vishnu code
def aggregated_dicts(list_of_dicts):
    result_dict = {}
    for i in list_of_dicts:
        for key, value in i.items():
            if key in result_dict:
                result_dict[key].append(value)
            else:
                result_dict[key] = [value]
    for key, value in result_dict.items():
        result_dict[key] = sum(value)
    return result_dict
list_of_dicts = [
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 4, 'c': 2, 'd': 4},
    {'c': 3, 'b': 8, 'e': 9}]
result_dict = aggregate_dicts(list_of_dicts)
print(result_dict)

"""ASWATHI-------,PROGRAM FOR INSERTION SORT ALGORITHM"""
l=[2,43,12,7,23]
for i in range(len(l)):
    for j in range(i+1):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)






'''Question: Program to find whether two strings are anagram of each other'''


def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    return s1==s2
s1="care"
s2="race"
print(anagram(s1,s2))

"""ASWATHI-------,PROGRAM FOR INSERTION SORT ALGORITHM"""
l=[2,43,12,7,23]
for i in range(len(l)):
    for j in range(i+1):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)






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

