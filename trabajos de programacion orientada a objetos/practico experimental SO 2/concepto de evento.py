import threading
import time
evente = threading.Event()
def esperar_evento():
    print("Esperando evento...")
    evente.wait()
    print("El evento ha sido activado")
def activar_evento():
    print("Esperando 5 segundos antes de activar evento...")
    time.sleep(5)
    evente.set()
    print("El evento ha sido activado despues de 5 segundos")
hilo1 = threading.Thread(target=esperar_evento)
hilo2 = threading.Thread(target=activar_evento)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
print("programa terminado")