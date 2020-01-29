
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        print name
        print bases
        print attrs

        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name

        return type.__new__(cls, name, bases, attrs)

print "\ndelimit Model class output"
"""
print name # Model
print bases # (<type 'dict'>,)
print attrs
{
'__module__': '__main__', 
'__metaclass__': <class '__main__.ModelMetaclass'>, 
'__setattr__': <function __setattr__ at 0x7f8ebb9cdaa0>, 
'__getattr__': <function __getattr__ at 0x7f8ebb9cda28>, 
'save': <function save at 0x7f8ebb9cdb18>, 
'__init__': <function __init__ at 0x7f8ebb9cd9b0>
}
"""
class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

print dir(Model)
"""
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', 
'__dict__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', 
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', 
'__le__', '__len__', '__lt__', '__metaclass__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 'clear', 'copy', 'fromkeys', 'get', 
'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 
'save', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
"""

print "\ndelimit User class output"
"""
print name # User
print bases # (<class '__main__.Model'>,)
print attrs
{
'email': <__main__.StringField object at 0x7f8ebb9d72d0>, 
'__module__': '__main__', 
'password': <__main__.StringField object at 0x7f8ebb9d7310>, 
'id': <__main__.IntegerField object at 0x7f8ebb9d7250>, 
'name': <__main__.StringField object at 0x7f8ebb9d7290>
}
"""
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

print dir(User)
"""
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__dict__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', 
'__lt__', '__mappings__', '__metaclass__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', 
'__str__', '__subclasshook__', '__table__', '__weakref__', 'clear', 'copy', 'fromkeys', 
'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 
'popitem', 'save', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
"""

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

"""
ubuntu@huzhi-ubuntu3:~/www/python-patterns/orm$ python orm_01.py 

delimit Model class output
Model
(<type 'dict'>,)
{'__module__': '__main__', '__metaclass__': <class '__main__.ModelMetaclass'>, '__setattr__': <function __setattr__ at 0x7f37d54bba28>, '__getattr__': <function __getattr__ at 0x7f37d54bb9b0>, 'save': <function save at 0x7f37d54bbaa0>, '__init__': <function __init__ at 0x7f37d54bb938>}

delimit User class output
User
(<class '__main__.Model'>,)
{'email': <__main__.StringField object at 0x7f37d54c5310>, '__module__': '__main__', 'password': <__main__.StringField object at 0x7f37d54c5350>, 'id': <__main__.IntegerField object at 0x7f37d54c5290>, 'name': <__main__.StringField object at 0x7f37d54c52d0>}

Found model: User
Found mapping: email ==> <StringField:email>
Found mapping: password ==> <StringField:password>
Found mapping: id ==> <IntegerField:id>
Found mapping: name ==> <StringField:username>

SQL: insert into User (password,email,username,id) values (?,?,?,?)
ARGS: ['my-pwd', 'test@orm.org', 'Michael', 12345]
ubuntu@huzhi-ubuntu3:~/www/python-patterns/orm$ 


"""
