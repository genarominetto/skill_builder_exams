creational_patterns_participants = {
    "Singleton": "Singleton",
    "Factory Method": "Creator, ConcreteCreator, Product, ConcreteProduct",
    "Abstract Factory": "AbstractFactory, ConcreteFactory, AbstractProduct, ConcreteProduct, Client",
    "Builder": "Builder, ConcreteBuilder, Director, Product",
    "Prototype": "Prototype, ConcretePrototype, Client"
}

structural_patterns_participants = {
    "Adapter": "Target, Adapter, Adaptee, Client",
    "Bridge": "Abstraction, RefinedAbstraction, Implementor, ConcreteImplementor",
    "Composite": "Component, Leaf, Composite, Client",
    "Decorator": "Component, ConcreteComponent, Decorator, ConcreteDecorator",
    "Facade": "Facade, Subsystem classes",
    "Flyweight": "Flyweight, ConcreteFlyweight, NonSharedConcreteFlyweight, FlyweightFactory, Client",
    "Proxy": "Subject, RealSubject, Proxy"
}

behavioral_patterns_participants = {
    "Observer": "Subject, Observer, ConcreteSubject, ConcreteObserver",
    "Strategy": "Strategy, ConcreteStrategy, Context",
    "Command": "Command, ConcreteCommand, Client, Invoker, Receiver",
    "State": "Context, State, ConcreteState",
    "Template Method": "AbstractClass, ConcreteClass",
    "Chain of Responsibility": "Handler, ConcreteHandler, Client",
    "Iterator": "Iterator, ConcreteIterator, Aggregate, ConcreteAggregate",
    "Mediator": "Mediator, ConcreteMediator, Colleague, ConcreteColleague",
    "Memento": "Memento, Originator, Caretaker",
    "Interpreter": "AbstractExpression, TerminalExpression, NonterminalExpression, Context, Client",
    "Visitor": "Visitor, ConcreteVisitor, Element, ConcreteElement, ObjectStructure"
}
