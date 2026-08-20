# run: python chi_square_uniform_test.py

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

n_samples = 10000
n_bins = 10

data = np.random.uniform(0, 1, n_samples)

observed, bin_edges = np.histogram(data, bins=n_bins, range=(0, 1))
expected = np.full(n_bins, n_samples / n_bins)

chi2_stat = np.sum((observed - expected) ** 2 / expected)
dof = n_bins - 1
p_value = 1 - stats.chi2.cdf(chi2_stat, dof)

print(f"Chi-square statistic = {chi2_stat:.4f}")
print(f"Degrees of freedom   = {dof}")
print(f"p-value              = {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Result: Reject H0 -> data does NOT look uniform")
else:
    print("Result: Fail to reject H0 -> data looks uniform")

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].bar(bin_edges[:-1], observed, width=1 / n_bins, align="edge",
           edgecolor="black", label="Observed")
axs[0].axhline(expected[0], color="red", linestyle="--", label="Expected")
axs[0].set_xlabel("Value")
axs[0].set_ylabel("Frequency")
axs[0].set_title("Observed vs Expected Frequencies")
axs[0].legend()

x = np.linspace(0, chi2_stat * 1.5, 500)
axs[1].plot(x, stats.chi2.pdf(x, dof), color="blue", label=f"Chi2 dist (dof={dof})")
axs[1].axvline(chi2_stat, color="red", linestyle="--", label=f"Chi2 stat = {chi2_stat:.2f}")
axs[1].set_xlabel("Chi-square value")
axs[1].set_ylabel("Density")
axs[1].set_title("Chi-Square Distribution")
axs[1].legend()

plt.tight_layout()
plt.show()
