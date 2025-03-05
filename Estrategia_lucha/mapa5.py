import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuración de la figura: 16x12 pulgadas a 93.75 dpi ≈ 1500px de ancho
fig, ax = plt.subplots(figsize=(16, 12), dpi=93.75)
ax.set_aspect('equal')
ax.set_xlim(0, 160)
ax.set_ylim(0, 120)
ax.axis('off')

# Dibujar el contorno de la sala del trono (paredes exteriores)
sala = patches.Rectangle((10, 10), 140, 100, linewidth=2, edgecolor='black', facecolor='#f5f5f5')
ax.add_patch(sala)

# Dibujar columnas o estructuras derrumbadas (ofreciendo cobertura)
columnas = [(30, 90), (130, 90), (30, 30), (130, 30)]
for (x, y) in columnas:
    col = patches.Circle((x, y), 8, linewidth=2, edgecolor='black', facecolor='#d1c4e9')
    ax.add_patch(col)
    ax.text(x, y, "Col", ha='center', va='center', fontsize=10, color='black')

# Dibujar escombros: áreas que pueden usarse para cubrirse
escombro1 = patches.Rectangle((60, 70), 20, 10, linewidth=2, edgecolor='black', facecolor='#ffe082', alpha=0.8)
ax.add_patch(escombro1)
ax.text(70, 75, "Escombro", ha='center', va='center', fontsize=10, color='black')

escombro2 = patches.Rectangle((60, 30), 25, 10, linewidth=2, edgecolor='black', facecolor='#ffe082', alpha=0.8)
ax.add_patch(escombro2)
ax.text(72.5, 35, "Escombro", ha='center', va='center', fontsize=10, color='black')

# Dibujar una plataforma elevada (ofreciendo ventaja para ataques a distancia)
plataforma = patches.Rectangle((110, 70), 30, 10, linewidth=2, edgecolor='black', facecolor='#a5d6a7', alpha=0.8)
ax.add_patch(plataforma)
ax.text(125, 75, "Plataforma", ha='center', va='center', fontsize=10, color='black')

# Dibujar el jefe final (Maestro de la Estrategia)
jefe = patches.Rectangle((70, 50), 20, 20, linewidth=3, edgecolor='darkred', facecolor='#ffab91')
ax.add_patch(jefe)
ax.text(80, 60, "Maestro", ha='center', va='center', fontsize=12, color='black')

# Indicador de vulnerabilidad (zona iluminada en la armadura del jefe)
vulnerabilidad = patches.Circle((80, 60), 4, linewidth=2, edgecolor='gold', facecolor='yellow', alpha=0.8)
ax.add_patch(vulnerabilidad)
ax.text(80, 60, "Debilidad", ha='center', va='center', fontsize=10, color='black')

# Dibujar líneas divisorias o muros derrumbados internos
ax.plot([10, 150], [80, 80], linestyle='--', color='gray', linewidth=1)
ax.plot([80, 80], [10, 110], linestyle='--', color='gray', linewidth=1)

# Posiciones iniciales de esbirros o enemigos secundarios (círculos rojos)
for pos in [(20, 100), (140, 100), (20, 20), (140, 20)]:
    esbirro = patches.Circle(pos, 4, linewidth=2, edgecolor='darkred', facecolor='#ff8a80')
    ax.add_patch(esbirro)
    ax.text(pos[0], pos[1], "En.", ha='center', va='center', fontsize=10, color='black')

# Título del mapa con tamaño de fuente aumentado
plt.title("Mapa de la Sala del Trono - Encuentro Final", fontsize=16)

# Guardar la imagen en alta resolución (aprox. 1500px de ancho)
plt.savefig("mapa_encuentro_final.png", dpi=93.75, bbox_inches='tight')
plt.show()

