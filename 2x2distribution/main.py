import calculos
import time

inicio = time.time()

#calculos.distribucion()
calculos.generar_combinaciones()
print("Resuelto en ", round(time.time() - inicio, 2))
