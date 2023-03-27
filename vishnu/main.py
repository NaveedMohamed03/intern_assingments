def find_first_non_repeating_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None
string = "Rolls Royce"
result = find_first_non_repeating_char(string)
print(result)

"""
psuedocode:
First write def function 
Then by using for loop iteration takes place 
After iteration we give string
 

added the new line"""

