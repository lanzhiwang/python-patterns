python-patterns
===============

A collection of design patterns and idioms惯用语法 in Python.

When an implementation is added or modified, be sure to update this file and
rerun重新运行 `append_output.sh` (eg. ./append_output.sh borg.py) to keep the output
comments at the bottom up to date.

Current Patterns:     

__Creational Patterns__: 创作模式

| Pattern | Description |
|:-------:| ----------- |
| [abstract_factory](creational/abstract_factory.py) 抽象工厂模式 | use a generic function with specific factories |
| [borg or Monostate](creational/borg.py) 伯格模式 or 单态模式 | a singleton with shared-state among instances 实例之间具有共享状态的单例 |
| [builder](creational/builder.py) 生成器模式 | instead of using multiple constructors, builder object receives parameters and returns constructed objects 生成器对象不使用多个构造函数，而是接收参数并返回构造的对象 |
| [factory_method](creational/factory_method.py) 工厂方法模式 | delegate a specialized function/method to create instances 委托专门的功能/方法来创建实例 |
| [lazy_evaluation](creational/lazy_evaluation.py) 延迟计算 | lazily-evaluated property pattern in Python |
| [pool](creational/pool.py) 对象池模式 | preinstantiate and maintain a group of instances of the same type 预先实例化并维护一组相同类型的实例 |
| [prototype](creational/prototype.py) 原型模式 | use a factory and clones of a prototype for new instances (if instantiation is expensive) 使用工厂和原型的克隆用于新实例（如果实例化非常昂贵） |

__Structural Patterns__: 结构模式

| Pattern | Description |
|:-------:| ----------- |
| [3-tier](structural/3-tier.py) 三层架构模式 | data<->business logic<->presentation separation (strict relationships) |
| [adapter](structural/adapter.py) 适配器模式 | adapt one interface to another using a white-list |
| [bridge](structural/bridge.py) 桥接模式 | a client-provider middleman to soften interface changes |
| [composite](structural/composite.py) 组合模式 | lets clients treat individual objects and compositions uniformly |
| [decorator](structural/decorator.py) 装饰器模式 | wrap functionality with other functionality in order to affect outputs |
| [facade](structural/facade.py) 外观模式 | use one class as an API to a number of others |
| [flyweight](structural/flyweight.py) 享元模式 | transparently reuse existing instances of objects with similar/identical state |
| [front_controller](structural/front_controller.py) 前端控制器模式 | single handler requests coming to the application |
| [mvc](structural/mvc.py) | model<->view<->controller (non-strict relationships) |
| [proxy](structural/proxy.py) 代理模式 | an object funnels operations to something else |

__Behavioral Patterns__: 行为模式

| Pattern | Description |
|:-------:| ----------- |
| [chain_of_responsibility](behavioral/chain_of_responsibility.py) 责任链模式 | apply a chain of successive handlers to try and process the data |
| [catalog](behavioral/catalog.py) 设计目录模式 | general methods will call different specialized methods based on construction parameter |
| [chaining_method](behavioral/chaining_method.py) | continue callback next object method |
| [command](behavioral/command.py) 命令模式 | bundle a command and arguments to call later |
| [iterator](behavioral/iterator.py) 迭代器模式 | traverse a container and access the container's elements |
| [mediator](behavioral/mediator.py) 中介者模式 | an object that knows how to connect other objects and act as a proxy |
| [memento](behavioral/memento.py) 备忘录模式 | generate an opaque token that can be used to go back to a previous state |
| [observer](behavioral/observer.py) 观察者模式 | provide a callback for notification of events/changes to data |
| [publish_subscribe](behavioral/publish_subscribe.py) 发布订阅模式 | a source syndicates events/data to 0+ registered listeners |
| [registry](behavioral/registry.py) 注册模式 | keep track of all subclasses of a given class |
| [specification](behavioral/specification.py) ~~规格模式~~ |  business rules can be recombined by chaining the business rules together using boolean logic |
| [state](behavioral/state.py) 状态模式 | logic is organized into a discrete number of potential states and the next state that can be transitioned to |
| [strategy](behavioral/strategy.py) 策略模式 | selectable operations over the same data |
| [template](behavioral/template.py) 模板模式 | an object imposes a structure but takes pluggable components |
| [visitor](behavioral/visitor.py) 访问者模式 | invoke a callback for all items of a collection |

__Design for Testability Patterns__:

|                 Pattern                 | Description                                                  |
| :-------------------------------------: | ------------------------------------------------------------ |
| [setter_injection](./dft/) 依赖注入模式 | the client provides the depended-on object to the SUT via the setter injection (implementation variant of dependency injection) |

__Fundamental Patterns__:

|                           Pattern                            | Description                                                  |
| :----------------------------------------------------------: | ------------------------------------------------------------ |
| [delegation_pattern](fundamental/delegation_pattern.py) 委派模式 | an object handles a request by delegating to a second object (the delegate) |

__Others__:

| Pattern | Description |
|:-------:| ----------- |
| [blackboard](other/blackboard.py) 黑板模式 | architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern |
| [graph_search](other/graph_search.py) 图搜索模式 | graphing algorithms - non gang of four pattern |
| [hsm](other/hsm/hsm.py) hierarchical state machine 层次状态机 | hierarchical state machine - non gang of four pattern |

__web  框架中间件实现方法__:

[Middleware](./middleware/)
