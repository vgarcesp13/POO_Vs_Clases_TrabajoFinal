#Importar Flask
from flask import Flask
# para renderizar las paginas html
from flask import render_template 
# para capturar los datos enviados de la pagina html a python.
from flask import request 
# Importar clase de usuarios
from coleccion import Colecciones
from calculo import Calculos
from cadena import Cadenas
from Ejercicio import Ejercicio
#instancia de flask con el nombre del modulo
app= Flask(__name__)
# configuracion de rutas o urls
#route (nombre url y el metodo(opcional))
@app.route('/')
def inicio():
    #return 'Mi primer pagina con Flask'
    return render_template("proyecto.html")

@app.route('/coleccion',methods=['GET','POST'])
def coleccion():
    opcion,valor1,valor2,resp='0','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = request.form['valor1']
        valor2 = request.form['valor2']
        if opcion == '1':
            lista = valor1.split()
            if int(valor2) < len(lista):
                col = Colecciones(lista)
                resp = col.getElemento(int(valor2))
            else:
                resp = "No existe elemento en esa posicion"
        elif opcion == '2':
            tupla = tuple(valor1.split())
            col = Colecciones(tupla)
            resp = 'Tupla ('+col.recorrido()+')'
        elif opcion == '3':
            lista = valor1.split()
            col = Colecciones(lista)
            resp = '['+col.recorrido()+']'
        elif opcion == '4':
            lista = valor1.split()
            dic={}
            for item in lista:
                pos= item.find(":")
                clave= item[:pos]
                valor= item[pos+1:]
                dic[clave]=valor
            col = Colecciones(dic)   
            resp = col.diccionario()
        elif opcion == '5':
            lista = valor1.split()
            col = Colecciones(lista)
            resp = col.invertirLista()
        elif opcion == '6':
            lista= valor1.split(" ")
            col= Colecciones(lista)
            resp= col.listaTupla()
        elif opcion == '7':
            usuarios = [{' '}]
            col=Colecciones(usuarios)
            resp= col.listaDiccionario(valor1)
        elif opcion == '8':
            pass
        elif opcion == '9':
            lista = valor1.split()
            col = Colecciones(lista)
            resp = col.listaComprehension(valor1)
        elif opcion == '10':
            lista = valor1.split()
            col = Colecciones(lista)
            resp = col.diccioComprehension()
                
    return render_template("Colecciones.html",Seleccion=opcion,n1=valor1,n2=valor2,respuesta=resp)

@app.route('/calculo', methods=['GET','POST'])
def calculo():
    opcion,valor1,valor2,resp='0','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = int(request.form['valor1'])
        valor2 = int(request.form['valor2'])
        if opcion=='1':
            cal= Calculos()
            resp= cal.fibo(valor1)
        elif opcion =='2':
            cal= Calculos()
            resp= cal.divisores(valor1)
        elif opcion=='3':
            cal= Calculos()
            if cal.primo(valor1)==True: resp= {valor1:'Primo'}
            else:resp={valor1:'No es Primo'}
        elif opcion =='4':
            cal= Calculos()
            if cal.primoGemelos(valor1,valor2)== True: resp=('Son primos gemelos')
            else: resp=('No son primos gemelos')
        elif opcion =='5':
            cal= Calculos()
            if cal.perfecto(valor1)==True: resp={valor1:'Es perfecto'}
            else: resp={valor1:'No es perfecto'}
        elif opcion =='6':
            cal= Calculos()
            if cal.amigos(valor1,valor2)== True: resp=('Los numeros son amigos')
            else: resp=('Los numeros no son amigos')
        elif opcion =='7':
            cal= Calculos()
            resp= cal.invertirNumero(valor1)
        elif opcion =='8':
            cal= Calculos()
            resp= cal.base2_10(valor1)
        elif opcion =='9':
            cal= Calculos()
            resp= cal.base10_2(valor1)
        elif opcion =='10':
            cal= Calculos()
            resp= cal.cualquierBase(valor1,valor2)    
    return render_template("Calculos.html",Seleccion=opcion,n1=valor1,n2=valor2,respuesta=resp)

@app.route('/cadena', methods=['GET','POST'])
def cadena():
    opcion,valor1,valor2,resp='0','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = request.form['valor1']
        valor2 = request.form['valor2']
        if opcion== '1':
            valo= valor1
            cad = Cadenas(valo)
            resp= cad.recorrer()
        elif opcion == '2':
            valo= valor1
            cad = Cadenas(valo)
            resp= cad.invertir()
        elif opcion == '3':
            valo= valor1
            cad = Cadenas(valo)
            resp = cad.buscar(valor2)
        elif opcion == '4':
            valo= valor1
            cad = Cadenas(valo)
            resp = cad.vocalesCadena(valor2)
        elif opcion == '5':
            valo= valor1
            cad = Cadenas(valo)
            resp = cad.ocurrencia(valor2)
        elif opcion == '6':
            valo= valor1
            cad = Cadenas(valo)
            resp = cad.concatenar(valor2)
        elif opcion == '7':
            valo= valor1
            cad = Cadenas(valo)
            resp = cad.reempla(valor2)    
        elif opcion == '8':
            valo= valor1
            cad = Cadenas(valo)
            resp = cad.cadena_lista()
        elif opcion == '9':
            lista= valor1.split(valor1)
            cad = Cadenas(lista)
            resp= cad.Convertir()
        elif opcion == '10':
            valo= valor1
            cad = Cadenas(valo)
            resp = cad.BuscarSub(valor2)
        elif opcion == '11':
            valo= valor1
            cad = Cadenas(valo)
            resp= cad.subincad(valor1, valor2)
    return render_template("Cadenas.html",Seleccion=opcion,n1=valor1,n2=valor2,respuesta=resp)

@app.route('/ayuda')
def ayuda():
    return render_template("Ayuda.html")

@app.route('/ejercicio', methods=['GET','POST'])
def ejercicio():
    opcion,valor1,valor2,resp='0','','',''
    if request.method == 'POST':
        opcion = request.form['select']
        valor1 = request.form['valor1']
        valor2 = request.form['valor2']
        obj= Ejercicio()
        if opcion == '1':
            resp= obj.Ejer1(valor1)
        elif opcion == '2':
            resp= obj.Ejer2(valor1, valor2)
        elif opcion == '3':
            resp= obj.Ejer3(valor1, valor2)
        elif opcion == '4':
            resp= obj.Ejer4(valor1, valor2)
        elif opcion == '5':
            resp= obj.Ejer5(valor1)
        elif opcion == '6':
            resp= obj.Ejer6(valor1)
        elif opcion == '7':
            resp= obj.Ejer7(valor1)
        elif opcion == '8':
            resp= obj.Ejer8(valor1,valor2)
        elif opcion == '9':
            resp= obj.Ejer9(valor1,valor2)
        elif opcion == '10':
            resp= obj.Ejer10(valor1)
        elif opcion == '11':
            resp= obj.Ejer11(valor1)
        elif opcion == '12':
            resp= obj.Ejer12(valor1)
        elif opcion == '13':
            resp= obj.Ejer13(valor1)
        elif opcion == '14':
            resp= obj.Ejer14(valor1)
        elif opcion == '15':
            resp= obj.Ejer15(valor1)
        elif opcion == '16':
            resp= obj.Ejer16(valor1)
        elif opcion == '17':
            resp= obj.Ejer17(valor1)
        elif opcion == '18':
            resp= obj.Ejer18(valor1)
        elif opcion == '19':
            resp= obj.Ejer19(valor1)
        elif opcion == '20':
            resp= obj.Ejer20(valor1)
        elif opcion == '21':
            resp= obj.Ejer21(valor1)
        elif opcion == '22':
            resp= obj.Ejer22(valor1)
        elif opcion == '23':
            resp= obj.Ejer23(valor1)
        elif opcion == '24':
            resp= obj.Ejer24(valor1)
        elif opcion == '25':
            resp= obj.Ejer25(valor1)
        elif opcion == '26':
            resp= obj.Ejer26(valor1, valor2)
        elif opcion == '27':
            resp= obj.Ejer27(valor1, valor2)
        elif opcion == '28':
            resp= obj.Ejer28(valor1)
        elif opcion == '29':
            resp= obj.Ejer29(valor1, valor2)
        elif opcion == '30':
            resp= obj.Ejer30(valor1)
        elif opcion == '31':
            resp= obj.Ejer31(valor1)
        elif opcion == '32':
            resp= obj.Ejer32(valor1, valor2)
        elif opcion == '33':
            resp= obj.subincad(valor1, valor2)
        elif opcion == '36':
            resp= obj.Ejer36(valor1)
        elif opcion == '39':
            resp= obj.Ejer39(valor1)
        elif opcion == '40':
            resp= obj.Ejer40(valor1, valor2)
        elif opcion == '41':
            resp= obj.Ejer41(valor1)
        elif opcion == '42':
            resp= obj.Ejer42(valor1)
        elif opcion == '43':
            resp= obj.Ejer43(valor1)
        
    return render_template("Ejercicios.html", Seleccion=opcion,n1=valor1,n2=valor2,respuesta=resp)



#iniciar el servidor
if __name__ == '__main__':
    app.run(port=3000,debug=True)