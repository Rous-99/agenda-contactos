import tkinter
from tkinter import INSERT
from properties import *

# i=0
###CREAMOS LAS FUNCIONES QUE VAMOS A NECESITAR###

lista_usuarios=[] #defino una lista vacia donde se van a ir guardando los usuarios

def eliminarContacto():
    pass


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
    with open(nombreArchivo, 'w') as user: 
        ###AÑADO AL ARCHIVO CREADO UNICAMENTE EL ÚLTIMO ELEMENTO DE LA LISTA, QUE ES EL NUEVO CONTACTO AGREGADO###
        contacto_nuevo=lista_usuarios[-1] #lista de caracteres
        print(contacto_nuevo)
        user.write(contacto_nuevo)
        with open("contactos.txt", "a") as contacto:
            contacto.write(contacto_nuevo +"/" + nombreArchivo + "\n")
    user.close()
    

def guardarContacto(): #para crear el arhivo de txt de cada usuario

    ###CON LOS GETS SACO EL VALOR DE LAS VARIABLES###
   name=nombre.get()
   nombre_usuario=username.get()
   correo=email.get()
   pagina_web=paginaWeb.get()

   print(name)

   lista_usuarios.append(name+"," +nombre_usuario + "," + correo + "," + pagina_web) #separo con $ para visualizar mejor la lista, la lista me sirve para añadir contactos a contactos.txt, pero se borra cuando cierro la app, asi que debo almacenar los contactos en txt
   archivarContacto()
#    print(name, nombre_usuario,correo, pagina_web)
#    print(lista_usuarios)

def editarContacto(archivo_contacto, datos_contacto):
    # #   ###CON LOS GETS SACO EL VALOR DE LAS VARIABLES###
    name=nombre.get()
    nombre_usuario=username.get()
    correo=email.get()
    pagina_web=paginaWeb.get()

    with open("contactos.txt", "r") as contactos:
        lines=contactos.readlines()
        print(lines)
        busqueda_contacto=datos_contacto+"/"+archivo_contacto+"\n" #este salto de linea se aplica de verdad?
        print("busco esto: " + busqueda_contacto)
        indice_contacto=lines.index(busqueda_contacto)
        print(indice_contacto)
        lines[indice_contacto]=name+"," +nombre_usuario + "," + correo + "," + pagina_web+"/"+archivo_contacto
        
     
    
    with open("contactos.txt", "w") as contactos_edit:
        # contactos_edit.write("me deberia sustituir todo")
        for i in lines:
            contactos_edit.write(i+"\n")
        # for contacto in lines:
        #     contactos_edit.write(contacto + "\n")

            
    ###filename (input), line__number(input), text=input

    with open(archivo_contacto, "w") as archivoEditado:
        
        archivoEditado.write(name +"," +nombre_usuario + "," + correo + "," + pagina_web)#quiero escribir lo que haya actualmente en el entry no?

  
    


def buscarContacto():
    contacto=contact.get() #para buscar por el nombre
    print(contacto)
    ##LEER EL ARCHIVO CONTACTOS###
    archivo_contactos=open("contactos.txt", "r")
    for linea in archivo_contactos: #esto me lee cada linea del archivo
        if contacto in linea: #como hago para que deje de leer las siguientes lineas si ya ha encontrado el nombre?
            datos_contacto, archivo_contacto=linea.strip().split("/")
            print("Lo he encontrado")
            # print(datos_contacto)
            print(archivo_contacto) 
            editarContacto(archivo_contacto, datos_contacto) #solo si existe el contacto quiero que me lo edite
        else:
            print("No existe el contacto")
    

    


root=tkinter.Tk() #creamos la ventana principal, por convención se llama root
root.geometry(SIZE) #redimensionamos la ventana
root.title("Agenda de usuarios")  #añadimos un titulo a la ventana
root.iconbitmap('E:\\ARCHIVOS\\Desktop\\Proyecto-final-agenda-usuarios\\agenda-contactos\\img\\contact.ico')

###CREAMOS LAS VARIABLES###
nombre=tkinter.StringVar()
username=tkinter.StringVar()
email=tkinter.StringVar()
paginaWeb=tkinter.StringVar()
contact=tkinter.StringVar()


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

buscarContactoEtiqueta=tkinter.Label(root, text="Nombre del contacto a buscar",font=(FONT_STYLE,FONT_SIZE_LABEL), fg=LETTER_COLOR)
buscarContactoEtiqueta.grid(row=7, column=1, padx=20, pady=10)

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

contactoBuscado=tkinter.Entry(root, textvariable=contact, font=(FONT_STYLE, 15))
contactoBuscado.grid(row=8, column=1, ipadx=100, ipady=5, columnspan=2)


###CREAMOS LOS BOTONES###
botonGuardar=tkinter.Button(root, text="GUARDAR CONTACTO", font=(FONT_STYLE,15, FONT_WEIGHT),fg=LETTER_BUTTON, bg=BG_BUTTON, command=guardarContacto)
# botonEliminar=tkinter.Button(root, text="EDITAR CONTACTO",font=(FONT_STYLE,15, FONT_WEIGHT), fg=LETTER_BUTTON, bg=BG_BUTTON)
botonGuardar.grid(row=1, column=3, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
# botonEliminar.grid(row=2, column=3, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
botonBuscar=tkinter.Button(root, text="BUSCAR CONTACTO", font=(FONT_STYLE,15, FONT_WEIGHT),fg=LETTER_BUTTON, bg=BG_BUTTON, command=buscarContacto)
botonBuscar.grid(row=3, column=3, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
# botonEditar=tkinter.Button(root, text="EDITAR CONTACTO",font=(FONT_STYLE,15, FONT_WEIGHT), fg=LETTER_BUTTON, bg=BG_BUTTON)
# botonEditar.grid(row=4, column=3, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)




root.mainloop() #va a registrar todo lo que ocurre mientras la ventana está abierta