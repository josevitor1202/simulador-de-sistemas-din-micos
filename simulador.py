import numpy as np
import matplotlib.pyplot as plt

# Constantes Físicas
g = 9.81      # Gravidade (m/s^2)
rho = 1.225   # Densidade do ar (kg/m^3)
Cd = 0.47     # Coeficiente de arrasto (esfera)
A = 0.1       # Área da seção transversal (m^2)

def calcular_velocidade_terminal(m):
    return np.sqrt((2 * m * g) / (rho * A * Cd))

# Intervalo de massas: de 1kg até 100kg
massas = np.linspace(1, 100, 50)
velocidades = calcular_velocidade_terminal(massas)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(massas, velocidades, color='blue', linewidth=2, label='Velocidade Terminal')
plt.title('Influência da Massa na Velocidade Terminal', fontsize=14)
plt.xlabel('Massa (kg)', fontsize=12)
plt.ylabel('Velocidade Terminal (m/s)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

print("Simulação concluída. Gráfico gerado!")
