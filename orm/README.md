# Object Relational Mapping(ORM)

#### 实现ORM思路:
1. 定义类来操作对应的数据表，例如定义一个User类来操作对应的数据库表User
2. 实例化User类时要将类中定义的相关属性进行读取和修改，从元类的attrs参数中读取
3. 在类中要生成相应的SQL语句

#### 实现ORM要点:
1. 使用metaclass读取和修改类定义信息
2. 最后输出相应的SQL语句用于执行


