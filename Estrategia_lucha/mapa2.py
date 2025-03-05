import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuración de la figura
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')
ax.set_xlim(0, 120)
ax.set_ylim(0, 100)
ax.axis('off')

# Dibujar el contorno del laberinto (paredes)
laberinto = patches.Rectangle((10, 10), 100, 80, linewidth=2, edgecolor='black', facecolor='#f5f5f5')
ax.add_patch(laberinto)

# Dibujar el corredor principal con divisiones internas
# Línea divisoria central (camino principal)
ax.plot([10, 110], [60, 60], linestyle='-', color='black', linewidth=2)

# Dibujar curvas que simulan giros del laberinto
curve1 = patches.Arc((40, 60), 40, 20, angle=0, theta1=180, theta2=270, linewidth=2, edgecolor='gray')
ax.add_patch(curve1)
curve2 = patches.Arc((80, 60), 40, 20, angle=0, theta1=270, theta2=360, linewidth=2, edgecolor='gray')
ax.add_patch(curve2)

# Zonas de trampas: 
# Representadas con rectángulos rojos semitransparentes (placas de presión)
trampa1 = patches.Rectangle((15, 15), 20, 10, linewidth=1, edgecolor='red', facecolor='#ff8a80', alpha=0.5)
ax.add_patch(trampa1)
ax.text(25, 20, "Trampa", ha='center', va='center', fontsize=8, color='black')

trampa2 = patches.Rectangle((85, 75), 15, 8, linewidth=1, edgecolor='red', facecolor='#ff8a80', alpha=0.5)
ax.add_patch(trampa2)
ax.text(92.5, 79, "Trampa", ha='center', va='center', fontsize=8, color='black')

# Zona segura: 
# Un área con fondo en color verde pálido que indica un breve respiro
zona_segura = patches.Rectangle((45, 20), 30, 15, linewidth=2, edgecolor='green', facecolor='#c8e6c9', alpha=0.7)
ax.add_patch(zona_segura)
ax.text(60, 27.5, "Zona Segura", ha='center', va='center', fontsize=9, color='black')

# Elemento interactivo (palanca/interrutor)
palanca = patches.Circle((100, 40), 4, linewidth=2, edgecolor='blue', facecolor='#81d4fa')
ax.add_patch(palanca)
ax.text(100, 40, "Palanca", ha='center', va='center', fontsize=8, color='black')

# Etiqueta para el enigma
ax.text(60, 85, "Laberinto de Trampas", ha='center', va='center', fontsize=14, color='black')

plt.title("Mapa del Laberinto de Trampas - Encuentro 2", fontsize=16)
plt.show()

