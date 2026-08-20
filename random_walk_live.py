import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("2D Random Walk — Live Animation")


n_steps = st.slider("Number of steps", min_value=10, max_value=1000, value=200, step=10)
speed = st.slider("Animation speed (delay per step, seconds)", 0.0, 0.2, 0.02, step=0.01)
seed = st.number_input("Random seed (optional, 0 = random)", min_value=0, value=0)

start = st.button("Start Walk")

plot_spot = st.empty()      # placeholder for the live-updating plot
status_spot = st.empty()    # placeholder for live status text

if start:
    if seed != 0:
        np.random.seed(seed)

    x, y = [0], [0]

    for i in range(n_steps):
        dx, dy = [(1, 0), (-1, 0), (0, 1), (0, -1)][np.random.choice(4)]

        x.append(x[-1] + dx)
        y.append(y[-1] + dy)

        
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(x, y, linewidth=1, alpha=0.8, color="steelblue")
        ax.scatter(x[0], y[0], color="green", label="Start", zorder=5)
        ax.scatter(x[-1], y[-1], color="red", label="Current", zorder=5)
        ax.set_xlim(min(x) - 5, max(x) + 5)
        ax.set_ylim(min(y) - 5, max(y) + 5)
        ax.set_aspect("equal")
        ax.set_title(f"Step {i+1} / {n_steps}")
        ax.legend(loc="upper left")

        plot_spot.pyplot(fig)
        plt.close(fig)  

        distance = np.sqrt(x[-1] ** 2 + y[-1] ** 2)
        status_spot.write(f"**Step {i+1}** — Position: ({x[-1]:.2f}, {y[-1]:.2f}) — Distance from origin: {distance:.2f}")

        time.sleep(speed)

    st.success("Walk complete!")
else:
    st.info("Adjust settings and click 'Start Walk' to watch it move live.")

# streamlit run random_walk_live.py