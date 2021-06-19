
def palabras(frase):
    palabra = ''
    lista = []
    for letras in frase + ' ':
        if letras != ' ':
            palabra += letras
        else:
            lista.append(palabra)
            palabra = ''
    return lista
frase='    Hola   que tal   '
frase.palabras()