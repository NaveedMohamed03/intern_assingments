

txt="my car is blue and car number 6220"
list=txt.split(" ")
for i in list:
    x=txt.count(i)
    if x>1:
        y=txt.replace(i,"bike")
print(y)