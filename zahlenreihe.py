# zahlenreihe

#n = input ("Bitte n eingeben:")
#n = int(n)
n = 1000
for i in range(1, n+1):
    if(i < n):
        print(i, end =" < ")
    else:
        print(i)  
print("\n")  

        # alle geraden Zahlen von 1..n ausgeben
for i in range  (1, n+1):
    

    if( i % 2 == 0):
        print (i, end = " > ")


print("\n")  
        #alle ungerade Zahlen von 1..n ausgeben

for i in range (1, n+1):

    if(i%2 !=0):
        print (i,end =" > ")        


        #alle zahlen von 1..n, die durch 9 teilbar sind
for i in range (1,n+1):

      if(i%9 == 0):
          print(i, end =" > ")