import numpy as np
'''arr = np.array([1, 2, 3], dtype=np.float16)
arr2 = np.array([4,5,6], dtype=np.int16)
suma = arr+ arr2
arr3 =np.array([7,8.0,9])
arr4 = np.array([10.45, 11.88,12.99])
intArr3 = arr3.astype(np.int32)
intArr4 = arr4.astype(np.int32)
print(intArr4)'''
################# indexado ##############
'''arr5  = np.arange(10)
print(arr5[9])
arr5[0:5] = 0.1
array_copia = arr5[0:5]
print(array_copia)
array_copia[0] = 9999
print(arr5)'''

#listas
'''lista = [1,2,3]
lista_append = lista[0:1]
print(lista_append)
lista_append[0]=888
print(lista)'''

#Arrays de dimensiones n
'''dim1 = np.array([1,2,3])
dim2 = np.array([4,5,6])
segunda = np.array([dim1,dim2])
print(segunda.shape)
print(segunda[0][2])'''

'''multidimension = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
x = multidimension[1]
x[0]
print(x)'''

politicos = np.array(["Sanchez", "Rajoy", "Zapatero", "Aznar", "Felipe", "Sanchez"])
puntuacion = np.array([[4.59,10],[5.3,10],[4.13,10],[6.39,10],[5.59,10],[8.91,10]])
puntuacion[puntuacion >9] =15 
print((politicos =="Sanchez")| (politicos=="Aznar"))
print(puntuacion)
