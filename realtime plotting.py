import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange

fs = 50

fig = plt.figure(figsize=(6, 3), facecolor = 'black')
x = [0]
y = [0]

count = 0
plt.rcParams.update({'axes.facecolor':'black'})
ln, = plt.plot(x, y, 'r')

plt.axis([0, fs * 5, 0, 10])

def update(frame):
    global count
    x.append(x[-1] + 1)
    y.append(randrange(0, 10))
    if(x[-1] >= fs * 5):
        if(count == fs * 5):
            count = 0
        x[count] = count
        y[count] = randrange(0, 10)

    count = count + 1
    print(count)
    ln.set_data(x, y) 
    return ln,

animation = FuncAnimation(fig, update, interval= 1000/fs)
plt.show()
