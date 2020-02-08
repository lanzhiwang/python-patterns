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
        print('name: %s' % name)
        print('bases: %s' % bases)
        print('attrs: %s' % attrs)
        print()
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
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
        """
        'id': <__main__.IntegerField object at 0x103a7fcf8>, 
        'name': <__main__.StringField object at 0x103a7fd30>, 
        'email': <__main__.StringField object at 0x103a7fd68>, 
        'password': <__main__.StringField object at 0x103a7fda0>
        """
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        print('fields: %s' % fields)  # fields: ['id', 'username', 'email', 'password']
        print('params: %s' % params)  # params: ['?', '?', '?', '?']
        print('args: %s' % args)  # args: [12345, 'Michael', 'test@orm.org', 'my-pwd']
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)  # SQL: insert into User (id,username,email,password) values (?,?,?,?)
        print('ARGS: %s' % str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


print(User.__mappings__)
print(User.__table__)

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
print(u)  # {'id': 12345, 'name': 'Michael', 'email': 'test@orm.org', 'password': 'my-pwd'}
u.save()


"""
name: Model
bases: <class 'dict'>
attrs: {
'__module__': '__main__', 
'__qualname__': 'Model', 
'__init__': <function Model.__init__ at 0x1087de510>, 
'__getattr__': <function Model.__getattr__ at 0x1087de598>, 
'__setattr__': <function Model.__setattr__ at 0x1087de620>, 
'save': <function Model.save at 0x1087de6a8>, 
'__classcell__': <cell at 0x1087bfc78: empty>
}

name: User
bases: <class '__main__.Model'>
attrs: {
'__module__': '__main__', 
'__qualname__': 'User', 
'id': <__main__.IntegerField object at 0x1087d6cf8>, 
'name': <__main__.StringField object at 0x1087d6d30>, 
'email': <__main__.StringField object at 0x1087d6d68>, 
'password': <__main__.StringField object at 0x1087d6da0>
}

{
'id': <__main__.IntegerField object at 0x103a7fcf8>, 
'name': <__main__.StringField object at 0x103a7fd30>, 
'email': <__main__.StringField object at 0x103a7fd68>, 
'password': <__main__.StringField object at 0x103a7fda0>
}
User

"""

