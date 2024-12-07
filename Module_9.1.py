class tepValueError(ValueError):
    pass
class StepValueError(Exception):
    pass

class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self

    def get_number1(self):
        el = []
        while self.pointer != self.stop + 1:
            el.append(str(self.pointer))
            self.pointer += self.step
        return el

    def get_number2(self):
        el = []
        while self.pointer != self.stop - 1:
            el.append(str(self.pointer))
            if self.step < 0:
                self.pointer += self.step
            else:
                self.pointer -= self.step
        return el


    def __next__(self):
        if self.pointer < self.stop:
            print(*self.get_number1())
            raise StopIteration()
        else:
            # print(*self.get_number2())
            # raise StopIteration()
            if self.pointer != self.stop - 1:
                el = str(self.pointer)
                if self.step < 0:
                    self.pointer += self.step
                else:
                    self.pointer -= self.step
                return el
            raise StopIteration()

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# for i in iter2:
#     print(i, end=' ')
# for i in iter3:
#     print(i, end=' ')
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')