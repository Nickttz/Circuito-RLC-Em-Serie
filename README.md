# Análise de Circuito RLC em Série

Este projeto considera um circuito RLC em série ligado a uma fonte de tensão dada por:

### &epsilon;(𝑡) = &epsilon;<sub>𝑚𝑎𝑥</sub> sin(𝜔𝑡)

## Dados do Circuito

- **Resistência:** R = 3,0 × 102 Ω
- **Indutância:** L = 50 H
- **Capacitância:** C = 2,0 × 10<sup>−4</sup> F
- **Tensão Máxima:** &epsilon;<sub>𝑚𝑎𝑥</sub> = 15 V
- **Frequência Angular:** 𝜔 = 25 s<sup>−1</sup>

### Condições Iniciais

- **Carga Inicial:** q(𝑡 = 0) = 0
- **Corrente Inicial:** i(𝑡 = 0) = 0

## Tecnologias Utilizadas

- Python
- NumPy
- Matplotlib
- SciPy

## Instalação

Para rodar o código, você precisará ter o Python instalado em seu computador. Você pode instalar as bibliotecas necessárias usando `pip`:

```bash
pip install numpy matplotlib scipy
```

## Problemas

### Solução da EDO e Gráfico da Tensão no Resistor

O objetivo é escrever um programa em Python que resolva a equação diferencial ordinária (EDO) e plote o gráfico da tensão no resistor em função do tempo.

# Gráfico

![Circuito RLC](Imagem.jpg)

