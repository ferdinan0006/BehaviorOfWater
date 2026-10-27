import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# ---------------------------------------------------------
# 1. Daten einlesen
# ---------------------------------------------------------
# Falls du eine echte CSV-Datei (z.B. "messdaten.csv" mit der Spalte "Werte") einlesen willst,
# nutze diese beiden Zeilen (und entferne die Rauten):
# df = pd.read_csv('messdaten.csv')
# daten = df['Werte'].values

# Für dieses Skript verwende ich direkt die 30 Werte aus deinem Bild:
daten = np.array([
    42.9360248, 40.3338415, 46.8392998, 44.8876623, 43.7166798,
    45.5382081, 44.3672256, 45.7984264, 42.9360248, 45.0177714,
    43.5865706, 45.5382081, 43.5865706, 42.5456973, 44.8876623,
    42.2854789, 41.1144965, 44.4973348, 43.8467889, 43.5865706,
    43.8467889, 42.2854789, 42.2854789, 40.2037323, 44.8876623,
    42.4155881, 42.9360248, 44.8876623, 41.3747148, 43.8467889
])

daten11 = np.array([42.58118159,
41.16180887,
44.35539749,
46.12961339,
43.85861704,
44.00055431,
44.35539749,
43.5747425,
41.87149523,
42.0134325,
44.21346022,
43.43280522,
44.28442886,
47.90382929,
42.86505614,
42.36827568,
43.7876484,
44.5683034,
45.27798976,
42.58118159,
43.7876484,
43.5747425,
43.29086795,
44.71024067,
45.41992703,
45.77477021,
48.25867247,
46.05864476,
45.41992703,
45.49089567
])

# 2. Empirische CDF (ECDF) berechnen
# Die Daten werden sortiert und jedem Wert wird ein kumulativer Wahrscheinlichkeitswert zugeordnet.
x_ecdf = np.sort(daten)
y_ecdf = np.arange(1, len(daten) + 1) / len(daten)

x11_ecdf = np.sort(daten11)
y11_ecdf = np.arange(1, len(daten11) + 1) / len(daten11)


# 3. Theoretische Normalverteilung (CDF) berechnen
# Wir berechnen Mittelwert (mu) und Standardabweichung (std) der Stichprobe
mu = np.mean(daten)
std = np.std(daten, ddof=1)

mu11 = np.mean(daten11)
std11 = np.std(daten11, ddof=1)

# Wir erstellen eine glatte Kurve für die x-Achse
x_theoretisch = np.linspace(min(daten) - 1, max(daten) + 1, 100)
# Und berechnen dafür die Werte der perfekten Normalverteilung
y_theoretisch = norm.cdf(x_theoretisch, mu, std)

x_theoretisch11 = np.linspace(min(daten11) - 1, max(daten11) + 1, 100)
y_theoretisch11 = norm.cdf(x_theoretisch11, mu11, std11)

# ---------------------------------------------------------
# 4. Plotten
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))

# Empirische Daten plotten (Treppenfunktion ist typisch für ECDF)
plt.step(x_ecdf, y_ecdf, where='post', label='Empirische CDF (Deine Daten)', color='royalblue', linewidth=2)
plt.step(x11_ecdf, y11_ecdf, where='post', label='Empirische CDF (Daten11)', color='lightgreen', linewidth=2)
# Theoretische Normalverteilungskurve plotten
plt.plot(x_theoretisch, y_theoretisch, label=f'Theoretische Normalverteilung\n(Mittelwert={mu:.2f}, StdAbw={std:.2f})', color='lightblue', linestyle='--', linewidth=2)
plt.plot(x_theoretisch11, y_theoretisch11, label=f'Theoretische Normalverteilung\n(Mittelwert={mu11:.2f}, StdAbw={std11:.2f})', color='darkgreen', linestyle='--', linewidth=2)
# Optik und Beschriftung anpassen
plt.title('Vergleich: Sind die Messdaten normalverteilt?', fontsize=14, pad=15)
plt.xlabel('Messwerte', fontsize=12)
plt.ylabel('Kumulative Wahrscheinlichkeit', fontsize=12)
plt.legend(loc='best', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.7)

# Grenzen für die y-Achse festlegen (0 bis 1)
plt.ylim([0, 1.05])

# Plot anzeigen
plt.tight_layout()
plt.show()