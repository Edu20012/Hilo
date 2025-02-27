import threading
import multiprocessing
import time


# ================== Sección de Hilos (I/O-bound) ==================
def tarea_io(nombre):
    print(f'Hilo {nombre}: Iniciando tarea I/O')
    time.sleep(2)  # Simula operación I/O (ej. lectura de archivo/red)
    print(f'Hilo {nombre}: Tarea I/O completada')


def ejecutar_hilos():
    hilos = []
    for i in range(3):
        hilo = threading.Thread(target=tarea_io, args=(i,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()


# ============== Sección de Procesos (CPU-bound) ==============
def tarea_cpu(numero):
    print(f'Proceso {numero}: Calculando...')
    resultado = sum(i * i for i in range(10 ** 6))  # Operación intensiva de CPU
    print(f'Proceso {numero}: Resultado = {resultado}')


def ejecutar_procesos():
    procesos = []
    for i in range(3):
        proceso = multiprocessing.Process(target=tarea_cpu, args=(i,))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()


# ================== Demonio (Tarea en segundo plano) ==================
def demonio():
    while True:
        print("Demonio: Ejecutando tarea en segundo plano...")
        time.sleep(1)


# ================== Ejecución principal ==================
if __name__ == "__main__":
    print("\nEjemplo completo de concurrencia en Python\n")

    # Iniciar demonio (se detendrá automáticamente al finalizar el programa)
    d = threading.Thread(target=demonio)
    d.daemon = True
    d.start()

    print("\n=== Ejecutando hilos para tareas I/O ===")
    inicio = time.time()
    ejecutar_hilos()
    print(f'Tiempo hilos: {time.time() - inicio:.2f}s')

    print("\n=== Ejecutando procesos para tareas CPU ===")
    inicio = time.time()
    ejecutar_procesos()
    print(f'Tiempo procesos: {time.time() - inicio:.2f}s')

    print("\nPrograma principal terminado. El demonio será eliminado automáticamente.")