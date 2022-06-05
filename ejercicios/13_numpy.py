import numpy as np

lista_de_listas = [[-44, 12], [12.0, 51], [1300, -5.0]]
a = np.array(lista_de_listas)
dim_a=a.shape

print("Matriz original")
print(a)
print()

#EJE 1
# a[1]-=5 
# print(a)

#EJE 2
# a*=5 
# print(a)

#EJE 3
# a[:2]/=-5 
# print(a)

#EJE 4
# print(a[dim_a[0]-1]) 

#EJE 5
# sumat = 0
# for x in a:
#     for y in x:
#         sumat += y
# print(sumat)

#EJE 6
# print(np.sum(a))

#EJE 7
# sumat = 0
# b=a[:2]
# dim_b=b.shape

# for x in b:
#     for y in x:
#         sumat += y
# print(sumat/(dim_b[0]*dim_b[1]))

#EJE 8
# sumat = 0
# b=a[:2]
# dim_b=b.shape
# print(np.mean(b))
