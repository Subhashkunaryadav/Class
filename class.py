class Animal:
    def __init__(self, species, weight, height):
        self.species = species
        self.weight = weight
        self.height = height

    def eat(self, food):
        print(f"{self.species} is eating {food}")

    def sleep(self):
        print(f"{self.species} is sleeping")

    def move(self):
        print(f"{self.species} is moving")

class Mammal(Animal):
    def __init__(self, species, weight, height, hair_color):
        super().__init__(species, weight, height)
        self.hair_color = hair_color

    def give_birth(self):
        print(f"{self.species} is giving birth")

class Bird(Animal):
    def __init__(self, species, weight, height, wingspan):
        super().__init__(species, weight, height)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.species} is flying")

class Reptile(Animal):
    def __init__(self, species, weight, height, is_cold_blooded):
        super().__init__(species, weight, height)
        self.is_cold_blooded = is_cold_blooded

    def sun_bathe(self):
        print(f"{self.species} is sun bathing")

class Dog(Mammal):
    def __init__(self, species, weight, height, hair_color, breed):
        super().__init__(species, weight, height, hair_color)
        self.breed = breed

    def bark(self):
        print(f"{self.species} is barking")

class Cat(Mammal):
    def __init__(self, species, weight, height, hair_color, breed):
        super().__init__(species, weight, height, hair_color)
        self.breed = breed

    def meow(self):
        print(f"{self.species} is meowing")

class Parrot(Bird):
    def __init__(self, species, weight, height, wingspan, color):
        super().__init__(species, weight, height, wingspan)
        self.color = color

    def talk(self, message):
        print(f"{self.species} says '{message}'")

class Snake(Reptile):
    def __init__(self, species, weight, height, is_cold_blooded, venomous):
        super().__init__(species, weight, height, is_cold_blooded)
        self.venomous = venomous

    def bite(self):
        if self.venomous:
            print(f"{self.species} is biting and injecting venom")
        else:
            print(f"{self.species} is biting")

class Zoo:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_total_weight(self):
        total_weight = 0
        for animal in self.animals:
            total_weight += animal.weight
        return total_weight

    def get_total_height(self):
        total_height = 0
        for animal in self.animals:
            total_height += animal.height
        return total_height
