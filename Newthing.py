

import random

file = open("C:\\Users\\cole.dylewski\\Documents\\Python stuff\\areacodes.txt","r")
junk = file.readlines()


junk.sort()


for num in range(0,2):
    temp = junk[random.randint(0,len(junk))]
    areacode = "("+temp[0:3]+") "
    x = 0
    numbah=""
    while (x <7):

        y = random.randint(0,9)
        numbah+=str(y)
        if(x==2):numbah+="-"
        x+=1
        numbr = areacode + numbah
    print(numbr)
