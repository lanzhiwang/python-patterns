class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super(StringField, self).__init__(name, ddl, primary_key, default)


class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='bigint'):
        super(IntegerField, self).__init__(name, ddl, primary_key, default)


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        print('name: %s' % name)
        print('bases: %s' % bases)
        print('attrs: %s' % attrs)
        print()
        """
        name: User
        bases: <class '__main__.Model'>
        attrs: {
        '__module__': '__main__', 
        '__qualname__': 'User', 
        '__table__': 'users', 
        'id': <__main__.IntegerField object at 0x103f840f0>, 
        'name': <__main__.StringField object at 0x103f84160>, 
        'email': <__main__.StringField object at 0x103f841d0>, 
        'password': <__main__.StringField object at 0x103f84208>
        }
        """
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        table_name = attrs.get('__table__', None) or name

        mappings = dict()
        fields = []
        primary_key = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                if v.primary_key:
                    if primary_key:
                        raise RuntimeError('Duplicate primary key for field: %s' % k)
                    primary_key = k
                else:
                    fields.append(k)
        print('mappings: %s' % mappings)
        """
        mappings: {
        'id': <__main__.IntegerField object at 0x103f840f0>, 
        'name': <__main__.StringField object at 0x103f84160>, 
        'email': <__main__.StringField object at 0x103f841d0>, 
        'password': <__main__.StringField object at 0x103f84208>
        }
        """
        print('fields: %s' % fields)  # fields: ['name', 'email', 'password']
        print('primary_key: %s' % primary_key)  # primary_key: id

        if not primary_key:
            raise RuntimeError('Primary key not found.')

        for k in mappings.keys():
            attrs.pop(k)

        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        print('escaped_fields: %s' % escaped_fields)  # escaped_fields: ['`name`', '`email`', '`password`']

        attrs['__mappings__'] = mappings
        attrs['__table__'] = table_name
        attrs['__primary_key__'] = primary_key
        attrs['__fields__'] = fields
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primary_key, ', '.join(escaped_fields), table_name)
        attrs['__insert__'] = 'insert into `%s`(`%s`, `%s`) values (%s)' % (table_name, primary_key, ', '.join(escaped_fields), ', '.join(['?'] * (len(escaped_fields) + 1)))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (table_name, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primary_key)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (table_name, primary_key)
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

    def get_value(self, key):
        return getattr(self, key, None)

    def get_value_or_default(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                setattr(self, key, value)
        return value

    def find(self, pk):
        """find object by primary key. """
        rs = '%s = %s' % (self.__select__, pk)
        return rs

    def save(self):
        args = []
        args.append(self.get_value_or_default(self.__primary_key__))
        args.extend(list(map(self.get_value_or_default, self.__fields__)))
        print(args)
        print(self.__insert__)


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()
    email = StringField('email')
    password = StringField('password')


user = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
print(user.find(10))
user.save()
