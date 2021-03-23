class Glass:
    def __init__(self, lb_x=0, lb_y=0, rt_x=50, rt_y=100):
        self.lb_x = lb_x
        self.lb_y = lb_y
        self.rt_x = rt_x
        self.rt_y = rt_y


class BallMovement:
    def __init__(self, x_0=1.0, y_0=1.0, vx_0=1.0, vy_0=1.0, m=1.0, alpha=0.001, glass=Glass()):
        self.x_0 = x_0
        self.y_0 = y_0

        self.vx_0 = vx_0
        self.vy_0 = vy_0

        self.m = m
        self.alpha = alpha
        self._movement = []

        self.glass = glass

    def input(self):
        print("Input:")
        while True:
            try:
                self.x_0 = float(input("\tx_0 = "))
                self.y_0 = float(input("\ty_0 = "))

                self.vx_0 = float(input("\tvx_0 = "))
                self.vy_0 = float(input("\tvy_0 = "))
            except ValueError:
                print("Введенное значение не является числом. Попробуйте еще раз!")
            else:
                print('Success!')
                break

    # function_x
    def f_x(self, x_i, vx_i, t_i):
        return -self.alpha * self.vx_0

    # function_y
    def f_y(self, y_i, vy_i, t_i):
        return -self.alpha * self.vy_0 - 9.8 * self.m

    # просчитывание движений
    def move(self, t_start=None, t_end=None, dt=None):
        # задаем начальные значения
        t_i = t_start
        x_i, y_i = self.x_0, self.y_0
        vx_i, vy_i = self.vx_0, self.vy_0

        # схема Эйлера
        # print('t_i | x_i | y_i | vx_i | vy_i')
        inside = True
        while t_i <= t_end:
            x_temp = x_i + dt * vx_i
            y_temp = y_i + dt * vy_i

            vx_temp = vx_i + dt / self.m * self.f_x(x_i, vx_i, t_i)
            vy_temp = vy_i + dt / self.m * self.f_y(y_i, vy_i, t_i)

            if y_temp < self.glass.lb_y:
                vy_temp = -(vy_temp / 1.5)
                y_temp = self.glass.lb_y

            if x_temp > self.glass.rt_x and y_temp < self.glass.rt_y and inside:
                vx_temp = -(vx_temp / 1.5)
                x_temp = self.glass.rt_x

            if x_temp < self.glass.lb_x and y_temp < self.glass.rt_y and inside:
                vx_temp = -(vx_temp / 1.5)
                x_temp = self.glass.lb_x

            if (x_temp > self.glass.rt_x or x_temp < self.glass.lb_x) and y_temp > self.glass.rt_y:
                inside = False

            data = [t_i, x_i, y_i, vx_i, vy_i]
            self._movement.append(data)
            # print(data)

            # reload
            x_i, y_i = x_temp, y_temp
            vx_i, vy_i = vx_temp, vy_temp
            t_i += dt
        return self._movement

    def write(self, filename="data.txt"):
        with open(filename, 'w') as file:
            for data in self._movement:
                t, x, y, vx, vy = data
                file.write(f"{t} {x} {y} {vx} {vy}" + "\n")
        print(f'{filename} успешно записан!')
