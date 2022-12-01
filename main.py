import tkinter
# from tkinter import *
from properties import *

root=tkinter.Tk() #creamos la ventana principal, por convención se llama root
root.geometry(SIZE) #redimensionamos la ventana
root.title("Agenda de usuarios")  #añadimos un titulo a la ventana
root.configure(background=BACKGROUND_COLOR)
etiqueta=tkinter.Label(root,text="Bievenido a tu agenda de usuarios!", bg="blue")
etiqueta.pack(fill=tkinter.X)

def saludo(nombre):
    print("Hola " + nombre) # se muestra en la consola

boton=tkinter.Button(root,text="Presiona", padx=40, pady=10, command= lambda: saludo("python"))
boton.pack(side=tkinter.BOTTOM)

etiqueta_texto=tkinter.Label(root)
etiqueta_texto.pack()


cajaTexto=tkinter.Entry(root)
cajaTexto.pack(side=tkinter.RIGHT)

def textoDeLaCaja():
    texto=cajaTexto.get()
    etiqueta_texto["text"]=texto
    print(texto)

boton_texto=tkinter.Button(root,text="Enseñame el texto", padx=40, pady=10, command=textoDeLaCaja)
boton_texto.pack(side=tkinter.LEFT)

# boton1=tkinter.Button(root,text="boton1", width=10, height=10)
# boton2=tkinter.Button(root,text="boton2", width=10, height=10)
# boton3=tkinter.Button(root,text="boton3", width=10, height=10)

# boton1.grid(row=4, column=2)

root.mainloop() #va a registrar todo lo que ocurre mientras la ventana está abierta
