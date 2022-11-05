from tkinter import*

raiz=Tk()
minombre=StringVar()
raiz.geometry("300x350")
miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()
#Labels
labelNombre=Label(miFrame,text="Nombre:")
labelNombre.grid(row=0,column=0,pady=5)

labelApellido=Label(miFrame,text="Apellido:")
labelApellido.grid(row=1,column=0,pady=5)

labelDireccion=Label(miFrame,text="Dirección:")
labelDireccion.grid(row=2,column=0,pady=5)

labelPass=Label(miFrame,text="Password:")
labelPass.grid(row=3,column=0,pady=5)

labelComentarios=Label(miFrame,text="Comentarios:")
labelComentarios.grid(row=4,column=0,pady=5)

#Entry campos de texto
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
   

botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)
botonEnvio.pack()
raiz.mainloop()