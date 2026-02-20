# 🛠️ Applied Physics & Engineering Simulations

Este repositório centraliza o desenvolvimento de modelos matemáticos e simulações computacionais para a resolução de problemas em Física Aplicada e Engenharia. 

O objetivo é transformar conceitos teóricos (Mecânica Clássica, Termodinâmica e Cálculo Diferencial) em ferramentas de análise funcional utilizando **Python**.

## 🔬 Simuladores Inclusos

Atualmente, o projeto conta com os seguintes módulos:

* **Mecânica de Fluidos:** Scripts para cálculo de força de arrasto e velocidade terminal em diferentes meios fluidos.
* **Sistemas Dinâmicos:** Modelagem de equações diferenciais para predição de comportamento de sistemas em equilíbrio e movimento.

## 💻 Tecnologias e Bibliotecas
* **Python 3.10+**
* **NumPy:** Processamento numérico de alta performance.
* **Matplotlib/Seaborn:** Visualização de dados e plotagem de gráficos científicos.

## 📈 Objetivo do Repositório
Este é um projeto contínuo focado em **Engenharia de Performance**. Cada novo script busca otimizar processos de análise que, anteriormente, seriam feitos de forma manual ou puramente analítica.

## 🚀 Experimento 01: Modelagem de Velocidade Terminal

Nesta primeira simulação, explora-se o conceito de **Velocidade Terminal**, que ocorre quando a força de arrasto ($F_d$) de um fluido se iguala à força peso ($P$) de um objeto em queda, resultando em uma aceleração nula e velocidade constante.

A modelagem utiliza a equação:
$$v_t = \sqrt{\frac{2mg}{\rho AC_d}}$$

O script `simulador.py` foi desenvolvido para calcular esse equilíbrio dinâmico variando a massa do objeto, permitindo visualizar como a inércia do corpo influencia o limite de velocidade em um meio viscoso (neste caso, o ar).

### 📊 Resultado da Simulação
Abaixo, o gráfico gerado que apresenta a progressão da velocidade terminal em função do aumento da massa (de 1kg a 100kg), mantendo a área de seção transversal constante:

![Gráfico de Velocidade Terminal](<img width="851" height="549" alt="image" src="https://github.com/user-attachments/assets/d9ab7721-a2c4-4151-b033-3bac4ba6cc34" />
)
