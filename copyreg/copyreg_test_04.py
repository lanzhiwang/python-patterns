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

# 对象引用的维护
a = [1, 2, 3]
b = a
print a  # [1, 2, 3]
print b  # [1, 2, 3]
a.append(4)
print a  # [1, 2, 3, 4]
print b  # [1, 2, 3, 4]
c = pickle.dumps((a, b))
d, e = pickle.loads(c)
print d  # [1, 2, 3, 4]
print e  # [1, 2, 3, 4]

d.append(5)
print d  # [1, 2, 3, 4, 5]
print e  # [1, 2, 3, 4, 5]

print '==================' * 10

# 递归引用
l = [1, 2, 3]
print l  # [1, 2, 3]
l.append(l)  
print l  # [1, 2, 3, [...]]
print l[3]  # [1, 2, 3, [...]]
print l[3][3]  # [1, 2, 3, [...]]
p = pickle.dumps(l)
l2 = pickle.loads(p)  
print l2  # [1, 2, 3, [...]]
print l2[3]  # [1, 2, 3, [...]]
print l2[3][3]  # [1, 2, 3, [...]]

print '==================' * 10

# 循环引用
a = [1, 2]  
b = [3, 4]
print a  # [1, 2]
print b  # [3, 4]

a.append(b)  
print a  # [1, 2, [3, 4]]
print b  # [3, 4]

print a[2] is b  # True

b.append(a)
print a  # [1, 2, [3, 4, [...]]]
print b  # [3, 4, [1, 2, [...]]]

print b[2] is a  # True

print a[2] is b  # True
print a[2][2] is a  # True

f = file('temp.pkl', 'w')  
pickle.dump((a, b), f)  
f.close()  

f = file('temp.pkl', 'r')
c, d = pickle.load(f)  
f.close()  
print c  # [1, 2, [3, 4, [...]]]
print d  # [3, 4, [1, 2, [...]]]


f = file('temp.pkl', 'w')  
pickle.dump(a, f)  
pickle.dump(b, f)  
f.close()  
f = file('temp.pkl', 'r')  
c = pickle.load(f)  
d = pickle.load(f)  
f.close()  