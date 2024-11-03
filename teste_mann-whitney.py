# pacotes utilizados
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import shapiro
import matplotlib.pyplot as plt
import seaborn as sns

#%% ATEC
controle_pre = [116, 89]
controle_pos = [85, 81]
placebo_pre = [152, 103]
placebo_pos = [147, 97]

# Calcular as diferenças
dif_controle = np.array(controle_pos) - np.array(controle_pre)
dif_placebo = np.array(placebo_pos) - np.array(placebo_pre)

# Teste de Mann-Whitney
stat, p_value = stats.mannwhitneyu(dif_controle, dif_placebo, alternative='less')
print(f'Estatística U: {stat}, p-valor bicaudal: {p_value}')

# Configurando a distribuição teórica para o teste de Mann-Whitney
n1 = len(dif_controle)
n2 = len(dif_placebo)
u1 = stat  # Estatística U do teste
u2 = n1 * n2 - u1  # Estatística U do grupo placebo

# Gerando valores da curva normal aproximada
mean_u = (n1 * n2) / 2
std_u = np.sqrt((n1 * n2 * (n1 + n2 + 1)) / 12)

# Gerando valores da curva normal
x = np.linspace(mean_u - 4 * std_u, mean_u + 4 * std_u, 1000)
y = stats.norm.pdf(x, mean_u, std_u)

# Definindo os valores críticos bicaudais (com nível de significância 0,05)
alpha = 0.05
critical_value_lower = stats.norm.ppf(alpha / 2, mean_u, std_u)  # Crítico inferior
critical_value_upper = stats.norm.ppf(1 - alpha / 2, mean_u, std_u)  # Crítico superior

# Exportando para Excel
proba_atec = pd.DataFrame({'valores U': x, 
                           'density proba': y})

#proba_atec.to_excel('atec_proba.xlsx', index=False)

# Gráfico da curva de distribuição com linha do valor crítico bicaudal e valor do teste U
plt.figure(figsize=(10, 6))
sns.set_style('darkgrid')
plt.plot(x, y, color="navy")
plt.axvline(critical_value_lower, color='red', linestyle='--', label=f"Valor crítico inferior (5%) = {critical_value_lower:.2f}")
plt.axvline(critical_value_upper, color='red', linestyle='--', label=f"Valor crítico superior (5%) = {critical_value_upper:.2f}")
plt.axvline(u1, color='green', linestyle='--', label=f"Valor do teste U = {u1:.2f}")

plt.title("ATEC | Grupo Controle vs Grupo Placebo\nTeste Estatístico de Mann-Whitney\n", 
          weight='bold', size=19)
plt.xlabel("Valores de U", size=14)
plt.ylabel("Densidade de Probabilidade", size=14)
plt.legend(loc='upper right', facecolor='white', fontsize=11.5)
plt.show()


#%% CGI
controle_pre = [16, 22]
controle_pos = [12, 20]
placebo_pre = [16, 27]
placebo_pos = [15, 24]

# Calculando as diferenças
dif_controle = np.array(controle_pos) - np.array(controle_pre)
dif_placebo = np.array(placebo_pos) - np.array(placebo_pre)

# Teste de Mann-Whitney
stat, p_value = stats.mannwhitneyu(dif_controle, dif_placebo, alternative='two-sided')
print(f'Estatística U: {stat}, p-valor bicaudal: {p_value}')

# Configurando a distribuição teórica para o teste de Mann-Whitney
n1 = len(dif_controle)
n2 = len(dif_placebo)
u1 = stat  # Estatística U do teste
u2 = n1 * n2 - u1  # Estatística U do grupo placebo

# Gerarando valores da curva normal aproximada
mean_u = (n1 * n2) / 2
std_u = np.sqrt((n1 * n2 * (n1 + n2 + 1)) / 12)

# Gerando valores da curva normal
x = np.linspace(mean_u - 4 * std_u, mean_u + 4 * std_u, 1000)
y = stats.norm.pdf(x, mean_u, std_u)

# Definindo os valores críticos bicaudais (com nível de significância 0,05)
alpha = 0.05
critical_value_lower = stats.norm.ppf(alpha / 2, mean_u, std_u)  # Crítico inferior
critical_value_upper = stats.norm.ppf(1 - alpha / 2, mean_u, std_u)  # Crítico superior

# Exportando para excel
proba_cgi = pd.DataFrame({'valores U': x, 
                           'density proba': y})
#proba_cgi.to_excel('cgi_proba.xlsx', index=False)

# Gráfico da curva de distribuição com linha do valor crítico bicaudal e valor do teste U
plt.figure(figsize=(10, 6))
sns.set_style('darkgrid')
plt.plot(x, y, color="navy")
plt.axvline(critical_value_lower, color='red', linestyle='--', label=f"Valor crítico inferior (5%) = {critical_value_lower:.2f}")
plt.axvline(critical_value_upper, color='red', linestyle='--', label=f"Valor crítico superior (5%) = {critical_value_upper:.2f}")
plt.axvline(u1, color='green', linestyle='--', label=f"Valor do teste U = {u1:.2f}")

plt.title("CGI | Grupo Controle vs Grupo Placebo\nTeste Estatístico de Mann-Whitney\n", 
          weight='bold', size=19)
plt.xlabel("Valores de U", size=14)
plt.ylabel("Densidade de Probabilidade", size=14)
plt.legend(loc='upper right', facecolor='white', fontsize=11.5)
plt.show()
