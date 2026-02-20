import numpy as np

# Constantes Físicas
g = 9.81  # Gravidade (m/s^2)
rho = 1.225  # Densidade do ar (kg/m^3)
Cd = 0.47  # Coeficiente de arrasto (esfera)

def calcular_velocidade_terminal(m, A):
    """Calcula a velocidade terminal de um objeto em queda."""
    v_terminal = np.sqrt((2 * m * g) / (rho * A * Cd))
    return v_terminal

print(f"Velocidade Terminal: {calcular_velocidade_terminal(70, 0.5):.2f} m/s")
