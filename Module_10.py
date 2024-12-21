import threading
import  time
import  random

lock = threading.Lock()

class Bank():

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self):
        for i in range(100):
            time.sleep(0.001)
            s = random.randint(50, 500)
            self.balance += s
            if self.balance >= 500 and lock.locked():
                lock.release()
            print(f'Поплнение: {s}, Баланс: {self.balance}')

    def take(self):
        for i in range(100):
            time.sleep(0.001)
            s = random.randint(50, 500)
            print(f'Запрос на {s}')
            if self.balance > s:
                self.balance -= s
                print(f'Снятие: {s}, Баланс: {self.balance}')
            else:
                print('Запрос отменён, недостаточно средств')
                lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')