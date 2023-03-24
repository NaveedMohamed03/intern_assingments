txt="my car is blue and car number 6220"
a=txt.split(" ")
for i in a:
    x=txt.count(i)
    if x>1:
        y=txt.replace(i,"bike")
print(y)