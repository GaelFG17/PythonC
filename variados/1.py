class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("La subclase debe implementar el método abstracto")

class Dog(Animal):
    def speak(self):
        return f"{self.name} dice Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} dice Meow!"

def animal_sound(animal):
    print(animal.speak())

if __name__ == "__main__":
    animals = [Dog("Buddy"), Cat("Whiskers")]
    for animal in animals:
        animal_sound(animal)