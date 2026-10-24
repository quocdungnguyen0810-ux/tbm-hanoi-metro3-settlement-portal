"""Surrogate AI Module for Fast Settlement Prediction (Pure NumPy implementation).

Trained on Peck analytical simulation grid.
Flag: qa_flag: surrogate_trained_on_peck_analytical_grid.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt
import numpy as np
from scripts.analytical_engine import PeckModel

OUT_DIR = ROOT / "research_outputs" / "2026-10-13_152753"
DATA_DIR = OUT_DIR / "03_processed_data"
FIG_DIR = OUT_DIR / "05_figures"
TABLE_DIR = OUT_DIR / "06_tables"


class LightweightMLP:
    """A self-contained 2-hidden-layer neural network with Adam optimizer."""

    def __init__(self, in_dim=5, h1=32, h2=16, out_dim=1):
        np.random.seed(42)
        self.W1 = np.random.randn(in_dim, h1) * np.sqrt(2.0 / in_dim)
        self.b1 = np.zeros((1, h1))
        self.W2 = np.random.randn(h1, h2) * np.sqrt(2.0 / h1)
        self.b2 = np.zeros((1, h2))
        self.W3 = np.random.randn(h2, out_dim) * np.sqrt(2.0 / h2)
        self.b3 = np.zeros((1, out_dim))

    def relu(self, z):
        return np.maximum(0, z)

    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.relu(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.relu(self.z2)
        self.out = np.dot(self.a2, self.W3) + self.b3
        return self.out

    def fit(self, X, y, epochs=120, lr=0.008, batch_size=64):
        # Adam optimizer parameters
        mW1, vW1 = np.zeros_like(self.W1), np.zeros_like(self.W1)
        mb1, vb1 = np.zeros_like(self.b1), np.zeros_like(self.b1)
        mW2, vW2 = np.zeros_like(self.W2), np.zeros_like(self.W2)
        mb2, vb2 = np.zeros_like(self.b2), np.zeros_like(self.b2)
        mW3, vW3 = np.zeros_like(self.W3), np.zeros_like(self.W3)
        mb3, vb3 = np.zeros_like(self.b3), np.zeros_like(self.b3)
        
        beta1, beta2, eps = 0.9, 0.999, 1e-8
        t_step = 0
        n = X.shape[0]

        for epoch in range(epochs):
            indices = np.random.permutation(n)
            X_shuffled = X[indices]
            y_shuffled = y[indices]

            for start in range(0, n, batch_size):
                t_step += 1
                end = min(start + batch_size, n)
                xb = X_shuffled[start:end]
                yb = y_shuffled[start:end]

                # Forward
                pred = self.forward(xb)
                error = pred - yb
                m = xb.shape[0]

                # Backprop
                grad_W3 = np.dot(self.a2.T, error) / m
                grad_b3 = np.sum(error, axis=0, keepdims=True) / m

                da2 = np.dot(error, self.W3.T)
                dz2 = da2 * (self.z2 > 0)
                grad_W2 = np.dot(self.a1.T, dz2) / m
                grad_b2 = np.sum(dz2, axis=0, keepdims=True) / m

                da1 = np.dot(dz2, self.W2.T)
                dz1 = da1 * (self.z1 > 0)
                grad_W1 = np.dot(xb.T, dz1) / m
                grad_b1 = np.sum(dz1, axis=0, keepdims=True) / m

                # Adam updates
                for p, gp, mp, vp in [
                    (self.W3, grad_W3, mW3, vW3), (self.b3, grad_b3, mb3, vb3),
                    (self.W2, grad_W2, mW2, vW2), (self.b2, grad_b2, mb2, vb2),
                    (self.W1, grad_W1, mW1, vW1), (self.b1, grad_b1, mb1, vb1)
                ]:
                    mp[:] = beta1 * mp + (1 - beta1) * gp
                    vp[:] = beta2 * vp + (1 - beta2) * (gp ** 2)
                    m_hat = mp / (1 - beta1 ** t_step)
                    v_hat = vp / (1 - beta2 ** t_step)
                    p -= lr * m_hat / (np.sqrt(v_hat) + eps)


def generate_dataset(n_samples=2500):
    np.random.seed(101)
    D = 6.30
    z0 = np.random.uniform(14.0, 20.0, n_samples)
    K = np.random.uniform(0.40, 0.65, n_samples)
    VL = np.random.uniform(0.005, 0.020, n_samples)
    x = np.random.uniform(-35.0, 35.0, n_samples)

    y = np.zeros(n_samples)
    for i in range(n_samples):
        model = PeckModel(D, z0[i], K[i], VL[i])
        y[i] = model.settlement(x[i]) * 1000.0  # mm

    X = np.stack([z0, K, VL * 100.0, x, np.abs(x)], axis=1)
    return X, y.reshape(-1, 1)


def train_and_evaluate():
    X, y = generate_dataset(2500)
    
    # Train / Test split 80/20
    split = 2000
    X_train, y_train = X[:split], y[:split]
    X_test, y_test = X[split:], y[split:]

    # Normalization
    x_mean = np.mean(X_train, axis=0)
    x_std = np.std(X_train, axis=0) + 1e-8
    y_mean = np.mean(y_train)
    y_std = np.std(y_train) + 1e-8

    X_train_norm = (X_train - x_mean) / x_std
    y_train_norm = (y_train - y_mean) / y_std
    X_test_norm = (X_test - x_mean) / x_std

    model = LightweightMLP(in_dim=5, h1=32, h2=16, out_dim=1)
    model.fit(X_train_norm, y_train_norm, epochs=150, lr=0.01)

    # Predict
    pred_norm = model.forward(X_test_norm)
    y_pred = pred_norm * y_std + y_mean

    # Evaluation metrics
    mae = float(np.mean(np.abs(y_pred - y_test)))
    rmse = float(np.sqrt(np.mean((y_pred - y_test) ** 2)))
    ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)
    ss_res = np.sum((y_test - y_pred) ** 2)
    r2 = float(1.0 - (ss_res / ss_tot))

    results = {
        "model_type": "Surrogate_MLP_Neural_Network",
        "qa_flag": "surrogate_trained_on_peck_analytical_grid",
        "training_samples": split,
        "test_samples": len(y_test),
        "R2_score": round(r2, 4),
        "MAE_mm": round(mae, 3),
        "RMSE_mm": round(rmse, 3),
        "status": "VALIDATED" if r2 >= 0.99 else "MARGINAL"
    }

    report_path = TABLE_DIR / "ai_surrogate_evaluation.json"
    report_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Surrogate AI evaluation: R2={r2:.4f}, MAE={mae:.3f} mm, RMSE={rmse:.3f} mm")

    # Plot Accuracy Scatter Plot
    plt.figure(figsize=(6, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='#1e3c72', s=20, label=f'Test Data (R² = {r2:.4f})')
    min_val = min(float(np.min(y_test)), float(np.min(y_pred)))
    max_val = max(float(np.max(y_test)), float(np.max(y_pred)))
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Fit 1:1')
    plt.title("Surrogate AI Model Accuracy (Analytical vs AI Predicted)", fontsize=11, fontweight='bold')
    plt.xlabel("Analytical True Settlement (mm)", fontsize=10)
    plt.ylabel("Surrogate AI Predicted Settlement (mm)", fontsize=10)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    fig_path = FIG_DIR / "ai_surrogate_accuracy.png"
    plt.savefig(fig_path, dpi=300)
    plt.close()
    print(f"Saved accuracy plot: {fig_path.name}")
    return results


if __name__ == "__main__":
    train_and_evaluate()
