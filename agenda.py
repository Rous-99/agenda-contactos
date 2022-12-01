import tkinter
from tkinter import PhotoImage

from properties import *


###CREAMOS LAS FUNCIONES QUE VAMOS A NECESITAR###



def eliminarContacto():
    pass

def editarContacto():
    pass

def guardarContacto(): #para crear el arhivo de txt de cada usuario
    pass



root=tkinter.Tk() #creamos la ventana principal, por convención se llama root
root.geometry(SIZE) #redimensionamos la ventana
root.title("Agenda de usuarios")  #añadimos un titulo a la ventana
root.iconbitmap('E:\\ARCHIVOS\\Desktop\\Proyecto-final-agenda-usuarios\\agenda-contactos\\img\\contact.ico')

###CREAMOS LAS VARIABLES###
nombre=tkinter.StringVar()
username=tkinter.StringVar()
email=tkinter.StringVar()
paginaWeb=tkinter.StringVar()


###CREAMOS LAS ETIQUETAS###

tituloEtiqueta=tkinter.Label(root,text="AGENDA DE USUARIOS",font=(FONT_STYLE, FONT_SIZE, FONT_WEIGHT), fg=LETTER_COLOR, bg=BACKGROUND_COLOR)
tituloEtiqueta.grid(row=0, column=1)

nombreEtiqueta=tkinter.Label(root,text="Nombre", fg=LETTER_COLOR, bg=BACKGROUND_COLOR)
nombreEtiqueta.grid(row=1, column=0)

usernameEtiqueta=tkinter.Label(root, text="Username", fg=LETTER_COLOR, bg=BACKGROUND_COLOR)
usernameEtiqueta.grid(row=2, column=0)

emailEtiqueta=tkinter.Label(root, text="Email", fg=LETTER_COLOR, bg=BACKGROUND_COLOR)
emailEtiqueta.grid(row=3, column=0)


paginaWebEtiqueta=tkinter.Label(root, text="Pagina Web", fg=LETTER_COLOR, bg=BACKGROUND_COLOR)
paginaWebEtiqueta.grid(row=4, column=0)

# eliminarContactoEtiqueta= tkinter.Label(root, text="Eliminar contacto", fg=LETTER_COLOR, bg=BACKGROUND_COLOR)
# eliminarContactoEtiqueta.grid(row=5, column=1)

###CREAMOS LAS ENTRADAS###

nombreEntrada=tkinter.Entry(root, textvariable=nombre)
nombreEntrada.grid(row=1, column=1)

usernameEntrada=tkinter.Entry(root, textvariable=username)
usernameEntrada.grid(row=2, column=1)

emailEntrada=tkinter.Entry(root, textvariable=email)
emailEntrada.grid(row=3, column=1)

paginaWebEntrada=tkinter.Entry(root, textvariable=paginaWeb)
paginaWebEntrada.grid(row=4, column=1)

###CREAMOS LOS BOTONES###
botonGuardar=tkinter.Button(root, text="Guardar contacto", fg=LETTER_COLOR, bg=BACKGROUND_COLOR)
botonEliminar=tkinter.Button(root, text="Eliminar contacto", fg=LETTER_COLOR, bg=BACKGROUND_COLOR)
botonGuardar.grid(row=5, column=1)
botonEliminar.grid(row=6, column=1)



root.mainloop() #va a registrar todo lo que ocurre mientras la ventana está abierta