class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if 1 > new_floor or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House('"ЖК Горский"', 18)
h2 = House('"Домик в деревне"', 2)
h1.go_to(18)
h2.go_to(3)
print(h1)
print(h2)
print(len(h1))
print(len(h2))