import random
import tkinter as Tk
from itertools import count

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use('fivethirtyeight')
plt.figure(figsize=(6, 3))
# values for first graph
x_vals = [0]
y_vals = [0]
# values for second graph
y_vals2 = [0]



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
       


# GUI
root = Tk.Tk()
label = Tk.Label(root, text="Realtime Animated Graphs").grid(column=0, row=0)

# graph 1
canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
canvas.get_tk_widget().grid(column=0, row=2)
# Create two subplots in row 1 and column 1, 2
plt.gcf().subplots(2, 1)
ani = FuncAnimation(plt.gcf(), animate, interval=1000, blit=False)

Tk.mainloop()