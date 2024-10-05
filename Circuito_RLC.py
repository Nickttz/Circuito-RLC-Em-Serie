import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parâmetros do circuito
R = 3.0e2
L = 50.0
C = 2.0e-4
epsilon_max = 15.0
omega = 25.0

# Condições iniciais
q0 = 0.0
i0 = 0.0

# Definindo a EDO
def circuito_RLC(y, t):
    q, i = y
    dqdt = i
    didt = (epsilon_max * np.sin(omega * t) - R*i - q/L) / L
    return [dqdt, didt]

# Tempo de simulação
tempo = np.linspace(0, 6, 5000)  # 6 segundos para visualização

# Resolvendo a EDO
solucao = odeint(circuito_RLC, [q0, i0], tempo)

# Extraindo a corrente no resistor
tensao_resistor = R * solucao[:, 1]

# Definindo o tempo em que o regime estacionário começa
tempo_fim_regime_transiente = 1.37

# Encontrando o índice correspondente ao tempo de fim do regime transiente
indice_inicio_regime_estacionario = np.argmax(tempo > tempo_fim_regime_transiente)

# Calculando o valor máximo da tensão no regime estacionário
steady_state_voltage = np.max(tensao_resistor[indice_inicio_regime_estacionario:])

# Construindo o gráfico com marcadores
fig, ax = plt.subplots()
linha, = ax.plot(tempo, tensao_resistor, label='Tensão no Resistor', color='b')

# Adicionando uma reta horizontal no ponto máximo
ax.axhline(y=steady_state_voltage, color='r', linestyle='--', label='Máximo no Regime Estacionário: 3.50V')

# Adicionando reta vertical para indicar fim do regime transiente
ax.axvline(x=tempo[indice_inicio_regime_estacionario], color='g', linestyle='--', label='Fim do Regime Transiente: 1.37s')

plt.title('Tensão no Resistor em Função do Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão no Resistor (V)')
plt.legend()
plt.grid(True)
plt.show()