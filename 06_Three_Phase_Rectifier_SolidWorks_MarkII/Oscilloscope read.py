import numpy as np
import matplotlib.pyplot as plt

# Ruta al archivo
file_path = "C:/Users/diego/Downloads/WAVE020.DAT"

# Carga binaria (ajusta dtype según modelo)
data = np.fromfile(file_path, dtype=np.uint8)

# En algunos modelos, los primeros bytes son encabezados
data = data[10:]  # puedes probar con 10, 16 o 32

# Grafica
plt.plot(data)
plt.title("Forma de onda capturada desde UNI-T UTD2102CEX")
plt.xlabel("Muestras")
plt.ylabel("Nivel (arbitrario)")
plt.show()
