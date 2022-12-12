from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from properties import *
from os import remove
import re


# ###CREAMOS LAS FUNCIONES QUE VAMOS A NECESITAR###

lista_usuarios=[] #defino una lista vacia donde se van a ir guardando los usuarios cada vez que abramos la interfaz

def validarCorreo(arg_email):
    is_valid=True
    EMAIL_REGEX=re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    is_valid=False if not EMAIL_REGEX.match(arg_email) else True
    return is_valid

def mostrarInstrucciones():
    instrucciones=messagebox.showinfo("Instrucciones de uso", "Hola! Soy tu agenda y quiero que aprendas a usarme correctamente :D. EDITAR CONTACTO: si quieres editar un contacto tienes que introducir su nombre en 'Buscar contacto por su nombre' y rellenar todos los campos del contacto con los cambios que quieras, eso sí, dale al botón de 'Editar Contacto' ÚNICAMENTE después de haber realizado esto. ELIMINAR CONTACTO: para eliminar un contacto debes introducir su nombre en 'Buscar contacto por su nombre' y darle al botón de 'Eliminar Contacto'. Eso es todo!! Gracias y espero que te sea útil <3 ")


def consultarAgenda():
    #crear una nueva ventana
    newWindow=Toplevel()
    newWindow.geometry(SIZE_SECOND_WD)
    newWindow.title("Consulta de Usarios")

    ##CREO EL ESTILO QUE QUIERO APLICAR###
    style = ttk.Style()
    style.configure("mystyle1.Treeview", highlightthickness=1, rowheight=40, bd=0, font=('Georgia', 12)) #modifico el cuerpo de treeview
    style.configure("mystyle1.Treeview.Heading", font=('Calibri', 15,'bold'),foreground=BG_BUTTON) #modifico el heading
    style.layout("mystyle1.Treeview", [('mystyle1.Treeview.treearea', {'sticky': 'nswe'})]) #quito los bordes

    tv=ttk.Treeview(newWindow,style="mystyle1.Treeview", columns=("Nombre", "Username", "Correo electrónico", "Página Web")) #el nombre de la columna se refiere no solo al encabezado, sino a todos los datos de esa columna
    
    ###CENTRO LOS DATOS DE CADA COLUMNA##
    tv.column("#0", width=80, anchor=CENTER)
    tv.column("Nombre", width=80, anchor=CENTER)
    tv.column("Username", width=80, anchor=CENTER)
    tv.column("Correo electrónico", width=80, anchor=CENTER)
    tv.column("Página Web", width=80, anchor=CENTER)
    tv.pack(fill=BOTH, expand=True)
    
    tv.tag_configure("row", background=BACKGROUND_COLOR, font=("Georgia",10))

    ##encabezados##
    tv.heading("#0", text="Archivo", anchor=CENTER)
    tv.heading("Nombre", text="Nombre", anchor=CENTER)
    tv.heading("Username", text="Username", anchor=CENTER)
    tv.heading("Correo electrónico", text="Correo electrónico", anchor=CENTER)
    tv.heading("Página Web", text="Página Web", anchor=CENTER)

    '''
    Para insertar los datos recolecto éstos del archivo contactos.txt. Leo cada línea, que tiene los datos de cada contacto. Separo cada dato y lo almaceno en una variable cada uno. Inserto cada variable en la tabla.
    Cuando un contacto se ha eliminado queda una linea vacia en contactos.txt. Si leyendo las lineas se encuentra unicamente "\n" no quiero que me lo añada, sino que siga leyendo.
    '''

    with open("contactos.txt", "r") as verContactos:
        for linea in verContactos:        
            linea_nueva=linea.replace('/', ',') #para separar el nombre del archivo cambio / por una ,
            if linea=="":
                continue #no quiero que haga nada
            else:
                nombreE, usernameE,correoE,paginaWebE, archivoE=linea_nueva.strip().split(",")
                tv.insert("", END,tags="row", text=archivoE, values=(nombreE,usernameE,correoE,paginaWebE))
            

    mainloop()

def eliminarContacto():
   '''
    Mismo procedimiento que para editar un contacto, solo que en la lista en vez de enviar los nuevos datos, lo sustituimos por "\n" para que al escribirlo en el archivo no se muestre
   '''
   contacto=buscarContacto()#buscamos contacto y obtenemos una tupla
   datos_contacto, archivo_contacto=contacto #separamos cada elemento de la tupla y lo almacenamos en estas variables
   
   
   with open("contactos.txt", "r") as contactos:
        lines=contactos.readlines()
        busqueda_contacto=datos_contacto+"/"+archivo_contacto+"\n"
        indice_contacto=lines.index(busqueda_contacto)
        lines[indice_contacto]="" #lo dejo vacio para que el contacto se borre en la linea correspondiente
    
   with open("contactos.txt", "w") as contactos_edit:
        for i in lines:
            contactos_edit.write(i)
        
    ##ARCHIVO INDIVIDUAL##
   remove(archivo_contacto) #así me borra el archivo del directorio

   messagebox.showinfo("Eliminado", "Contacto eliminado con éxito")  #muestro un mensaje cuando el contacto se ha eliminado con éxito


def archivarContacto():
    '''
    Para poder almacenar cada contacto en un archivo diferente con el formato: "user_.txt" cambiando el _ por el número que corresponda, creo un archivo "suma.txt" que va a almacenar un número, a partir del 1, y se la va a ir sumando 1 cada vez que un contacto se haya guardado. El nº que esté almacenado en ese archivo será el correspondiente al que va en el nombre del archivo individual de ese contacto.
    '''
    ###ABRO EL ARCHIVO SUMA PARA EXTRAER EL NÚMERO###
        #manualmente lo inicializo con un 1
    with open("suma.txt", "r") as archivo_suma:
        num=archivo_suma.read()

    ###NOMBRO EL ARCHIVO CON ESE NÚMERO###
    nombreArchivo= "user"+ str(num)+ ".txt" #formato de cada archivo

    ###SOBREESCRIBO EN EL ARCHIVO EL NÚMERO SUMÁNDOLE 1###
    with open("suma.txt", "w") as numeroActualizado:
        num=int(num)+1
        numeroActualizado.write(str(num))
 
    ###CREO UN ARCHIVO CON EL NOMBRE ACTUALIZADO Y GUARDO LOS DATOS###
    contacto_nuevo=lista_usuarios[-1]

    with open(nombreArchivo, 'w') as user: 
        ###AÑADO AL ARCHIVO CREADO UNICAMENTE EL ÚLTIMO ELEMENTO DE LA LISTA, QUE ES EL NUEVO CONTACTO AGREGADO###
        user.write(contacto_nuevo)
    
    ##GUARDO ESE CONTACTO EN EL ARCHIVO CONTACTOS.TXT, QUE ALMANCENARÁ TODOS LOS CONTACTOS DE LA AGENDA###
    with open("contactos.txt", "a") as contacto: #no quiero sobreeescribir sino añadir abajo, así que escribo con "a"
        contacto.write(contacto_nuevo +"/" + nombreArchivo + "\n")
    
        

def guardarContacto():

    ###CON LOS GETS SACO EL VALOR DE LAS VARIABLES###
    name=nombre.get()
    nombre_usuario=username.get()
    correo=email.get()
    pagina_web=paginaWeb.get()

    check=validarCorreo(correo)

    if check==True: #validar el correo
        lista_usuarios.append(name+"," +nombre_usuario + "," + correo + "," + pagina_web) # la lista me sirve para añadir contactos a contactos.txt, pero se borra cuando cierro la app, asi que debo almacenar los contactos en txt
        archivarContacto()
        messagebox.showinfo("Guardado", "Contacto guardado con éxito")
    else:
        messagebox.showinfo("ERROR", "El correo electrónico no cumple con el formato. Revisalo por favor")



def editarContacto():
    '''
    Primero buscamos el contacto con la función buscarContacto(). Separamos la tupla que obtenemos en dos variables para almacenar los datos del contacto y el nombre del archivo de manera separada. Obtenemos los nuevos valores de los campos del contacto con el get. Solo si hay un "@" en el correo puedo editar el contacto. 
    Para editar el contacto abrimos el archivo contactos. txt, leemos cada linea y almacenamos ésto en una variable llamada "lines", que es de tipo lista. Creo una variable "busqueda_contacto" que será el contacto que buscamos y unimos los datos con el formato correspondiente para poder encontrarla en "lines". Creo una variable "indice_contacto" que buscará en "lines" el índice donde se encunetra "busqueda_contacto".
    Con este índice ya podemos cambiar en el lugar correspondiente los valores del contacto con los nuevos datos. 

    Una vez esos valores se han escrito en la lista, abro el archivo contactos.txt para sobreescribir y por cada elemento de lines escribo en el archivo, con las modificaciones en el contacto ya hechas.
    '''

    contacto=buscarContacto() #buscamos contacto y obtenemos una tupla
    datos_contacto, archivo_contacto=contacto #separamos cada elemento de la tupla y lo almacenamos en estas variables

    ###CON LOS GETS SACO EL VALOR DE LAS VARIABLES###
    name=nombre.get()
    nombre_usuario=username.get()
    correo=email.get()
    pagina_web=paginaWeb.get()

    check=validarCorreo(correo)


    if check ==True:
        
        with open("contactos.txt", "r") as contactos:
            lines=contactos.readlines() #obtengo una lista
            busqueda_contacto=datos_contacto+"/"+archivo_contacto+"\n" #escribimos el contato con el formato de los contactos en la lista
            indice_contacto=lines.index(busqueda_contacto) #busco el indice en la lista para este contacto
            lines[indice_contacto]=name+"," +nombre_usuario + "," + correo + "," + pagina_web+"/"+archivo_contacto+"\n" #modifico en ese indice los valores del contacto
        
        with open("contactos.txt", "w") as contactos_edit:
            for i in lines: #escribo para cada elemento de la lista en el archivo
                contactos_edit.write(i)
    
        with open(archivo_contacto, "w") as archivoEditado: #modifico el archivo indivual sobreescribiendo únicamente
            
            archivoEditado.write(name +"," +nombre_usuario + "," + correo + "," + pagina_web)
        
        messagebox.showinfo("Editado", "Contacto editado con éxito")    #muestro un mensaje cuando se ha editado correctamente
    else:
        messagebox.showinfo("ERROR", "El correo electrónico no cumple con el formato. Revisalo por favor") #muestro el error sino se puede editar

    
def buscarContacto():
    '''
    Para editar o eliminar un contacto tenemos que comprobar que existe buscandolo. Creo una variable contacto que va a recibir el valor que el usuario busca por la interfaz. Abrimos el archivo contactos.txt y buscamos en cada linea por el nombre. Solo si existe, es decir, si el contacto está en alguna línea, vamos a separar en dos variables los datos. En una guardamos los datos del contacto y en otro el nombre del archivo en el que están guardados. Hacemos un return con esas variables para usarlas en la función de editar o eliminar un contacto.
    '''
    contacto=contact.get() #para buscar por el nombre
    ##LEER EL ARCHIVO CONTACTOS###
    archivo_contactos=open("contactos.txt", "r")
    for linea in archivo_contactos: #esto me lee cada linea del archivo
        if contacto in linea:
            datos_contacto, archivo_contacto=linea.strip().split("/")
            return datos_contacto, archivo_contacto
    archivo_contactos.close()

root=Tk() #creamos la ventana principal, por convención se llama root
root.geometry(SIZE) #redimensionamos la ventana
root.title("Agenda de usuarios")  #añadimos un titulo a la ventana

##CREAMOS LAS VARIABLES###
nombre=StringVar()
username=StringVar()
email=StringVar()
paginaWeb=StringVar()
contact=StringVar()


##CREAMOS LAS ETIQUETAS###

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
botonEliminar=Button(root, text="ELIMINAR CONTACTO",font=(FONT_STYLE,15, FONT_WEIGHT), fg=LETTER_BUTTON, bg=BG_BUTTON, command=eliminarContacto)
botonGuardar.grid(row=2, column=4, ipadx=5, ipady=5, padx=25, pady=10, columnspan=2)
botonAgenda=Button(root,text="      VER AGENDA      ", font=(FONT_STYLE,15, FONT_WEIGHT),fg=LETTER_BUTTON, bg=BG_BUTTON, command=consultarAgenda)
botonAgenda.grid(row=3, column=4, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
botonEliminar.grid(row=10, column=1, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
botonEditar=Button(root, text="EDITAR CONTACTO", font=(FONT_STYLE,15, FONT_WEIGHT),fg=LETTER_BUTTON, bg=BG_BUTTON, command=editarContacto)
botonEditar.grid(row=9, column=1, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)
botonInstrucciones=Button(root, text="INSTRUCCIONES", font=(FONT_STYLE,15, FONT_WEIGHT),fg=LETTER_BUTTON, bg=BG_BUTTON, command=mostrarInstrucciones)
botonInstrucciones.grid(row=4,column=4, ipadx=5, ipady=5, padx=10, pady=10, columnspan=2)

root.mainloop() #va a registrar todo lo que ocurre mientras la ventana está abierta