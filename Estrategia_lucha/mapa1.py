import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuración de la figura
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('equal')
ax.set_xlim(0, 100)
ax.set_ylim(0, 80)
ax.axis('off')

# Dibujar el contorno del vestíbulo (paredes)
vestibulo = patches.Rectangle((5, 5), 90, 70, linewidth=2, edgecolor='black', facecolor='#f5f5f5')
ax.add_patch(vestibulo)

# Dibujar la entrada principal (en la parte superior central)
entrada = patches.Rectangle((42.5, 70), 15, 5, linewidth=2, edgecolor='black', facecolor='#a2d5f2')
ax.add_patch(entrada)
ax.text(50, 72.5, "Entrada", ha='center', va='center', fontsize=10, color='black')

# Dibujar columnas como elementos de cobertura
# Ubicaciones de las columnas
columnas = [(25, 45), (75, 45)]
for (x, y) in columnas:
    columna = patches.Circle((x, y), 5, linewidth=2, edgecolor='black', facecolor='#d1c4e9')
    ax.add_patch(columna)
    ax.text(x, y, "Columna", ha='center', va='center', fontsize=8, color='black')

# Dibujar zonas de escombros (elementos del entorno) con curvas
escombro1 = patches.Arc((50, 30), 30, 15, angle=0, theta1=0, theta2=180, linewidth=2, edgecolor='#ffcc80')
ax.add_patch(escombro1)
ax.text(50, 38, "Escombros", ha='center', va='center', fontsize=8, color='black')

# Dibujar posiciones iniciales de goblins (círculos rojos)
goblins = [(20, 60), (80, 60), (20, 20), (80, 20)]
for (x, y) in goblins:
    goblin = patches.Circle((x, y), 3, linewidth=2, edgecolor='darkred', facecolor='#ff8a80')
    ax.add_patch(goblin)
    ax.text(x, y, "Goblin", ha='center', va='center', fontsize=7, color='black')

# Dibujar líneas para representar muros derrumbados o separaciones
ax.plot([5, 95], [40, 40], linestyle='--', color='gray', linewidth=1)
ax.plot([50, 50], [5, 75], linestyle='--', color='gray', linewidth=1)

# Título del mapa
plt.title("Mapa del Vestíbulo - Encuentro 1", fontsize=14)

plt.show()

