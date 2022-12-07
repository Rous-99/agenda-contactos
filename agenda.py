from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from tkinter import INSERT
from properties import *
from os import remove

###CREAMOS LAS FUNCIONES QUE VAMOS A NECESITAR###

lista_usuarios=[] #defino una lista vacia donde se van a ir guardando los usuarios


def consultarAgenda():
    #crear una nueva ventana
    newWindow=Tk()
    newWindow.geometry(SIZE_SECOND_WD)
    newWindow.title("Consulta de Usarios")

    
   
    tv=ttk.Treeview(newWindow, columns=("Nombre", "Username", "Correo electrónico", "Página Web")) #el nombre de la columna se refiere no solo al encabezado, sino a todos los datos de esa columna
    tv.pack(fill=BOTH, expand=True)
    tv.column("#0", width=80)
    tv.column("Nombre", width=80, anchor=CENTER)
    
   
   
    #Add some style:
    # style = ttk.Style()

    # style.theme_use("clam")

    # style.configure("Treeview",
    #                 background="silver",
    #                 foreground="black",
    #                 rowheight=55,
    #                 fieldbackground="silver")


    ##encabezados##
    tv.heading("#0", text="Archivo", anchor=CENTER)
    tv.heading("Nombre", text="Nombre", anchor=CENTER)
    tv.heading("Username", text="Username", anchor=CENTER)
    tv.heading("Correo electrónico", text="Correo electrónico", anchor=CENTER)
    tv.heading("Página Web", text="Página Web", anchor=CENTER)

    '''
    La manera de insertar valores en la tabla:

        tv.insert("", END, text="", values=(28,2)) se le puede pasar una variable, el texto va en la primera columna, con values se ponen las demas columnas
    '''

    with open("contactos.txt", "r") as verContactos:
        for linea in verContactos:         #por cada linea tengo que hacer un split en las comas y guardar en variables los datos de cada contacto
            print(linea)
            linea_nueva=linea.replace('/', ',')
            print(linea_nueva)
            if linea=="\n":
                continue #no quiero que haga nada
            else:
                nombreE, usernameE,correoE,paginaWebE, archivoE=linea_nueva.strip().split(",") #cuando elimino un contacto no me puede crear las variables porque se borra el espacio y se queda sin comas
                tv.insert("", END, text=archivoE, values=(nombreE,usernameE,correoE,paginaWebE))
            
           
        
    


    mainloop()

def eliminarContacto(archivo_contacto, datos_contacto):
    #necesito que al buscar el contacto por el nombre, me busque el archivo en el que están guardado sus datos y me borre ese archivo INDIVIDUAL. Luego, que en el archivo contactos me borre la linea en la que estaba con sus datos. 

    with open("contactos.txt", "r") as contactos:
        lines=contactos.readlines()
        print(lines)
        busqueda_contacto=datos_contacto+"/"+archivo_contacto+"\n" #este salto de linea se aplica de verdad?
        print("busco esto: " + busqueda_contacto)
        indice_contacto=lines.index(busqueda_contacto)
        print(indice_contacto)
        lines[indice_contacto]="\n" #lo dejo vacio para que el contacto se borre en la linea correspondiente
        print(lines)
        
     
    
    with open("contactos.txt", "w") as contactos_edit:
        for i in lines:
            contactos_edit.write(i)
        
    ##ARCHIVO INDIVIDUAL##

    remove(archivo_contacto) #así me borra el archivo del directorio

    messagebox.showinfo("Eliminado", "Contacto eliminado con éxito")    




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

    if "@" in correo: #validar el correo, si tiene "@"
        lista_usuarios.append(name+"," +nombre_usuario + "," + correo + "," + pagina_web) #separo con $ para visualizar mejor la lista, la lista me sirve para añadir contactos a contactos.txt, pero se borra cuando cierro la app, asi que debo almacenar los contactos en txt
        archivarContacto()
        messagebox.showinfo("Guardado", "Contacto guardado con éxito")
    else:
        messagebox.showinfo("ERROR", "El correo electrónico debe contener un '@'")



        


def editarContacto(archivo_contacto, datos_contacto):
    # #   ###CON LOS GETS SACO EL VALOR DE LAS VARIABLES###
    name=nombre.get()
    nombre_usuario=username.get()
    correo=email.get()
    pagina_web=paginaWeb.get()

    if "@" in correo:
        
        with open("contactos.txt", "r") as contactos:
            lines=contactos.readlines()
            print(lines)
            busqueda_contacto=datos_contacto+"/"+archivo_contacto+"\n" #este salto de linea se aplica de verdad?
            print("busco esto: " + busqueda_contacto)
            indice_contacto=lines.index(busqueda_contacto)
            print(indice_contacto)
            lines[indice_contacto]=name+"," +nombre_usuario + "," + correo + "," + pagina_web+"/"+archivo_contacto+"\n"
        
        with open("contactos.txt", "w") as contactos_edit:
            for i in lines:
                contactos_edit.write(i)
    
        with open(archivo_contacto, "w") as archivoEditado:
            
            archivoEditado.write(name +"," +nombre_usuario + "," + correo + "," + pagina_web)#quiero escribir lo que haya actualmente en el entry no?
        
        messagebox.showinfo("Editado", "Contacto editado con éxito")    
    else:
        messagebox.showinfo("ERROR", "El correo debe contener un '@")

   



def buscarContactoEdit():
    contacto=contact.get() #para buscar por el nombre
    print(contacto)
    ##LEER EL ARCHIVO CONTACTOS###
    archivo_contactos=open("contactos.txt", "r")
    for linea in archivo_contactos: #esto me lee cada linea del archivo
        if contacto in linea: #como hago para que deje de leer las siguientes lineas si ya ha encontrado el nombre?
            datos_contacto, archivo_contacto=linea.strip().split("/")
            print("Lo he encontrado")
            print(archivo_contacto) 
            editarContacto(archivo_contacto, datos_contacto) #solo si existe el contacto quiero que me lo edite
    archivo_contactos.close()    
    
def buscarContactoElim():
    contacto=contact.get() #para buscar por el nombre
    print(contacto)
    ##LEER EL ARCHIVO CONTACTOS###
    archivo_contactos=open("contactos.txt", "r")
    for linea in archivo_contactos: #esto me lee cada linea del archivo
        if contacto in linea: #como hago para que deje de leer las siguientes lineas si ya ha encontrado el nombre?
            datos_contacto, archivo_contacto=linea.strip().split("/")
            print("Lo he encontrado")
            print(archivo_contacto) 
            eliminarContacto(archivo_contacto, datos_contacto) #solo si existe el contacto quiero que me lo edite
    archivo_contactos.close()    

    


root=Tk() #creamos la ventana principal, por convención se llama root
root.geometry(SIZE) #redimensionamos la ventana
root.title("Agenda de usuarios")  #añadimos un titulo a la ventana
# root.iconbitmap('E:\\ARCHIVOS\\Desktop\\Proyecto-final-agenda-usuarios\\agenda-contactos\\img\\contact.ico')
#cuando alguien se lo descargue va a dar error porque no tinenen la misma url

###CREAMOS LAS VARIABLES###
nombre=StringVar()
username=StringVar()
email=StringVar()
paginaWeb=StringVar()
contact=StringVar()


###CREAMOS LAS ETIQUETAS###

tituloEtiqueta=Label(root,text="AGENDA DE USUARIOS",font=(FONT_STYLE, FONT_SIZE, FONT_WEIGHT), fg=BG_BUTTON)
tituloEtiqueta.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

nombreEtiqueta=Label(root,text="Nombre", font=(FONT_STYLE,FONT_SIZE_LABEL),fg=LETTER_COLOR)
nombreEtiqueta.grid(row=1, column=0, padx=20, pady=10)

usernameEtiqueta=Label(root, text="Username",font=(FONT_STYLE,FONT_SIZE_LABEL), fg=LETTER_COLOR)
usernameEtiqueta.grid(row=2, column=0, padx=20, pady=10)

emailEtiqueta=Label(root, text="Email",font=(FONT_STYLE,FONT_SIZE_LABEL), fg=LETTER_COLOR)
emailEtiqueta.grid(row=3, column=0, padx=20, pady=10)


paginaWebEtiqueta=Label(root, text="Pagina Web",font=(FONT_STYLE,FONT_SIZE_LABEL), fg=LETTER_COLOR)
paginaWebEtiqueta.grid(row=4, column=0, padx=20, pady=10)

buscarContactoEtiqueta=Label(root, text="Buscar contacto por nombre",font=(FONT_STYLE,FONT_SIZE_LABEL), fg=LETTER_COLOR)
buscarContactoEtiqueta.grid(row=7, column=1, padx=20, pady=10)

###tkinter.messagebox.showinfo("titulo", "texto")



###CREAMOS LAS ENTRADAS###

nombreEntrada=Entry(root, textvariable=nombre, font=(FONT_STYLE, 15))
nombreEntrada.grid(row=1, column=1, ipadx=100, ipady=5, columnspan=2)

usernameEntrada=Entry(root, textvariable=username, font=(FONT_STYLE, 15))
usernameEntrada.grid(row=2, column=1, ipadx=100, ipady=5, columnspan=2)

emailEntrada=Entry(root, textvariable=email, font=(FONT_STYLE, 15))
emailEntrada.grid(row=3, column=1, ipadx=100, ipady=5, columnspan=2)

paginaWebEntrada=Entry(root, textvariable=paginaWeb, font=(FONT_STYLE, 15))
paginaWebEntrada.grid(row=4, column=1, ipadx=100, ipady=5, columnspan=2)

contactoBuscado=Entry(root, textvariable=contact, font=(FONT_STYLE, 15))
contactoBuscado.grid(row=8, column=1, ipadx=100, ipady=5, columnspan=2)


###CREAMOS LOS BOTONES###
botonGuardar=Button(root, text="GUARDAR CONTACTO", font=(FONT_STYLE,15, FONT_WEIGHT),fg=LETTER_BUTTON, bg=BG_BUTTON, command=guardarContacto)
botonEliminar=Button(root, text="ELIMINAR CONTACTO",font=(FONT_STYLE,15, FONT_WEIGHT), fg=LETTER_BUTTON, bg=BG_BUTTON, command=buscarContactoElim)
botonGuardar.grid(row=2, column=3, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
botonAgenda=Button(root,text="VER AGENDA", font=(FONT_STYLE,15, FONT_WEIGHT),fg=LETTER_BUTTON, bg=BG_BUTTON, command=consultarAgenda)
botonAgenda.grid(row=3, column=3, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
botonEliminar.grid(row=10, column=1, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
botonEditar=Button(root, text="EDITAR CONTACTO", font=(FONT_STYLE,15, FONT_WEIGHT),fg=LETTER_BUTTON, bg=BG_BUTTON, command=buscarContactoEdit)
botonEditar.grid(row=9, column=1, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)

root.mainloop() #va a registrar todo lo que ocurre mientras la ventana está abierta