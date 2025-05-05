class Flower:
    def __init__(self, title, life_time, color, cost, height):
        self.__title = title
        self.__life_time = life_time
        self.__color = color
        self.__cost = cost
        self.__height = height

    @property
    def title(self):
        return self.__title

    @property
    def life_time(self):
        return self.__life_time

    @property
    def color(self):
        return self.__color

    @property
    def height(self):
        return self.__height

    @property
    def cost(self):
        return self.__cost

    def __str__(self):
        return (f'{self.title}: цвет - {self.color}, высота - {self.height} см, \n'
                f'время стояния (в днях) - {self.life_time}, стоимость - {self.cost} руб.')

    def __repr__(self):
        return (f'{self.title}: цвет - {self.color}, высота - {self.height} см, \n'
                f'время стояния (в днях) - {self.life_time}, стоимость - {self.cost} руб.')


class Rose(Flower):
    def __init__(self, life_time, color, cost, height, with_thorns):
        super().__init__('Роза', life_time, color, cost, height)
        self.__with_thorns = with_thorns

    @property
    def with_thorns(self):
        return self.__with_thorns

    def __str__(self):
        return super.__str__(self) + f', с шипами - {self.with_thorns}'


class Peony(Flower):
    def __init__(self, life_time, color, cost, height, is_pastel):
        super().__init__('Пион', life_time, color, cost, height)
        self.__is_pastel = is_pastel

    @property
    def is_pastel(self):
        return self.__is_pastel

    def __str__(self):
        return super.__str__(self) + f', пастельный оттенок - {self.is_pastel}'


class Chamomile(Flower):
    def __init__(self, life_time, color, cost, height, is_wild):
        super().__init__('Ромашка', life_time, color, cost, height)
        self.__is_wild = is_wild

    @property
    def is_wild(self):
        return self.__is_wild

    def __str__(self):
        return super.__str__(self) + f', полевая - {self.is_wild}'


class Bouquet():
    def __init__(self):
        self.bouquet = []

    def add_flower(self, obj):
        self.bouquet.append(obj)

    def life_time_of_bouquet(self):
        life_time = 0
        for flower in self.bouquet:
            life_time += flower.life_time
        return life_time / len(self.bouquet)

    def cost_of_bouquet(self):
        cost = 0
        for flower in self.bouquet:
            cost += flower.cost
        return cost

    def sort_by_fresh(self):
        return sorted(self.bouquet, key = lambda flower : flower.life_time, reverse = True)

    def sort_by_height(self):
        return sorted(self.bouquet, key = lambda flower : flower.height)

    def sort_by_cost(self):
        return sorted(self.bouquet, key=lambda flower: flower.cost)

    def sort_by_color(self):
        return sorted(self.bouquet, key=lambda flower: flower.color)

    def find_by_color(self, color):
        return [flower for flower in self.bouquet if flower.color == color]

    def __str__(self):
        result = ''
        for flower in self.bouquet:
            result += flower.__str__() + '\n'
        return f'Букет состоит из цветов: \n{result[:-1]}'

    def __repr__(self):
        result = ''
        for flower in self.bouquet:
            result += flower.__str__() + '\n'
        return f'Букет состоит из цветов: \n{result[:-1]}'


rose = Rose(5, 'красный', 500, 150, True)
peony = Peony(10, 'розовый', 1500, 100, False)
chamomile = Chamomile(7, 'белый', 1000, 15, False)

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(peony)
bouquet.add_flower(chamomile)

print(bouquet, '\n')
print(f'Стоимость букета: {bouquet.cost_of_bouquet()}\n')
print(f'Время стояния букета (в днях): {bouquet.life_time_of_bouquet()}\n')
print(f'Цветы в букете по убыванию свежести: \n{bouquet.sort_by_fresh()}\n')
print(f'Цветы в букете по возрастанию длины стебеля: \n{bouquet.sort_by_height()}\n')
print(f'Цветы в букете по возрастанию стоимости: \n{bouquet.sort_by_cost()}\n')
print(f'Цветы в букете отсортированные по цветам: \n{bouquet.sort_by_color()}\n')
print(f'Цветы красного цвета в букете: {bouquet.find_by_color("красный")}')
