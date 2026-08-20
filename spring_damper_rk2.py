# run: python spring_damper_rk2.py

import numpy as np
import matplotlib.pyplot as plt

m = 1.0
c = 0.5
k = 20.0
x0 = 1.0
v0 = 0.0
t_final = 20.0
dt = 0.01

omega_n = np.sqrt(k / m)
zeta = c / (2 * np.sqrt(k * m))
print(f"omega_n = {omega_n:.4f} rad/s")
print(f"zeta    = {zeta:.4f}")


def deriv(t, s):
    x1, x2 = s
    return np.array([x2, -(c * x2 + k * x1) / m])


n = int(t_final / dt)
t = np.linspace(0, n * dt, n + 1)
s = np.zeros((n + 1, 2))
s[0] = [x0, v0]

for i in range(n):
    k1 = deriv(t[i], s[i])
    k2 = deriv(t[i] + dt, s[i] + dt * k1)
    s[i + 1] = s[i] + (dt / 2) * (k1 + k2)

x = s[:, 0]

plt.plot(t, x)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title(f"Spring-Damper Response (RK2), zeta={zeta:.3f}")
plt.grid(True)
plt.show()