class House:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def __len__(self):
        return self.num

    def __str__ (self):
        return  f"Название: {self.name}, кол-во этажей: {self.num}"

    def __eq__(self, other):
        isinstance(other, int)
        return self.num == other.num

    def  __add__(self, value):
        self.num = self.num + value
        return self
    def __iadd__(self, other):
        isinstance(other, int)
        self.num += other
        return self
    def __radd__(self, other):
        isinstance(other, int)
        self.num = self.num + other
        return self

    def __lt__(self, other):
        return self.num < other.num
    def __le__(self, other):
        return self.num <= other.num
    def __gt__(self, other):
        return self.num > other.num
    def __ge__(self, other):
        return  self.num >= other.num
    def __ne__(self, other):
        return self.num != other.num



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__