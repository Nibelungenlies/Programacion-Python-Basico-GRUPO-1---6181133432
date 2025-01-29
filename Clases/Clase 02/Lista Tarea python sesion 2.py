lista = [1,2,3,4,5,6,7,8,9,10]
numeros_agregar = [11,12,13,14,15]
print(lista)
lista.extend(numeros_agregar)
print(lista)
lista.append(16)
print(lista)
lista.insert(0 , 0)
print(lista)
lista.remove(5)
print(lista)
ultimo_numero = lista.pop(15)
print(lista)
print('El numero eliminado es: ',ultimo_numero)
archivo = open('numeros.text', 'w')
print(archivo)
print("Archivo 'numeros.txt' creado correctamente")
with open("numeros.txt", "w") as archivo:
    for numero in lista:
            archivo.write(str(numero) + "\n")

print(archivo)
archivo.close

archivo = open('numeros.txt', 'r')
contenido_lista = archivo.read

