#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import openpyxl
import matplotlib.pyplot as grafico
from modos import partida_modosolitario, partida_dos_jugadores, estadistica
from estadisticas import solucion, nivel_dificultad

def menu():
    #Cargamos el archivo
    archivo=("C:\\Users\\celia\\Desktop\\MASTER DATA SCIENCE\\Programacion basica\\TAREA CELIA\\datos_estadisticas.xlsx")
    #Cargamos el libro
    libro=openpyxl.load_workbook(archivo)

    #Nos aseguramos que el individuo introduzca una opcion valida
    while True:
        print("Menu principal \n 1.Modo Solitario \n 2.Modo dos jugadores \n 3.Estadistica \n 4.Salir")
        
        #Pedimos al jugador que elija una opcion
        opcion=int(input("Elige una opcion entre 1 y 4:"))
        if opcion==1:
            partida_modosolitario()
        elif opcion==2:
            partida_dos_jugadores()
        elif opcion==3:
            estadistica(libro)
        elif opcion==4:
            print("Salir")
            break
        else:
            print("Opcion no valida, por favor introduce un numero entre 1 y 4:")
menu()


# In[ ]:




