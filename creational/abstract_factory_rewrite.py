#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class Dog(object):
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat(object):
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


class DogFactory(object):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory(object):
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


def get_factory():
    return random.choice([DogFactory, CatFactory])()


class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print(pet)
        print(pet.speak())
        print(self.pet_factory.get_food())


if __name__ == "__main__":
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)
"""
Cat
meow
cat food
====================
Dog
woof
dog food
====================
Cat
meow
cat food
====================
"""
