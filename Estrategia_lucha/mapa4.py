import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuración de la figura
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')
ax.set_xlim(0, 140)
ax.set_ylim(0, 100)
ax.axis('off')

# Dibujar el contorno del gran salón (paredes exteriores)
salon = patches.Rectangle((10, 10), 120, 80, linewidth=2, edgecolor='black', facecolor='#f5f5f5')
ax.add_patch(salon)

# Dibujar obstáculos internos: columnas derrumbadas y escombros
# Columnas caídas (círculos representando columnas derrumbadas)
columnas = [(30, 70), (110, 70), (30, 30), (110, 30)]
for (x, y) in columnas:
    columna = patches.Circle((x, y), 7, linewidth=2, edgecolor='black', facecolor='#d1c4e9')
    ax.add_patch(columna)
    ax.text(x, y, "Columna", ha='center', va='center', fontsize=7, color='black')

# Escombros: rectángulos que indican áreas de cobertura o barreras
escombro1 = patches.Rectangle((60, 55), 20, 8, linewidth=2, edgecolor='black', facecolor='#ffe082', alpha=0.8)
ax.add_patch(escombro1)
ax.text(70, 59, "Escombro", ha='center', va='center', fontsize=7, color='black')

escombro2 = patches.Rectangle((60, 30), 25, 8, linewidth=2, edgecolor='black', facecolor='#ffe082', alpha=0.8)
ax.add_patch(escombro2)
ax.text(72.5, 34, "Escombro", ha='center', va='center', fontsize=7, color='black')

# Plataforma elevada: una zona que ofrece ventaja para ataques a distancia
plataforma = patches.Rectangle((90, 80), 20, 8, linewidth=2, edgecolor='black', facecolor='#a5d6a7', alpha=0.8)
ax.add_patch(plataforma)
ax.text(100, 84, "Plataforma", ha='center', va='center', fontsize=7, color='black')

# Líneas para representar muros derrumbados o separaciones internas
ax.plot([10, 130], [50, 50], linestyle='--', color='gray', linewidth=1)
ax.plot([70, 70], [10, 90], linestyle='--', color='gray', linewidth=1)

# Posiciones iniciales de los enemigos (círculos rojos)
enemies = [(20, 80), (40, 80), (20, 40), (40, 40), (120, 80), (120, 40)]
for (x, y) in enemies:
    enemy = patches.Circle((x, y), 4, linewidth=2, edgecolor='darkred', facecolor='#ff8a80')
    ax.add_patch(enemy)
    ax.text(x, y, "Enemigo", ha='center', va='center', fontsize=6, color='black')

# Título del mapa
plt.title("Mapa del Gran Salón - Encuentro 4: El Duelo Táctico", fontsize=16)

plt.show()
