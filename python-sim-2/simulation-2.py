import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters 
P0 = 200         
r = 0.4          
t0, tf = 0, 9    

# Exact analytical solution
t_exact = np.linspace(t0, tf, 400)
P_exact = P0 * np.exp(r * t_exact)

# Time steps for Euler’s method
h_values = [0.5, 0.1]
t_arrays = [np.arange(t0, tf + h, h) for h in h_values]

# Euler approximations
P_euler = []
for t_vals, h in zip(t_arrays, h_values):
    P_vals = np.zeros(len(t_vals))
    P_vals[0] = P0
    for i in range(1, len(t_vals)):
        P_vals[i] = P_vals[i-1] + h * r * P_vals[i-1]
    P_euler.append(P_vals)


fig, ax = plt.subplots(figsize=(9, 6))
ax.set_xlim(t0, tf)
ax.set_ylim(0, max(P_exact) * 1.1)
ax.set_xlabel("Time (t) in seconds")
ax.set_ylabel("Population P(t)")
ax.set_title("")
ax.grid(True, linestyle='--', alpha=0.6)

# Plot initial empty lines
(line_exact,) = ax.plot([], [], 'k-', linewidth=2.5, label="Exact Solution")
(line_h05,) = ax.plot([], [], 'b--', linewidth=2, label="0.5s")
(line_h01,) = ax.plot([], [], 'm--', linewidth=2, label="0.1s")

# Text labels that move with the lines
label_exact = ax.text(0, 0, '', color='black', fontsize=10, weight='bold')
label_h05 = ax.text(0, 0, '', color='blue', fontsize=9, weight='bold')
label_h01 = ax.text(0, 0, '', color='purple', fontsize=9, weight='bold')

ax.legend(loc="upper left")

# Animation Function
def update(frame):
   
    frac = frame / len(t_exact)

    # Exact solution 
    n_exact = int(frac * len(t_exact))
    line_exact.set_data(t_exact[:n_exact], P_exact[:n_exact])
    if n_exact > 0:
        label_exact.set_position((t_exact[n_exact-1], P_exact[n_exact-1]))
        label_exact.set_text(f"Exact: {P_exact[n_exact-1]:.0f}")

    # 0.5
    n_h05 = int(frac * len(t_arrays[0]))
    line_h05.set_data(t_arrays[0][:n_h05], P_euler[0][:n_h05])
    if n_h05 > 0:
        label_h05.set_position((t_arrays[0][n_h05-1], P_euler[0][n_h05-1]))
        label_h05.set_text(f"0.5s: {P_euler[0][n_h05-1]:.0f}")

    # 0.1
    n_h01 = int(frac * len(t_arrays[1]))
    line_h01.set_data(t_arrays[1][:n_h01], P_euler[1][:n_h01])
    if n_h01 > 0:
        label_h01.set_position((t_arrays[1][n_h01-1], P_euler[1][n_h01-1]))
        label_h01.set_text(f"0.1s: {P_euler[1][n_h01-1]:.0f}")

    return line_exact, line_h05, line_h01, label_exact, label_h05, label_h01


ani = FuncAnimation(
    fig, update, frames=len(t_exact),
    interval=35, blit=True, repeat=True
)

plt.show()
