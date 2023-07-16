import tkinter as tk
from tkinter import ttk

from itertools import count
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os, signal

plt.style.use('fivethirtyeight')

plt.style.use('fivethirtyeight')
plt.figure(figsize=(6, 4))
# values for first graph
x_vals = [0]
y_vals = [0]
# values for second graph
y_vals2 = [0]
SR = 100

if_start = False
if_firstStart = False



def animate(i):
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
    if(len(x_vals) > 10):
        ax1.set_xlim(x_vals[-10], x_vals[-1])
        ax1.set_ylim(0, 5)
        ax1.plot(x_vals, y_vals)
        
        ax2.set_xlim(x_vals[-10], x_vals[-1])
        ax2.plot(x_vals, y_vals2)
       
    else:
        ax1.set_xlim(x_vals[-1], x_vals[-1]  + 10)
        ax1.set_xlim(0, 9)
        ax1.plot(x_vals, y_vals)
        
        ax2.set_xlim(0, 9)
        ax2.plot(x_vals, y_vals2)


def Inicia_obtencion():
    global if_start
    global if_firstStart
    

    
    if (if_firstStart):
        
        if_firstStart = False
        return
    if_start = not if_start
    if (if_start):
        ani.event_source.start()
    else:
        ani.event_source.stop()
    print("Inicia")


def Guarda_datos():
    print("Guarda")

#Main Window
window = tk.Tk()
window.title('Monitor')
window.geometry('600x600')

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
frame_Pseniales.pack_propagate(False)
frame_Pseniales.pack(side='left')

canvas = FigureCanvasTkAgg(plt.gcf(), master=frame_Pseniales)
canvas.get_tk_widget().grid(column=0, row=1)
# Create two subplots in row 1 and column 1, 2

plt.gcf().subplots(2, 1)
ani = FuncAnimation(plt.gcf(), animate, interval=1000/SR, blit=False, save_count=10)
ani.event_source.stop() 

#Parámetros Numéricos
frame_Pseniales = ttk.Frame(window, width=600, height=200, borderwidth=10, relief=tk.GROOVE )
                                                                #(FLAT, RAISED, SUNKEN, GROOVE
frame_Pseniales.pack_propagate(False)
frame_Pseniales.pack(side='top')

if __tjinyrt__ == "__main__":

    window.mainloop()
    try:
        window.P.kill()
    except:
        pass
    try:
        window.L.kill()
    except:
        pass
    PID = os.getpid()
    os.kill(PID, signal.SIGKILL) 