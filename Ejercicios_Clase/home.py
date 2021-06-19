class Cadena:
    def __init__(self, Str):
        self.__String= Str
   
    @property
    def String(self):
        return self.__String
    
    def Longitud(self):
        N= len(self.__String)
        return N

    def MostrarDatos(self):
        print("En numero de caracteres de la frase ({}) es de: {}.".format(self.__String, self.Longitud()))

class Caracteres(Cadena):
    def __init__(self, Str):
        super().__init__(Str)

    def BP(self):
        Buscar1= input("Ingrese La Palabra Que Desea Saber Su Posicion: ")
        Buscar1= Buscar1.lower()
        S= self.String.lower()
        if Buscar1 in S:
            Posicion= S.index(Buscar1)
            return print("La Primera Ocurrencia De La Palabra ({}), Se Encuentra En la Posicion #{}.".format(Buscar1,
            Posicion))
        else:
            return print((-1))
    
    def BuscarP(self):
        Buscar2= input("Ingrese La Palabra Que Desea Saber Sus Posiciones Dentro Del Texto: ")
        Buscar2= Buscar2.lower()
        S= self.String.lower()
        Lista= []
        cont=0
        while cont != -1:
            cont= S.find(Buscar2, cont)

            if cont != -1:
                Lista.append(cont)
                cont+= 1

        return print("La Palabra ({}), Se Encuentra En Las Posiciones: {}.".format(Buscar2, Lista))
 
    def EliminarP(self):
        Buscar3= input("Ingrese La Palabra Que Desea Eliminar Del Texto: ")
        Buscar3= Buscar3.lower()
        S= self.String.lower()
        Lista= S.split()

        for i in Lista:
            if Buscar3 in Lista:
                Lista.remove(Buscar3)
        Lista= " ".join(Lista)
        return print("El Texto Sin La Palabra Que Elimino Es: {}.".format(Lista.capitalize()))

    def ExtraerDN(self):
        S= ""
        Dic={}
        for i in self.String:
            if i in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                S+= i
        
        Dic[S]=len(S)
        return print("Los Digitos Numericos Que Hay En El Texto Son: {}".format(Dic))
    def InsertarP(self):
        Buscar4= input("Ingrese la palabra que desea agregar a la frace: ")
        Buscar4= Buscar4.lower()
        S= self.String.lower()
        if Buscar4 in S:
            Lista= S.split()
            i=Lista.index(Buscar4)
            Lista.insert(i,Buscar4)
            List= " ".join(Lista)
            return print("El Texto Mas La Palabra Que Inserto Es: {}.".format(List.capitalize()))
        else:
            return print("La Palabra Que Ingreso No Se Encuentra En El Texto.")

    def ExtraerCE(self):
        S= self.String.lower()
        s= ""
        Dic={}
        for i in S:
            if i not in (" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                s+= i
        
        Dic[s]=len(s)
        return print("Los Digitos Especiales Que Hay En El Texto Son: {}".format(Dic))
Salir= True
while (Salir == True):
    print("\n-----Menu Principal-----")
    print("a. Ingrese 1 Si Desea Buscar La Posicion De la Primera Ocurrencia De Una Palabra En Un Texto.")
    print("b. Ingrese 2 Si Desea Buscar Las Diversas Posiciones De Una Palabra En Un Texto.")
    print("c. Ingrese 3 Si Desea Eliminar Una Palabra De Todo El Texto.")
    print("d. Ingrese 4 Si Desea Saber Cuantos Digitos Numericos Hay En Un Texto Y Cuales Son.")
    print("e. Ingrese 5 Si Desea Insertar Una Palabra Dentro De Un Texto En Su Primera Ocurrencia.")
    print("f. Ingrese 6 Si Desea Saber Cuantos Digitos Especiales Hay En Un Texto Y Cuales Son.")
    print("g. Ingrese 7 Si Desea Salir Del Menu.")
    
    Opcion= input("Ingrese Una Opcion: ")

    if(Opcion == "1"):
        Palabra= input("Ingrese Un Texto: ")
        STR= Caracteres(Palabra)
        STR.BP()
    
    elif(Opcion == "2"):
        Palabra= input("Ingrese Un Texto: ")
        STR= Caracteres(Palabra)
        STR.BuscarP()
    
    elif(Opcion == "3"):
        Palabra= input("Ingrese Un Texto: ")
        STR= Caracteres(Palabra)
        STR.EliminarP()
    
    elif(Opcion == "4"):
        Palabra= input("Ingrese Un Texto: ")
        STR= Caracteres(Palabra)
        STR.ExtraerDN()

    elif(Opcion == "5"):
        Palabra= input("Ingrese Un Texto: ")
        STR= Caracteres(Palabra)
        STR.InsertarP()

    elif(Opcion == "6"):
        Palabra= input("Ingrese Un Texto: ")
        STR= Caracteres(Palabra)
        STR.ExtraerCE()

    elif(Opcion == "7"):
        print("Ha Salido Del Menu Exitosamente.")
        Salir= False

    else:
        print("La Opcion Ingresada No Es La Correcta Intente Nuevamente.")
