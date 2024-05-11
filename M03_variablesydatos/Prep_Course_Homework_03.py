#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
# In[7]:

num = 7
print(num)


# 2) Imprimir el tipo de dato de la constante 8.5
# In[3]:

print(8.5)



# 3) Imprimir el tipo de dato de la variable creada en el punto 1
# In[8]:
print(type(num))




# 4) Crear una variable que contenga tu nombre
# In[2]:

mi_nombre = "Yvon"


# 5) Crear una variable que contenga un número complejo
# In[3]:
num_comp = 3+4j




# 6) Mostrar el tipo de dato de la variable creada en el punto 5
# In[4]:
print(type(num_comp))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
# In[1]:

pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
# In[3]:

peque = 'True'
grande = True

print(peque==grande)
#No es lo mismo porque uno es un string y otro es booleano


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
# In[5]:
print(type(peque))
print(type(grande))




# 10) Asignar a una variable, la suma de un número entero y otro decimal
# In[1]:

suma = 5 + 3.6



# 11) Realizar una operación de suma de números complejos
# In[2]:
suma2 = 6j + 3 




# 12) Realizar una operación de suma de un número real y otro complejo
# In[4]:

suma3 = 3.5 + 3j



# 13) Realizar una operación de multiplicación
# In[5]:

5 * 45



# 14) Mostrar el resultado de elevar 2 a la octava potencia
# In[6]:

print(2**8)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
# In[8]:
cociente = 27 / 4
print(cociente)




# 16) De la división anterior solamente mostrar la parte entera
# In[9]:
cociente = 27 / 4
entero = int(cociente)
print(entero)




# 17) De la división de 27 entre 4 mostrar solamente el resto
# In[1]:
resto = 27 % 4
print(resto)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
# In[2]:

print(4*resto+15)
print(4*entero+3)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
# In[3]:
texto = " es Buena estudiante"
print(mi_nombre + texto)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
# In[4]:

print(2 == "2")
# son distintos tipos:
print(type(2))   # es tipo numéico 
print(type("2")) # es tipo string


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
# In[11]:

print(2 == int("2"))



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# In[12]:
a = float('3.8') #No acepta coma (,) para decimal debe ser punto (.)




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.
# In[15]:
sum = 3
sum -= 1
print(sum)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
# In[29]:
print(1 << 2)  # es el desplazamiento a la izquierda de bits, en este caso 1 = 0001, desplazando dos posiciones 
               # quedaría 0100 y su valor al sistema decimal es 4




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# In[23]:
#2 + '2'  # son distintos tipos
#No sería el mismo valor cambiando el tipo:
print(2 + 2)  # tipo numérico realiza la suma 
print('2' + '2')  # tipo str, imprime los dos valores como alfanumérico


# 26) Realizar una operación válida entre valores de tipo entero y string
# In[30]:
print(str(sum) + mi_nombre)


