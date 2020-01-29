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

t1 = ('this is a string', 42, [1, 2, 3], None)

p1 = pickle.dumps(t1)
print p1
t2 = pickle.loads(p1)
print t2

p2 = pickle.dumps(t1, True)
print p2
t2 = pickle.loads(p2)
print t2
'''ubuntu@huzhi-dev:~/www/python-patterns/copyreg$ python copyreg_test_01.py 
(S'this is a string'
p1
I42
(lp2
I1
aI2
aI3
aNtp3
.
('this is a string', 42, [1, 2, 3], None)
(Uthis is a stringqK*]q(KKKeNtq.
('this is a string', 42, [1, 2, 3], None)
ubuntu@huzhi-dev:~/www/python-patterns/copyreg$ 
'''

