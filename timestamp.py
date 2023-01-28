from time import sleep
from threading import Thread
from threading import Thread
from time import sleep

print("Olá campers")

for i in range(10):
    print(i)
    sleep(.5)
    
print("Olá")

class IGThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        
        super().__init__()
        
    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = IGThread('Sana Thread 1', 5)
t1.start()

t2 = IGThread('Sana Thread 2', 8)
t2.start()

t3 = IGThread('Sana Thread 3', 17)
t3.start()

t4 = IGThread('Sana Thread 4', 2)
t4.start()

for i in range(20):
    print(i)
    sleep(1)
    

def tarefa_demorada(texto, tempo):
    sleep(tempo)
    print(texto)

t = Thread(target=tarefa_demorada, args=('Thread IGTI 1 ', 5))
t.start()

t1 = Thread(target=tarefa_demorada, args=('Thread IGTI 2', 4))
t1.start()

t2 = Thread(target=tarefa_demorada, args=('Thread IGTI 3', 2))
t2.start()

for i in range(20):
    print(i)
    sleep(0.5)
    
    def tarefa_demorada(texto, tempo):
        sleep(tempo)
        print(texto)

t = Thread(target=tarefa_demorada, args=('Thread IGTI', 10))
t.start()

while t.is_alive():
    print('Esperando a Thread.')
    sleep(2)

# Então essa é uma maneira de você esperar thread terminar de fazer um parefa para execultar
# Por exemplo
print("Thread Acabou!")

#t.join() #Agora ele retorna block


