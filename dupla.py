import random
from time import time
from memory_profiler import profile
# ejemplo para entender complejidad
@profile
def dupla():
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
            if ((a[i] + a[j]) == 0):
                count +=1
                #print('Dupla '+str(count)+': '+str(a[i])+' , '+str(a[j]))
            j+=1
        i+=1
    elapsed_time = time() - start_time
    print('La lista con '+str(l)+' numeros, tiene '+str(count)+' duplas')
    print("Tiempo trascurrido: %.20f seconds." % elapsed_time)

dupla()