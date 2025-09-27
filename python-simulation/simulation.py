import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

y0 = 4.20    
v0 = 1.50    
g = 9.81     

coeffs = [-0.5*g, v0, y0]
roots = np.roots(coeffs)
t_max = max(roots) 

dt = 0.20 
t_table = np.arange(0, t_max + dt, dt)


dt_anim = 0.02
t_fine = np.arange(0, t_max + dt_anim, dt_anim)

def y(t): return y0 + v0*t - 0.5*g*t**2
def v(t): return v0 - g*t

# Plot setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

line1, = ax1.plot([], [], 'b-', lw=2, label="y(t)")
point1, = ax1.plot([], [], 'ro')
ax1.set_xlim(0, t_max)
ax1.set_ylim(0, max(y(t_fine)) + 1)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Position y(t) (m)')
ax1.legend()
ax1.grid()

line2, = ax2.plot([], [], 'g-', lw=2, label="v(t)")
point2, = ax2.plot([], [], 'ro')
ax2.set_xlim(0, t_max)
ax2.set_ylim(min(v(t_fine)) - 1, max(v(t_fine)) + 1)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity v(t) (m/s)')
ax2.legend()
ax2.grid()

def init():
    line1.set_data([], [])
    point1.set_data([], [])
    line2.set_data([], [])
    point2.set_data([], [])
    return line1, point1, line2, point2

# Update animation
def update(frame):
    t_data = t_fine[:frame+1]
    y_data = y(t_data)
    v_data = v(t_data)

    line1.set_data(t_data, y_data)
    point1.set_data([t_data[-1]], [y_data[-1]])

    line2.set_data(t_data, v_data)
    point2.set_data([t_data[-1]], [v_data[-1]])

    return line1, point1, line2, point2

ani = FuncAnimation(fig, update, frames=len(t_fine), init_func=init,
                    blit=False, interval=30, repeat=True)

plt.tight_layout()
plt.show()
