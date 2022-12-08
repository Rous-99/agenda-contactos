from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from properties import *
from os import remove
import agenda
###CREAMOS LAS FUNCIONES QUE VAMOS A NECESITAR###

lista_usuarios=[] #defino una lista vacia donde se van a ir guardando los usuarios


def consultarAgenda():
    #crear una nueva ventana
    newWindow=Toplevel()
    newWindow.geometry(SIZE_SECOND_WD)
    newWindow.title("Consulta de Usarios")

    ##CREO EL ESTILO QUE QUIERO APLICAR###
    style = ttk.Style()
    style.configure("mystyle1.Treeview", highlightthickness=1, rowheight=40, bd=0, font=('Georgia', 12)) # Modify the font of the body
    style.configure("mystyle1.Treeview.Heading", font=('Calibri', 15,'bold'),foreground=BG_BUTTON) # Modify the font of the headings
    style.layout("mystyle1.Treeview", [('mystyle1.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


    tv=ttk.Treeview(newWindow,style="mystyle1.Treeview", columns=("Nombre", "Username", "Correo electrónico", "Página Web")) #el nombre de la columna se refiere no solo al encabezado, sino a todos los datos de esa columna
    tv.column("#0", width=80)
    tv.column("Nombre", width=80, anchor=CENTER)
    tv.pack(fill=BOTH, expand=True)
    
    tv.tag_configure("prueba", background=BACKGROUND_COLOR, font=("Georgia",10))


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
                tv.insert("", END,tags="prueba", text=archivoE, values=(nombreE,usernameE,correoE,paginaWebE))
            
           
        
    


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
    name=agenda.nombre.get()
    nombre_usuario=agenda.username.get()
    correo=agenda.email.get()
    pagina_web=agenda.paginaWeb.get()

    if "@" in correo: #validar el correo, si tiene "@"
        lista_usuarios.append(name+"," +nombre_usuario + "," + correo + "," + pagina_web) #separo con $ para visualizar mejor la lista, la lista me sirve para añadir contactos a contactos.txt, pero se borra cuando cierro la app, asi que debo almacenar los contactos en txt
        archivarContacto()
        messagebox.showinfo("Guardado", "Contacto guardado con éxito")
    else:
        messagebox.showinfo("ERROR", "El correo electrónico debe contener un '@'")



        


def editarContacto(archivo_contacto, datos_contacto):
    # #   ###CON LOS GETS SACO EL VALOR DE LAS VARIABLES###
    name=agenda.nombre.get()
    nombre_usuario=agenda.username.get()
    correo=agenda.email.get()
    pagina_web=agenda.paginaWeb.get()

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
    contacto=agenda.contact.get() #para buscar por el nombre
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
    contacto=agenda.contact.get() #para buscar por el nombre
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