l=["vinoth","kumar","naveen","mohamadnaveed"]             #1.Take a list of strings
for i in range(0,len(l)):
    for j in range(i+1,len(l)):                            #2.Two loops to iterate and check the length of the string
        if len(l[i])<len(l[j]):
            l[i],l[j]=l[j],l[i]                            #3.After sorting print the firts string inthe sorted list
print(l[0])


"""
questions:
1.print the largest string in  the list"""