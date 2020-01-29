#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cPickle as pickle

#import pickle

'''pickle 模块提供了以下函数对：
dumps(object) 返回一个字符串，它包含一个 pickle 格式的对象；
loads(string) 返回包含在 pickle 字符串中的对象；

dump(object, file) 将对象写到文件，这个文件可以是实际的物理文件，但也可以是任何类似于文件的对象，这个对象具有 write() 方法，可以接受单个的字符串参数；
load(file) 返回包含在 pickle 文件中的对象。

缺省情况下， dumps() 和 dump() 使用可打印的 ASCII 表示来创建 pickle。两者都有一个 final 参数（可选），如果为 True ，则该参数指定用更快以及更小的二进制表示来创建 pickle。 
loads() 和 load() 函数自动检测 pickle 是二进制格式还是文本格式。
'''

a1 = 'apple'
b1 = {1: 'One', 2: 'Two', 3: 'Three'}
c1 = ['fee', 'fie', 'foe', 'fum']

f1 = file('temp.pkl', 'wb')

pickle.dump(a1, f1, True)
pickle.dump(b1, f1, True)
pickle.dump(c1, f1, True)

f1.close()

f2 = file('temp.pkl', 'rb')
a2 = pickle.load(f2)
print a2  # apple
b2 = pickle.load(f2)
print b2  # {1: 'One', 2: 'Two', 3: 'Three'}
c2 = pickle.load(f2)
print c2  # ['fee', 'fie', 'foe', 'fum']
f2.close()  

'''ubuntu@huzhi-dev:~/www/python-patterns/copyreg$ cat temp.pkl 
ubuntu@huzhi-dev:~/www/python-patterns/copyreg$ 
ubuntu@huzhi-dev:~/www/python-patterns/copyreg$ python copyreg_test_02.py 
apple
{1: 'One', 2: 'Two', 3: 'Three'}
['fee', 'fie', 'foe', 'fum']
ubuntu@huzhi-dev:~/www/python-patterns/copyreg$ strings temp.pkl 
appleq
Oneq
Twoq
Threeq
u.]q
feeq
fieq
foeq
fumq
ubuntu@huzhi-dev:~/www/python-patterns/copyreg$ 
'''
