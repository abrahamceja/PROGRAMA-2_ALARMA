from tkinter import*
import time
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from pygame import mixer

root = Tk()
root.title("ALARM")
root.geometry('230x400')

datohora=StringVar()
datominuto=StringVar()
#H=StringVar()
#M=StringVar()
#x=BooleanVar()

pygame.init()
mixer.init()

def Setalarma():
    global datohora,datominuto,horas,minutos
    datoalarma=datohora.get() + ":" + datominuto.get() + ":" + "00"
    horaalarma.config(text=datoalarma)
    global cancion
    #cancion = filedialog.askopenfile() 
    #print(cancion)
    #pygame.mixer.music.load(cancion)
    
def Stopalarma():
    datoalarma="00:00:00"
    horaalarma.config(text=datoalarma)
    mixer.music.stop()
    root.config(bg="white")
    horaalarma.config(bg="white")
    labelalarma.config(bg="white")
    titulo.config(bg="white")
    tituloH.config(bg="white")
    tituloM.config(bg="white")
    tituloReloj.config(bg="white")
    mietiqueta.config(bg="white")

def clock():
    global datohora,datominuto,horas,minutos
    horas=time.strftime("%H")
    minutos=time.strftime("%M")
    segundos=time.strftime("%S")
    horalocal= horas + ":" + minutos +":" + segundos
    mietiqueta.config(text=horalocal)
    mietiqueta.after(1000,clock)
    #print(datohora.get()==horas)
    #print(datominuto.get()==minutos)
    if datohora.get()==horas and datominuto.get()==minutos and "00"==segundos:
        cancion="journey dont stop believin.mp3"
        mixer.music.load(cancion)
        mixer.music.play()
        root.config(bg="red")
        horaalarma.config(bg="red")
        labelalarma.config(bg="red")
        titulo.config(bg="red")
        tituloH.config(bg="red")
        tituloM.config(bg="red")
        tituloReloj.config(bg="red")
        mietiqueta.config(bg="red")

mietiqueta=Label(root,text="",font=("Roboto",20))
mietiqueta.grid(row=5,column=2,padx=10,pady=10)
clock()    

horaalarma=Label(root,text="00:00:00", font=("Roboto",20))
horaalarma.grid(row=7,column=2,padx=10,pady=10)
labelalarma=Label(root,text="Alarma :", font=("Roboto",10))
labelalarma.grid(row=7,column=1,sticky=E)
titulo=Label(root,text="ALARMA",font=("Roboto",10))
titulo.grid(row=1,column=2,padx=10,pady=10)
tituloH=Label(root,text="Horas :",font=("Roboto",10))
tituloH.grid(row=2,column=1,sticky=E)
tituloM=Label(root,text="Minutos :",font=("Roboto",10))
tituloM.grid(row=3,column=1,sticky=E)
tituloReloj=Label(root,text="RELOJ",font=("Roboto",10))
tituloReloj.grid(row=4,column=2,padx=10,pady=10)

SetHora=Entry(root,textvariable=datohora).grid(row=2,column=2,columnspan=3)
SetMinuto=Entry(root,textvariable=datominuto).grid(row=3,column=2,columnspan=3)

BotonSetAlarma=Button(root, text="SET ALARMA", bg="#ffA420",font=("Roboto", 8, "bold"),fg="Black",width=13,height=1,command=Setalarma)
BotonSetAlarma.grid(row=6,column=2,padx=10,pady=10)

BotonstopAlarma=Button(root, text="STOP SONG", bg="#ffA420",font=("Roboto", 8, "bold"),fg="Black",width=13,height=1,command=Stopalarma)
BotonstopAlarma.grid(row=8,column=2,padx=10,pady=10)

root.mainloop()