import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class Animation:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.xdata, self.ydata = [], []

        plt.style.use('dark_background')

        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(min(x), max(x)), ylim=(min(y), max(self.y)))
        self.line, = self.ax.plot([], [], lw=2)

        # Заголовок анимации
        plt.title('Мяч в стакане')
        # Скрываем лишние данные

        self.anim = FuncAnimation(self.fig, self.animate, init_func=self.init_func,
                                  frames=len(self.x), interval=20, blit=True)

    def init_func(self):
        self.line.set_data([], [])
        return self.line,

        # функция анимации

    def animate(self, i):
        x, y = self.x[i], self.y[i]
        self.xdata.append(x)
        self.ydata.append(y)
        self.line.set_data(self.xdata, self.ydata)
        return self.line,

    def save(self):
        self.anim.save('coil.gif', writer='imagemagick')
