
# Project Questions

## answer the following questions

### 1. What is the difference between a class and an object?

A class a the blueprint which an object is instantiated from.

### 2. Why did we use LanguageModel as an abstract class?

So our code does not depend on a hard class implementation and it become easy to change.

### 3. What is the purpose of super()?

To access parent class properties and methods

### 4. What is the difference between inheritance and composition?

Inheritance takes the parent properties and and methods directly into the child class.
Composition is using an object from another class.

### 5. What is the difference between composition and aggregation?

composition is when create object of different class internally, while aggregation is passing the reference from outside

### 6. Where does polymorphism appear in the project?

``` models = [gpt, llama]
    for model in models:
        try:
            print(model.generate_response("Explain OOP"))
        except InvalidPromptError as e:
            print(e)
```

### 7. What is the difference between a class attribute and an instance attribute?

Class Attributes are common attribute for all objects, instance attribute is special to each instance

### 8. Why did we use @property?

To create a getter for private attributes.

### 9. When should we use a static method?

When the method does not need to be called only on instance attributes, without changing class attributes.

### 10. When should we use a class method?

When we have to change class attributes.

### 11. Why did we override generate_response()?

To have a specif behavior for the child class.

### 12. What is the purpose of __str__ and __repr__?

__str__ is a simpler repression, while __repr__ is for developers.

### 13. Why did we create a custom exception?

To show custom error

### 14. What problem does ModelManager solve?

Group all models together, to run operations on them.

### 15. How could this project be connected to a real API later?

Either by using already built abstraction frameworks or libraries, or implementing them.
