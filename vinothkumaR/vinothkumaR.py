l=["vinoth","kumar","naveen","mohamadnaveed"]             #1.Take a list of strings
for i in range(0,len(l)):
    for j in range(i+1,len(l)):                            #2.Two loops to iterate and check the length of the string
        if len(l[i])<len(l[j]):
            l[i],l[j]=l[j],l[i]                            #3.After sorting print the firts string inthe sorted list
print(l[0])
"""
questions:
1.print the largest string in  the list"""
"""
psuedocode:
1.take list
2.iterate the loop and sort the list based on length of the string 
3.print the1st string in list"""


