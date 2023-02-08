from tkinter import *

#funciones

def setup():

    global palabra, palabra2
    for i in palabra:
        palabra2 = palabra2 + "_ "
    print(palabra2)
    pedir_letra()

def vida_perdida():
    global vida
    if vida > 0:
        vida -= 1
        print(vida)
        pedir_letra()
    else:
        game_over()
    

def pedir_letra():
    global letra, acierto
    letra = input("letra: ")
    acierto = False
    comprobar()

def borrar():
    global letra, palabra
    if letra in palabra:
        index = palabra.find(letra)
        palabra = palabra.replace(letra, "y", 1)
        comprobar()
    else:
        comprobar()


def comprobar():
    global letra, vida, palabra, palabra2, palabra3, acierto
    if letra in palabra:
        index = palabra.find(letra)*2
        index2 = index + 1
        index3 = len(palabra2)
        palabra2 = palabra2[:index] + letra + palabra2[index2:index3]
        print(palabra2)
        acierto = True
        borrar()
    if acierto:
        pedir_letra()
    else:
        vida_perdida()

def game_over():
    print("game over")


#settings

gpad = 5 

#interfaz

root = Tk()
root.title("Ahorcado by Kevin")
juego = Frame(root,height=200, width=200, bg="red")
juego.pack()
titulo = Label(juego, text="Ahorcado")
titulo.grid(row=0, column=0, padx=gpad, pady=gpad)



root.mainloop()