# to calculate the value of pi
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(n_points, seed=None):
    rng = np.random.default_rng(seed)
    x = rng.uniform(-1, 1, n_points)
    y = rng.uniform(-1, 1, n_points)

    inside = x**2 + y**2 <= 1
    pi_estimate = 4 * np.sum(inside) / n_points

    return pi_estimate, x, y, inside


if __name__ == "__main__":
    n_points = 100_000
    pi_est, x, y, inside = monte_carlo_pi(n_points, seed=42)

    print(f"Points used     : {n_points}")
    print(f"Estimated pi    : {pi_est:.6f}")
    print(f"Actual pi       : {np.pi:.6f}")
    print(f"Absolute error  : {abs(pi_est - np.pi):.6f}")

    # Plot
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(x[inside], y[inside], s=1, color="tab:blue", label="Inside circle")
    ax.scatter(x[~inside], y[~inside], s=1, color="tab:red", label="Outside circle")
    circle = plt.Circle((0, 0), 1, fill=False, color="black", linewidth=1.5)
    ax.add_patch(circle)
    ax.set_aspect("equal")
    ax.set_title(f"Monte Carlo Estimate of π ≈ {pi_est:.5f}")
    ax.legend(loc="upper right")
    plt.savefig("monte_carlo_pi.png", dpi=150)
    plt.show()