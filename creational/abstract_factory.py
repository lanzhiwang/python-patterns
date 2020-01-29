#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
The Abstract Factory Pattern serves to provide an interface for
creating related/dependent objects without need to specify their
actual class.
The idea is to abstract the creation of objects depending on business
logic, platform choice, etc.

*What does this example do?
This particular implementation abstracts the creation of a pet and
does so depending on the AnimalFactory we chose (Dog or Cat)
This works because both Dog/Cat and their factories respect a common
interface (.speak(), get_pet() and get_food()).
Now my application can create pets (and feed them) abstractly and decide later,
based on my own criteria, dogs over cats.
The second example allows us to create pets based on the string passed by the
user, using cls.__subclasses__ (the list of sub classes for class cls)
and  sub_cls.__name__ to get its name.

*Where is the pattern used practically?

*References:
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR80
Provides a way to encapsulate a group of individual factories.
"""


import six
import abc
import random


class PetShop(object):

    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""

        pet = self.pet_factory.get_pet()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("We also have {}".format(self.pet_factory.get_food()))


# Stuff that our factory makes

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


# Factory classes

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


# Create the proper family
def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()


"""
装饰器的引入纯粹是一个“语法糖”，即让代码看起来更加易懂。
装饰器引入前Python中已经存在了“class method”, "static method"等包裹函数，
不使用装饰器的结果是如果一个方法要被声明为class method，
那么在他的“def”语句结束后需要立即使用"classmethod"将其注册成类方法。
这样有一些弊端：当代码的读者开始读这个函数的时候，他一般看不到末尾的"classmethod"语句，
所以可能直到看完整个函数的定义才知道这是一个类方法，也即是最初没有装饰器时在定义的结尾对方法进行装饰的设定比较反人类；
另外采用 method = classmethod(method) 方式写出来的代码，设计Python的大神们觉得 method 竟然重复出现了两次太多了，
写这两次 method 的时间已经够他们喝一壶的了，所以引入了更为简洁的decorator。

装饰器以“@”标识，实质上是一层包裹函数，即函数的函数。
写在函数定义（ def 语句）的前面，表示 def 语句后定义的函数受到装饰器的装饰，也就是说这个新定义的函数刚刚出生，
立刻在函数定义结束的下一行代码运行装饰器给她穿点衣服遮羞。
"""


# Implementation 2 of an abstract factory
@six.add_metaclass(abc.ABCMeta)
class Pet(object):

    @classmethod
    def from_name(cls, name):
        for sub_cls in cls.__subclasses__():
            if name == sub_cls.__name__.lower():
                return sub_cls()

    @abc.abstractmethod
    def speak(self):
        """"""


class Kitty(Pet):
    def speak(self):
        return "Miao"


class Duck(Pet):
    def speak(self):
        return "Quak"


# Show pets with various factories
if __name__ == "__main__":
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)

    for name0 in ["kitty", "duck"]:
        pet = Pet.from_name(name0)
        print("{}: {}".format(name0, pet.speak()))

### OUTPUT ###
# We have a lovely Cat
# It says meow
# We also have cat food
# ====================
# We have a lovely Dog
# It says woof
# We also have dog food
# ====================
# We have a lovely Cat
# It says meow
# We also have cat food
# ====================
# kitty: Miao
# duck: Quak
