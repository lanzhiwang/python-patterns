#!/usr/bin/env python
# -*- coding: utf-8 -*-

class foobase:
    def hello(self):
        print "hello"

class foo:
    pass

#obj=foo()
#obj.hello()
'''ubuntu@huzhi-dev:~/www/python-patterns$ python mixin-test.py
Traceback (most recent call last):
  File "mixin-test.py", line 12, in <module>
    obj.hello()
AttributeError: foo instance has no attribute 'hello'
ubuntu@huzhi-dev:~/www/python-patterns$ 
'''

obj=foo()
foo.__bases__ +=(foobase,)
obj.hello()
'''ubuntu@huzhi-dev:~/www/python-patterns$ python mixin-test.py
hello
ubuntu@huzhi-dev:~/www/python-patterns$ 
'''

'''每个类都有一个__base__属性，它是一个tuple，用来存放所有的基类。而且在运行中，可以动态改变。
所以当我们向其中增加新的基类时，再次调用原来不存在的函数，由于基类中的函数已经存在了，所以这次成功了。

这是一个最简单的应用，可以看到我们可以动态改变类的基类。有几个注意事项要说一下：
1、__bases__是一个tuple，所以增加一个值要使用tuple类型，而单个元素tuple的写法为(foobase,)
2、类必须先存在。所以，如果想使用这一技术，先要将相关的类的模块导入(import)。
由于Mix-in是一种动态技术，以多继承，对象为基础，而python正好是这样的语言，使得在python中实现这一技术非常容易。
'''









