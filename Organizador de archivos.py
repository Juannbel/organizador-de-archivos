import os
import shutil
from tkinter import Tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from tkinter import messagebox as MessageBox
import time

raiz = Tk()
raiz.geometry("400x150")
raiz.configure(bg="#FFFFFF")
raiz.resizable(0,0)
raiz.title("Organizador")
#seleccionar la carpeta que queremos organizar con el programa
def seleccionador():
	carpeta = askdirectory()
	carpeta = carpeta.replace("/", "\\")
	camino.set(carpeta)


#crear las carpetas donde se organizaran los archivos
#antes de crearlas se comprueba si esta carpeta ya existe
#esto en caso de que el programa se vaya a usar mas de una vez
def organizar():
	ruta = camino.get()
	if ruta == "":
		MessageBox.showwarning("Error", "No selecciono ninguna carpeta")
	else:
		carpetas = ["Videos", "Imagenes", "Documentos", "Comprimidos", "Ejecutables", "Otros", "Audios"]
		for i in carpetas:
			if os.path.exists(ruta + "\\" + i) == False:
				os.mkdir(ruta + "\\" + i)

		#se obtienen los nombres de los archivos que se encuentran en la carpeta especificada
		archivos = os.listdir(ruta)

		#se definen los tipos de archivo por extension
		imagenes = ('.jpg', '.png', '.jpeg', '.ico', '.webp')
		videos = ('.avi', '.mp4', '.mkv', '.mov', '.flv')
		documentos = ('.odt', '.pdf', '.PDF', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.ppsx', '.csv', '.potx', '.xlsx', '.pptx', '.odp', '.ods')
		comprimidos = ('.zip', '.rar', '.rar5', ".7z")
		ejecutables = ('.exe', '.msi', '.appimage', '.deb')
		audios = ('.mp3', '.mid', 'wav', 'aac', 'flac', 'ogg', '.m4a', '.opus')

		#se recorre cada archivo, y dependiendo de su extension se organiza en la carpeta correspondiente
		for i in archivos:
			if os.path.isfile(ruta + "\\" + i):
				if (i.lower()).endswith(imagenes):
					shutil.move(ruta + "\\" +i, ruta + "\\Imagenes")
					continue
				elif (i.lower()).endswith(documentos):
					shutil.move(ruta + "\\" +i, ruta + "\\Documentos")
					continue
				elif (i.lower()).endswith(videos):
					shutil.move(ruta + "\\" +i, ruta + "\\Videos")
					continue
				elif (i.lower()).endswith(comprimidos):
					shutil.move(ruta + "\\" +i, ruta + "\\Comprimidos")
					continue
				elif (i.lower()).endswith(ejecutables):
					shutil.move(ruta + "\\" +i, ruta + "\\Ejecutables")
					continue
				elif (i.lower()).endswith(audios):
					shutil.move(ruta + "\\" +i, ruta + "\\Audios")
					continue
				else:
					shutil.move(ruta + "\\" +i, ruta + "\\Otros")
			else:
				continue

		#se verifica que las carpetas creadas contengan algun archivo
		#si la carpeta no contiene ningun archivo se elimina para no tener exceso de carpetas
		for carpeta in carpetas:
			directorio = ruta + "\\" + carpeta
		if os.listdir(directorio) == []:
			shutil.rmtree(directorio)
			MessageBox.showinfo("Info", "Carpeta organizada")

def desorganizar():
	ruta = camino.get()
	if ruta == "":
		MessageBox.showwarning("Error", "No selecciono ninguna carpeta")
	else:
		contenido = os.listdir(ruta)

		for i in contenido:
			if os.path.isdir(ruta + "\\" + i):
				directorio = ruta + "\\" + i
				carpeta = os.listdir(directorio)
				for x in carpeta:
					shutil.move(directorio + "\\" + x, ruta)
				shutil.rmtree(directorio)
		MessageBox.showinfo("Info", "Carpeta desorganizada")


camino = StringVar()
boton = Button(raiz, text="Seleccionar carpeta", command=seleccionador)
boton.place(x=270, y=16)
seleccionada = Entry(raiz,width=40,textvariable=camino, bg="#E9EDF8")
seleccionada.place(x=10, y=20)
boton_organizar = Button(raiz, text="Organizar", command=organizar, height=1)
boton_organizar.place(x=60, y=60)
boton_desorganizar = Button(raiz, text="Desorganizar", command=desorganizar, height=1)
boton_desorganizar.place(x=150, y=60)
raiz.mainloop()