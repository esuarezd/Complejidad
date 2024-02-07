import random
from time import time
from memory_profiler import profile
@profile
def FuerzaBruta():
    a=[]
    print('Ingrese cuantos numeros aleatorios desea insertar')
    n=int(input())
    for i in range (n):
        a.append(random.randint(-100, 100))
    l=len(a)
    count=0;
    i=0;
    start_time = time()
    while i < l:
        j=i+1
        while j < l:
            k=j+1
            while k < l:
                if ((a[i] + a[j] + a[k]) == 0):
                    count +=1
                    print('Tripleta '+str(count)+': '+str(a[i])+' , '+str(a[j])+' , '+str(a[k]))
                k+=1
            j+=1
        i+=1
    elapsed_time = time() - start_time
    print("Elapsed time: %.20f seconds." % elapsed_time)

FuerzaBruta()
