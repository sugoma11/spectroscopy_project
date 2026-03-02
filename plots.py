import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

def plot_metrics(y_target, y_pred, name):
    r2 = r2_score(y_target, y_pred)

    rmse = np.sqrt(mean_squared_error(y_target, y_pred))
    rpd = np.std(y_target) / rmse
    bias = np.mean(y_pred - y_target)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(y_target, y_pred, alpha=0.6, edgecolors="steelblue", facecolors="lightskyblue", linewidths=0.8, s=40)
    ax.plot([y_target.min(), y_target.max()], [y_target.min(), y_target.max()], "r--", lw=1.5, label="1:1 line")
    ax.set_xlabel("Measured", fontsize=12)
    ax.set_ylabel("Predicted", fontsize=12)
    ax.set_title(name, fontsize=13, fontweight="bold")

    textstr = f"R² = {r2:.3f}\nRMSE = {rmse:.3f}\nRPD = {rpd:.2f}\nBias = {bias:.3f}"
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=11,
            verticalalignment="top", bbox=dict(boxstyle="round,pad=0.4", facecolor="wheat", alpha=0.8))

    ax.legend(loc="lower right")
    ax.set_aspect("equal", adjustable="datalim")
    fig.tight_layout()
    fig.savefig(f"figures/{name}.png", dpi=150, bbox_inches="tight")
    plt.show()