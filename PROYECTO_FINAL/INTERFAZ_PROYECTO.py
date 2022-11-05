from cgitb import text
from tkinter import*
from tkinter import font
from tkinter import messagebox
from turtle import bgcolor


raiz=Tk()
## VENTANAS EMERGENTE

def infoAdicional():
    #messagebox.showinfo("INFORMACION","VERSION CODIGO 1.0")
    #messagebox.showwarning("INFORMACION","LICENCIA CADUCADA")
    #messagebox.showerror("INFORMACION","ERROR DE CONEXION")
    #valor=messagebox.askquestion("Atencion", "Desea eliminar una persona")
    valor=messagebox.askokcancel("Atencion", "Desea salir de la aplicacion")

    print(valor)



minombre=StringVar()
raiz.geometry("600x330")
raiz.config(bg="yellow")
miIdentidad=StringVar()
raiz.geometry("600x330")


##MENU
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)

####
menuBd=Menu(barraMenu,tearoff=0)
menuBorrar=Menu(barraMenu,tearoff=0)
menuCrud=Menu(barraMenu,tearoff=0)
menuAyuda=Menu(barraMenu,tearoff=0)



barraMenu.add_cascade(label="BBDD",menu=menuBd)
barraMenu.add_cascade(label="Borrar",menu=menuBorrar)
barraMenu.add_cascade(label="Crud",menu=menuCrud)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)


##menu submenu
menuBd.add_command(label="Conectar")
menuBd.add_command(label="Salir")

##menu submenu
menuCrud.add_command(label="Crear")
menuCrud.add_command(label="Leer")
menuCrud.add_command(label="Actualizar")
menuCrud.add_command(label="Eliminar")

#MABU AYUDA

menuAyuda.add_command(label="Licencia",command=infoAdicional)
menuAyuda.add_command(label="Acerca de.......")
##menu submenu
menuCrud.add_command(label="Licencia")
menuCrud.add_command(label="Acerca de ....")





labelTitulo=Label(raiz,text="Sistema administrador LEYDYCA")
labelTitulo.config(fg="RED",bd=2,font=("Comic Sans Ms bold",12))
labelTitulo.pack()


miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

#Labels
labelID=Label(miFrame,text="ID: ")
labelID.grid(row=0,column=0,pady=5)

labelNombre=Label(miFrame,text="Nombre: ")
labelNombre.grid(row=1,column=0,pady=5)

labelApellido=Label(miFrame,text="Apellido: ")
labelApellido.grid(row=2,column=0,pady=5)

labelDireccion=Label(miFrame,text="Dirección: ")
labelDireccion.grid(row=3,column=0,pady=5)

labelPass=Label(miFrame,text="Password: ")
labelPass.grid(row=4,column=0,pady=5)

labelComentarios=Label(miFrame,text="Comentarios: ")
labelComentarios.grid(row=5,column=0,pady=5)



raiz.iconbitmap("imagen.ico")



#Entry campos de texto
identidad=Entry(miFrame,textvariable=miIdentidad)
identidad.grid(row=0,column=1,pady=5)

nombre=Entry(miFrame,textvariable=minombre)
nombre.grid(row=0,column=1,pady=5)

apellido=Entry(miFrame)
apellido.grid(row=1,column=1,pady=5)

direccion=Entry(miFrame)
direccion.grid(row=2,column=1,pady=5)

parword=Entry(miFrame)
parword.grid(row=3,column=1,pady=5)
parword.config(show="*")

#Area de texto
comentario=Text(miFrame,width=13,height=5)
comentario.grid(row=4,column=1,pady=5)
#Boton
def codigoBoton():
    print(minombre.get())
    minombre.set("Veronica")
   

frame2=Frame()
frame2=Frame(raiz, width=1200,height=600,bg="green")  

frame2.pack()

botonCrear=Button(frame2,text="Crear",command=codigoBoton)
botonCrear.grid(row=0,column=1,padx=5, pady=5)

botonLeer=Button(frame2,text="Leer",command=codigoBoton)
botonLeer.grid(row=0,column=2,padx=5, pady=5)

botonActualizar=Button(frame2,text="Actualizar",command=codigoBoton)
botonActualizar.grid(row=0,column=3,padx=5, pady=5)

botonEliminar=Button(frame2,text="Eliminar",command=codigoBoton)
botonEliminar.grid(row=0,column=4,padx=5, pady=5)



raiz.mainloop()