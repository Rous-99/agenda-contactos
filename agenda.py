import tkinter
from tkinter import INSERT
from properties import *

# i=0
###CREAMOS LAS FUNCIONES QUE VAMOS A NECESITAR###

lista_usuarios=[] #defino una lista vacia donde se van a ir guardando los usuarios

def eliminarContacto():
    pass

def editarContacto():
    pass

# def suma(i):
#    i=+1
#    return i

# def consultarAgenda():
#     r=tkinter.Text(root, width=80, height=15, bg=BG_BUTTON, fg=LETTER_COLOR, font=(FONT_STYLE, FONT_SIZE_LABEL))
#     lista_usuarios.sort()
#     valores=[]
#     r.insert(INSERT, "Nombre\tApellido\t\tTelefono\t\tCorreo\n") #los t es para darle espacio
#     for elemento in lista_usuarios:
#         arreglo=elemento.split("/") #separo los elemento spor / y los guardo en nuevo arreglo
#         valores.append(arreglo[3])
#         r.insert(INSERT, arreglo[0]+ "\t\t" + arreglo[1] + "\t\t" + arreglo[2] + "\t\t" + arreglo[3] + "\n")
#     r.grid(row=7, column=1)
#     spin=tkinter.Spinbox(root, value=valores, textvariable=conteliminar).grid(row=7, column=1)

def archivarContacto():
    ###ABRO EL ARCHIVO SUMA PARA EXTRAER EL NÚMERO###
    archivo_suma=open("suma.txt", "r")
    num=archivo_suma.read()
    print(num)
    archivo_suma.close()
    ###NOMBRO EL ARCHIVO CON ESE NÚMERO###
    nombreArchivo= "user"+ str(num)+ ".txt"
    ###SOBREESCRIBO EN EL ARCHIVO EL NÚMERO SUMÁNDOLE 1###
    num_act=open("suma.txt", "w")
    num=int(num)+1
    num_act.write(str(num))
    num_act.close()
    ###CREO UN ARCHIVO CON EL NOMBRE ACTUALIZADO Y GUARDO LOS DATOS###
    with open(nombreArchivo, 'w') as user: #como cambio el nombre para que se vayan cambiando nuevos archivos?
        lista_usuarios.sort() #ordeno la lista
        for elemento in lista_usuarios:
            user.write(elemento +'\n')
    user.close()

def guardarContacto(): #para crear el arhivo de txt de cada usuario

    ###CON LOS GETS SACO EL VALOR DE LAS VARIABLES###
   name=nombre.get()
   nombre_usuario=username.get()
   correo=email.get()
   pagina_web=paginaWeb.get()

   lista_usuarios.append(name+"/" +nombre_usuario + "/" + correo + "/" + pagina_web) #separo con $ para visualizar mejor la lista
   archivarContacto()
   print(name, nombre_usuario,correo, pagina_web)
   print(lista_usuarios)
    #insertar codigo que haga que cuando guardo el contacto se cree un archivo nuevo con esos datos
   



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

tituloEtiqueta=tkinter.Label(root,text="AGENDA DE USUARIOS",font=(FONT_STYLE, FONT_SIZE, FONT_WEIGHT), fg=BG_BUTTON)
tituloEtiqueta.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

nombreEtiqueta=tkinter.Label(root,text="Nombre", font=(FONT_STYLE,FONT_SIZE_LABEL),fg=LETTER_COLOR)
nombreEtiqueta.grid(row=1, column=0, padx=20, pady=10)

usernameEtiqueta=tkinter.Label(root, text="Username",font=(FONT_STYLE,FONT_SIZE_LABEL), fg=LETTER_COLOR)
usernameEtiqueta.grid(row=2, column=0, padx=20, pady=10)

emailEtiqueta=tkinter.Label(root, text="Email",font=(FONT_STYLE,FONT_SIZE_LABEL), fg=LETTER_COLOR)
emailEtiqueta.grid(row=3, column=0, padx=20, pady=10)


paginaWebEtiqueta=tkinter.Label(root, text="Pagina Web",font=(FONT_STYLE,FONT_SIZE_LABEL), fg=LETTER_COLOR)
paginaWebEtiqueta.grid(row=4, column=0, padx=20, pady=10)

# eliminarContactoEtiqueta= tkinter.Label(root, text="Eliminar contacto", fg=LETTER_COLOR, bg=BACKGROUND_COLOR)
# eliminarContactoEtiqueta.grid(row=5, column=1)

###CREAMOS LAS ENTRADAS###

nombreEntrada=tkinter.Entry(root, textvariable=nombre, font=(FONT_STYLE, 15))
nombreEntrada.grid(row=1, column=1, ipadx=100, ipady=5, columnspan=2)

usernameEntrada=tkinter.Entry(root, textvariable=username, font=(FONT_STYLE, 15))
usernameEntrada.grid(row=2, column=1, ipadx=100, ipady=5, columnspan=2)

emailEntrada=tkinter.Entry(root, textvariable=email, font=(FONT_STYLE, 15))
emailEntrada.grid(row=3, column=1, ipadx=100, ipady=5, columnspan=2)

paginaWebEntrada=tkinter.Entry(root, textvariable=paginaWeb, font=(FONT_STYLE, 15))
paginaWebEntrada.grid(row=4, column=1, ipadx=100, ipady=5, columnspan=2)

###CREAMOS LOS BOTONES###
botonGuardar=tkinter.Button(root, text="GUARDAR CONTACTO", font=(FONT_STYLE,15, FONT_WEIGHT),fg=LETTER_BUTTON, bg=BG_BUTTON, command=guardarContacto)
botonEliminar=tkinter.Button(root, text="ELIMINAR CONTACTO",font=(FONT_STYLE,15, FONT_WEIGHT), fg=LETTER_BUTTON, bg=BG_BUTTON)
botonGuardar.grid(row=5, column=1, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
botonEliminar.grid(row=6, column=1, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
botonConsultar=tkinter.Button(root, text="VER AGENDA", font=(FONT_STYLE,15, FONT_WEIGHT),fg=LETTER_BUTTON, bg=BG_BUTTON)
botonConsultar.grid(row=7, column=1, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)



root.mainloop() #va a registrar todo lo que ocurre mientras la ventana está abierta