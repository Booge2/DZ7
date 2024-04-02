class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def __str__(self):
        return f"Пристрій:\nБренд: {self.brand}\nМодель: {self.model}\nПотужність: {self.power}"


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, capacity):
        super().__init__(brand, model, power)
        self.capacity = capacity

    def make_coffee(self):
        print(f"Кавоварка {self.brand} {self.model} готує каву!")

    def __str__(self):
        return f"{super().__str__()}\nМісткість: {self.capacity}"


class Blender(Device):
    def __init__(self, brand, model, power, speed):
        super().__init__(brand, model, power)
        self.speed = speed

    def blend(self):
        print(f"Блендер {self.brand} {self.model} подрібнює продукти!")

    def __str__(self):
        return f"{super().__str__()}\nШвидкість: {self.speed}"


class MeatGrinder(Device):
    def __init__(self, brand, model, power, productivity):
        super().__init__(brand, model, power)
        self.productivity = productivity

    def grind_meat(self):
        print(f"М'ясорубка {self.brand} {self.model} перемелює м'ясо!")

    def __str__(self):
        return f"{super().__str__()}\nПродуктивність: {self.productivity}"


coffee_machine = CoffeeMachine("Bosch", "CM 1200", 1450, 1.5)
print(coffee_machine)
coffee_machine.make_coffee()

blender = Blender("Braun", "JB 5160", 750, 20000)
print(blender)
blender.blend()

meat_grinder = MeatGrinder("Panasonic", "MK-MG1000", 800, 2.1)
print(meat_grinder)
meat_grinder.grind_meat()


# Завдання 2
class Ship:
    def __init__(self, name, country, length, width, displacement):
        self.name = name
        self.country = country
        self.length = length
        self.width = width
        self.displacement = displacement

    def __str__(self):
        return f"Корабель:\nНазва: {self.name}\nКраїна: {self.country}\nДовжина: {self.length}\nШирина: {self.width}\nВодотоннажність: {self.displacement}"


class Frigate(Ship):
    def __init__(self, name, country, length, width, displacement, armament):
        super().__init__(name, country, length, width, displacement)
        self.armament = armament

    def fire_missiles(self):
        print(f"Фрегат {self.name} веде вогонь ракетами!")

    def __str__(self):
        return f"{super().__str__()}\nОзброєння: {self.armament}"


class Destroyer(Ship):
    def __init__(self, name, country, length, width, displacement, speed):
        super().__init__(name, country, length, width, displacement)
        self.speed = speed

    def __str__(self):
        return f"{super().__str__()}\nШвидкість: {self.speed}"


class Cruiser(Ship):
    def __init__(self, name, country, length, width, displacement, range):
        super().__init__(name, country, length, width, displacement)
        self.range = range

    def __str__(self):
        return f"{super().__str__()}\nДальність ходу: {self.range}"


frigate = Frigate("USS Freedom", "USA", 140, 18, 4500, "16 x RIM-162 ESSM missiles")
print(frigate)
frigate.fire_missiles()

destroyer = Destroyer("HMS Daring", "UK", 133, 16, 7350, 30)
print(destroyer)

cruiser = Cruiser("HMS Queen Elizabeth (R08)", "Great Britain", 280, 50, 65000, 10000)
print(cruiser)


# Завдання 3
class Money:
    def __init__(self, whole_part, fractional_part):
        self._whole_part = whole_part
        self._fractional_part = fractional_part

    def __str__(self):
        return f"{self._whole_part} грн {self._fractional_part} коп."

    def set_whole_part(self, new_whole_part):
        self._whole_part = new_whole_part

    def set_fractional_part(self, new_fractional_part):
        self._fractional_part = new_fractional_part

    def get_whole_part(self):
        return self._whole_part

    def get_fractional_part(self):
        return self._fractional_part

    def add(self, other_money):
        total_whole_part = self._whole_part + other_money._whole_part
        total_fractional_part = self._fractional_part + other_money._fractional_part
        return Money(total_whole_part, total_fractional_part)

    def subtract(self, other_money):
        total_whole_part = self._whole_part - other_money._whole_part
        total_fractional_part = self._fractional_part - other_money._fractional_part
        return Money(total_whole_part, total_fractional_part)

    def multiply(self, number):
        total_whole_part = self._whole_part * number
        total_fractional_part = self._fractional_part * number
        return Money(total_whole_part, total_fractional_part)

    def divide(self, number):
        total_whole_part = self._whole_part // number
        total_fractional_part = self._fractional_part // number
        return Money(total_whole_part, total_fractional_part)


class Product(Money):
    def __init__(self, name, whole_part, fractional_part):
        super().__init__(whole_part, fractional_part)
        self.name = name

    def __str__(self):
        return f"{self.name}: {super().__str__()}"

    def discount(self, discount_amount):
        new_price = self.subtract(Money(discount_amount, 0))
        return new_price


money1 = Money(100, 50)
print(money1)

money2 = Money(50, 25)
print(money2)

money3 = money1.add(money2)
print(money3)

money4 = money1.subtract(money2)
print(money4)

money5 = money1.multiply(2)
print(money5)

money6 = money1.divide(2)
print(money6)

product1 = Product("Товар 1", 100, 50)
print(product1)

discounted_price = product1.discount(10)
print(f"Знижена ціна: {discounted_price}")
