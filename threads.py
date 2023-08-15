from time import sleep
from threading import Thread


# Exemplo 1
def tarefa(tempo_espera, mensagem):
    """
    Método que imprime duas mensagens com um intervalo de tempo x entre elas
    :param tempo_espera: int
    :param mensagem: str
    :return: str
    """
    print(f"\nIniciando a tarefa {mensagem}")
    sleep(tempo_espera)
    print(f"Conclusão da tarefa {mensagem}")


# Thread que chama a função tarefa (target) carregando o delay para exibir a mensagem
# Threads são a unidade básica de execução de um processo.
thread = Thread(target=tarefa, args=(.1, "Thread em execução"))

# Após instanciar a thread é necessário iniciá-la, para isso a função 'instancia.start()'
thread.start()
print(f"\nAguardando a execução da Thread...")

# join() bloqueia a execução do código corrente até que as threads sejam concluídas
thread.join()

print("A execução foi concluída.\n")
print("Fim do Exemplo 1\n")
sleep(3)

# Exemplo 2
def task(atraso, descricao):
    print(f"Task {descricao} iniciada")
    sleep(atraso)
    print(f"Task {descricao} concluída")


thread1 = Thread(target=task, args=(3, "A"))
thread2 = Thread(target=task, args=(2, "B"))

# Iniciando as threads
thread1.start()
thread2.start()

# Bloqueando a execução dos códigos seguintes até a conclusão das threads
thread1.join()
thread2.join()

print("Threads concluídas\n\n")
sleep(3)

# Exemplo 3
def task2(atraso, num):
    print(f"Task 2 >> O cubo de {num} é {num ** 3}")
    sleep(atraso)
    print(f"Task 2 concluída")

def task3(atraso, num):
    print(f"Task 3 >> O quadrado de {num} é {num ** 2}")
    sleep(atraso)
    print(f"Task 3 concluída")

thread3 = Thread(target=task2, args=(3, 3))
thread4 = Thread(target=task3, args=(2, 4))

thread3.start()
thread4.start()

thread3.join()
thread4.join()

print("Threads concluídas!")
