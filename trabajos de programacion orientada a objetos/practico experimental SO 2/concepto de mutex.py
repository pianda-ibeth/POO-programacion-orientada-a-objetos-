import threading
contador_global=0
mutex=threading.Lock()
def incrementar():
    global contador_global
    mutex.acquire()
    try:
        contador_global+=1
    finally:
        mutex.release()
def tarea():
    for _ in range(100000):
        incrementar()
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
print("el valor final del contador global es:", contador_global)