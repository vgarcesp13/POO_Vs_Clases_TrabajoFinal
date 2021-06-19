class lista:
    def __init__(self,datos): #self se pone para trabajar con los atributos
        self.datos = datos #inicializar los atributos de una clase
#lista coleccion de elemntos de cualquier tipo 
datos = (2, 5.7, 'Hola', True) #ala tupla no se puede añadir mas valores
numeros = [2, 4, 6, 7, 8,1, 10]
numeros.append(13) #.append añade un numero a la lista
numeros.append(16)
nombres = ["daniel", "juan", "ana"]
print(numeros)
print(datos[0], numeros[-1], nombres[2]) #-1 presenta el ultimo valor
#lista1 = Lista()       
for a in numeros:
    print(a)   
for i in range(0,9 ): #i posicion
    if i % 2 !=0:
       print(numeros[i])
i= 0
while (i< 9):
    if i % 2==0:
        print(numeros[i])
    i=i+1
print("End")
datos = {"nombre": "Dani", "edad": "50", "docente": True}
datos ["sexo"]= "Masculino"
datos["nombre"] = "Jose"

notas = [
    {"nombre": "Perla", "Nota": 100},
    {"nombre": "Ana", "Nota": 90},
    {"nombre": "Chik", "Nota": 80},
    
]
for alumno in notas:
    if alumno:
        
#print(datos, datos["nombre"])