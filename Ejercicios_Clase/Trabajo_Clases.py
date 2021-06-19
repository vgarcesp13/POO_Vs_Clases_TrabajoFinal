#frase = input("Ingrese frase: ")
#for indice in range(len(frase)):
#    print(indice, '=', frase[indice])
    
'''for car in frase: #car es el caracter en la frase 1cuando un in esta dentro de un for|
    if car in("a", "e", "i", "o", "u","A", "E", "I", "O", "U" ):
       if car in ["A", "E", "I", "O", "U"]:
          continue
       else:
         cvoc=cvoc+1
print('cantidad vocales:{}'.format(cvoc))'''

def vocales(Hola):
    for car in Hola:
        if car in('a', 'e', 'i', 'o', 'u'):
            print(car)        