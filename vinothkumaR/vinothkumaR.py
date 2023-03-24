l=["vinoth","kumar","naveen","mohamadnaveed"]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if len(l[i])<len(l[j]):
            l[i],l[j]=l[j],l[i]
print(l[0])




"""
psuedocode
1.Take a list of strings
2.Two loops to iterate and check the length of the string
3.After sorting print the firts string inthe sorted list
"""



"""
questions:
1.print the largest string in  the list"""