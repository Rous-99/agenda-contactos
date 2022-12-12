# Agenda de Contactos (python + tkinter)
Con esta aplicación podremos tener una agenda completamente funcional en la que agregar, editar o eliminar contactos, además de poder visualizar todos sus datos a través de una interfaz gráfica o a través de sus archivos txt correspondientes.

## Instalación Tkinter
Para poder realizar esta agenda usé la librería Tkinter, la cuál hay que tener instalada para poder hacer uso de esta aplicación. 
Para instalarla nos vamos a la CMD y agregamos el siguiente comando: pip install tk. En principio con esto bastaría para instarlar la librería de manera funcional.

## Uso

Al colocar en la terminal el comando "python agenda.py" se ejecturá el programa, siempre y cuando estemos colocados previamente en la carpeta agenda-contactos.
En la ventana principal apreciaremos varios botones y unas campos de entrada. 

-GUARDAR CONTACTO: para guardar algún contacto solo tendremos que rellenar los campos (Nombre, Username, Eail y Pagina Web) y darle al botón "Guardar Contacto". Recuerda colocar el formato de correo electrónico valido, comprobando que tenga un @ en el sitio correspondiente, y un . seguido de algúna extensión de correo electrónico.

-VER AGENDA: una vez ya hayamos agregado algún contacto podremos hacer uso del botón "Ver Agenda". Se abrirá una ventana en la que saldrá la información de cada contacto agregado con sus datos correspondientes.

-EDITAR CONTACTO: para editar un contacto debemos rellenar los campos (Nombre, Username, Email y Página Web), sin dejar ninguno vacío, manteniéndo los datos que no queremos cambiar del contacto a editar y los cambios que queremos agregar. Seguidamente colocamos el nombre en la entrada "Buscar contacto por nombre" y ÚNICAMENTE después de realizar todo ésto clickamos en el botón "Editar contacto". Si pulsamos en "Ver Agenda" ya se podrán apreciar los cambios en el contacto específicado.

-ELIMINAR CONTACTO: para eliminar un contacto únicamente tendremos que colocar el nombre del contacto a eliminar en el buscador "Buscar contacto por nombre" y clickar en el botón "Eliminar contacto". Si abrimos la agenda nuevamente podremos apreciar que ese contacto ya no aparecerá como registrado y sus datos se habrán eliminado.


En el caso de que la agenda ya se haya utilizado y deseemos resetearla para comenzar de nuevo, solo tendremos que borrar los contactos almacenados en "contactos.txt" y quedarnos en la línea 1. Además, habrá que resetear el número del archivo "suma.txt" y dejarlo en 1. Los archivos individuales de cada contacto habrá que eliminarlos, para que la agenda se pueda utilizar como si fuese nueva.
