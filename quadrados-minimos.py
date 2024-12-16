import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Dados
x = np.array([0, 0.5, 1, 2.5, 3])
V = np.array([2.0, 2.6, 3.7, 13.2, 21.0])

# Função modelo
def V_model(x, a, b):
    return 1 + a * np.exp(b * x)

# Ajuste de curva
params, covariance = curve_fit(V_model, x, V, p0=[1, 1])

# Parâmetros ajustados
a_fit, b_fit = params

# Valores ajustados
V_fit = V_model(x, a_fit, b_fit)

# Visualização
plt.scatter(x, V, label="Dados observados", color="red")
plt.plot(x, V_fit, label=f"Ajuste: V(x) = 1 + {a_fit:.4f}e^({b_fit:.4f}x)", color="blue")
plt.xlabel("x")
plt.ylabel("V(x)")
plt.title("Ajuste de Curva")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

a_fit, b_fit
