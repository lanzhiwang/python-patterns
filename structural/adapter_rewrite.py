#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"


class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)


class Adapter(object):
    """
    Adapter(dog, make_noise=dog.bark)
    """
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


def main():
    objects = []

    dog = Dog()
    print(dog.__dict__)  # {'name': 'Dog'}
    objects.append(Adapter(dog, make_noise=dog.bark))
    print(objects[0].__dict__)  # {'obj': <__main__.Dog object at 0x10cb47d30>, 'make_noise': <bound method Dog.bark of <__main__.Dog object at 0x10cb47d30>>}
    print(objects[0].original_dict())  # {'name': 'Dog'}

    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    print(objects[1].__dict__)  # {'obj': <__main__.Cat object at 0x10cb47e80>, 'make_noise': <bound method Cat.meow of <__main__.Cat object at 0x10cb47e80>>}
    print(objects[1].original_dict())  # {'name': 'Cat'}

    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    print(objects[2].__dict__)  # {'obj': <__main__.Human object at 0x10cb47ef0>, 'make_noise': <bound method Human.speak of <__main__.Human object at 0x10cb47ef0>>}
    print(objects[2].original_dict())  # {'name': 'Human'}

    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))
    print(objects[3].__dict__)  # {'obj': <__main__.Car object at 0x10cb47f28>, 'make_noise': <function main.<locals>.<lambda> at 0x10cb4f840>}
    print(objects[3].original_dict())  # {'name': 'Car'}

    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))
    """
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """


if __name__ == "__main__":
    main()
