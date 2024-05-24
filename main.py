import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Количество частиц
N = 10

# Инициализация частиц в случайных позициях и со случайными скоростями
x = np.random.rand(N)
y = np.random.rand(N)
vx = np.random.randn(N) * 0.01
vy = np.random.randn(N) * 0.01

# Заряды частиц
charges = np.random.choice([-1, 1], N)

# Коэффициент замедления
slowdown = 0.25

# Создание фигуры и осей
fig, ax = plt.subplots()
particles, = ax.plot(x, y, 'bo')

# Определение функции для обновления позиций и скоростей частиц
def update(frame):
    global x, y, vx, vy

    for i in range(N):
        for j in range(i+1, N):
            dx = x[j] - x[i]
            dy = y[j] - y[i]
            r = np.hypot(dx, dy)
            f = charges[i] * charges[j] / r**2  # Закон Кулона
            fx = f * dx / r
            fy = f * dy / r
            vx[i] += slowdown * fx
            vy[i] += slowdown * fy
            vx[j] -= slowdown * fx
            vy[j] -= slowdown * fy

    # Обновление позиций
    x += vx
    y += vy

    # Отражение от стенок
    vx = np.where((x<0) | (x>1), -vx, vx)
    vy = np.where((y<0) | (y>1), -vy, vy)

    # Обновление позиций частиц на графике
    particles.set_xdata(x)
    particles.set_ydata(y)

    return particles,

# Создание анимации
ani = animation.FuncAnimation(fig, update, frames=100, interval=100)

plt.show()
