import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuración de la figura
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')
ax.set_xlim(0, 120)
ax.set_ylim(0, 100)
ax.axis('off')

# Fondo del corredor (paredes y piso)
corridor = patches.Rectangle((10, 10), 100, 80, linewidth=2, edgecolor='black', facecolor='white')
ax.add_patch(corridor)

# Iluminación: Antorchas y sus áreas de luz (círculos translúcidos)
torch_positions = [(20, 80), (60, 80), (100, 80), (20, 40), (60, 40), (100, 40)]
for (x, y) in torch_positions:
    # Área iluminada por la antorcha
    light = patches.Circle((x, y), 10, linewidth=0, facecolor='#ffcc80', alpha=0.3)
    ax.add_patch(light)
    # Representación de la antorcha
    torch = patches.Circle((x, y), 2, linewidth=1, edgecolor='black', facecolor='#ff8a65')
    ax.add_patch(torch)
    ax.text(x, y-3, "Antorcha", ha='center', va='center', fontsize=7, color='white')

# Dibujar las fronteras del corredor
ax.plot([10, 110], [10, 10], color='black', linewidth=2)
ax.plot([10, 110], [90, 90], color='black', linewidth=2)
ax.plot([10, 10], [10, 90], color='black', linewidth=2)
ax.plot([110, 110], [10, 90], color='black', linewidth=2)

# Zonas de sombra (áreas oscuras donde se ocultan los espectros)
shadow1 = patches.Rectangle((30, 65), 15, 10, linewidth=1, edgecolor='black', facecolor='#212121', alpha=0.7)
ax.add_patch(shadow1)
ax.text(37.5, 70, "Sombra", ha='center', va='center', fontsize=7, color='white')

shadow2 = patches.Rectangle((70, 65), 15, 10, linewidth=1, edgecolor='black', facecolor='#212121', alpha=0.7)
ax.add_patch(shadow2)
ax.text(77.5, 70, "Sombra", ha='center', va='center', fontsize=7, color='white')

shadow3 = patches.Rectangle((50, 30), 20, 10, linewidth=1, edgecolor='black', facecolor='#212121', alpha=0.7)
ax.add_patch(shadow3)
ax.text(60, 35, "Sombra", ha='center', va='center', fontsize=7, color='white')

# Posiciones de los Espectros (círculos de tono púrpura)
specter_positions = [(35, 75), (80, 75), (60, 35)]
for (x, y) in specter_positions:
    specter = patches.Circle((x, y), 3, linewidth=2, edgecolor='purple', facecolor='#ce93d8', alpha=0.9)
    ax.add_patch(specter)
    ax.text(x, y, "Espectro", ha='center', va='center', fontsize=6, color='black')

# Título del mapa
plt.title("Mapa del Corredor Oscuro - Encuentro 3: La Emboscada de las Sombras", fontsize=16, color='white')

plt.show()

