import tkinter as tk
from tkinter import ttk
from itertools import count
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


plt.style.use('fivethirtyeight')

#plt.style.use('dark_background')
#plt.style.use('ggplot')

plt.figure(figsize=(4, 4))
# values for first graph
x_vals = [0]
y_vals = [0]
# values for second graph
y_vals2 = [0]
SR = 25

if_start = False
if_firstStart = True


def animate(i):
    global if_firstStart
    if(if_firstStart):
        return
    # Generate values
    x_vals.append(x_vals[-1] + 1)
    y_vals.append(random.randint(0, 5))
    y_vals2.append(random.randint(0, 10))
    # Get all axes of figure
    ax1, ax2 = plt.gcf().get_axes()
    # Clear current data
    ax1.cla()
    ax2.cla()
    # Plot new data
    tamanioVentana = SR * 2
    
    if(len(x_vals) > tamanioVentana):
        ax1.set_xlim(x_vals[-tamanioVentana], x_vals[-1])
        ax1.set_ylim(0, 5)
        ax1.plot(x_vals, y_vals, 'r')
        
        ax2.set_xlim(x_vals[-tamanioVentana], x_vals[-1])
        ax2.plot(x_vals, y_vals2)
       
    else:
        ax1.set_xlim(0, tamanioVentana)
        ax1.plot(x_vals, y_vals, 'r')
        
        ax2.set_xlim(0, tamanioVentana)
        ax2.plot(x_vals, y_vals2)


def Inicia_obtencion():
    global if_start
    global if_firstStart
    if(if_firstStart):

        if_firstStart = False
    if_start = not if_start
    if (if_start):

        ani.event_source.start()
    else:

        ani.event_source.stop()
    print("Inicia")


def Guarda_datos():
    print("Guarda")

def creaVentanaPrincipal():
    #Main Window
    

    #Datos
    frame_datos = ttk.Frame(window, width=600, height=150, borderwidth=10, relief=tk.GROOVE )
                                                                    #(RIDGE, FLAT, RAISED, SUNKEN, GROOVE
    frame_datos.pack_propagate(True)
    frame_datos.pack(side='top')

    #.......
    frame_ID = ttk.Frame(frame_datos, width=600, height=50, borderwidth=10, relief=tk.FLAT)
    frame_ID.pack_propagate(False)
    frame_ID.pack(side='top')

    IDlabel = ttk.Label(frame_ID, text='ID: ')
    IDlabel.pack(side='left')
    IDentry = ttk.Entry(frame_ID)
    IDentry.pack(side = 'left')

    SaveButton = ttk.Button(frame_ID, text=' Guardar ', command=Guarda_datos)
    SaveButton.pack(side = 'right')

    StartButton = ttk.Button(frame_ID, text='  Inicio  ', command=Inicia_obtencion)
    StartButton.pack(side = 'right')
    #.......

    #.......
    frame_obs = ttk.Frame(frame_datos, width=600, height=50, borderwidth=10)
    frame_obs.pack_propagate(True)
    frame_obs.pack(side='top')

    IDlabel = ttk.Label(frame_obs, text='Observaciones: ')
    IDlabel.pack(side='left')
    IDentry = ttk.Entry(frame_obs, width=400)
    IDentry.pack(side='left')
    #.......

    #Parámetros Señales
    
    frame_Pseniales = ttk.Frame(window, width=600, height=400, borderwidth=10, relief=tk.SUNKEN )
                                                                    #(FLAT, RAISED, SUNKEN, GROOVE
    frame_Pseniales.pack_propagate(True)
    frame_Pseniales.pack(side='top')
    
    #.......
        #.......
    frame_seniales = ttk.Frame(frame_Pseniales, borderwidth=10, relief=tk.FLAT)
    frame_seniales.pack_propagate(True)
    frame_seniales.pack(side='left')

    canvas = FigureCanvasTkAgg(graficas, master=frame_seniales)
    canvas.get_tk_widget().grid(column=0, row=1)
        #.......
        #.......
    frame_valorseniales = ttk.Frame(frame_Pseniales, borderwidth=10, relief=tk.FLAT)
    frame_valorseniales.pack_propagate(True)
    frame_valorseniales.pack(side='left')

    frame_spo2 = ttk.Frame(frame_valorseniales, borderwidth=10, relief=tk.FLAT)
    frame_spo2.pack_propagate(True)
    frame_spo2.pack(side='top')

    Spolabel = ttk.Label(frame_spo2, text='SpO2 %')
    Spolabel.pack(side='left')
        #.......
        #.......
    frame_ppm = ttk.Frame(frame_valorseniales, borderwidth=10, relief=tk.FLAT)
    frame_ppm.pack_propagate(True)
    frame_ppm.pack(side='top')

    ppmlabel = ttk.Label(frame_ppm, text='ppm ')
    ppmlabel.pack(side='left')
        #.......
    #.......

    #IDentry = ttk.Entry(frame_obs, width=400)
    #IDentry.pack(side='left')
    
    #frame_valseniales = ttk.Frame(window, width=600, height=200, borderwidth=10, relief=tk.GROOVE )
                                                                    #(FLAT, RAISED, SUNKEN, GROOVE
    #frame_valseniales.pack_propagate(False)
    #frame_valseniales.pack(side='top')
    
    

def on_closing():
    window.destroy()
    exit()

if __name__  == "__main__":

    #Inicio de gráficas
    if_firstStart = True
    graficas = plt.gcf()
    plt.rcParams.update({'axes.facecolor':'black'})
    graficas.subplots(2, 1)
    ani = FuncAnimation(graficas, animate, interval=1000/SR, blit=False, save_count=10)
    

    #Inicio de la ventana
    window = tk.Tk()
    window.title('Monitor')
    window.geometry('800x800')
    creaVentanaPrincipal()
    window.protocol('WM_DELETE_WINDOW', on_closing)
    window.mainloop()
