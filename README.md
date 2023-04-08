# Design Pattern Project

This project demonstrates the usage of three design patterns: Factory Method, Adapter, and Observer. The purpose of these design patterns is to solve different problems in a TA management system.

## Design Patterns

### 1. Factory Method

**Scenario:** User role creation in the TA management system.

**Choice:** The Factory Method pattern is chosen because it allows the creation of User objects (Faculty, Student, and Staff) based on their roles without specifying their concrete classes. This provides flexibility and extensibility when adding new user roles in the future. The Factory Method pattern promotes loose coupling between the creator (UserFactory) and the products (User classes), making it easier to modify the user creation process or add new user roles without affecting other parts of the system. Additionally, this pattern simplifies the client code by encapsulating the object creation process within the factory.

### 2. Adapter

**Scenario:** Integrating an external authentication system into the TA management system.

**Choice:** The Adapter pattern is chosen to enable the TA management system to use an external authentication system without modifying its existing code. The AuthAdapter class acts as a bridge between the AuthSystem class and the ExternalAuth class, adapting the interface of the external authentication system to the one expected by the AuthSystem. This pattern allows for seamless integration of third-party systems with different interfaces, making it easier to switch between authentication providers or add new ones in the future. By encapsulating the differences between the two systems, the Adapter pattern promotes separation of concerns and improves maintainability of the code.

### 3. Observer

**Scenario:** Notifying students when new TA positions are available.

**Choice:** The Observer pattern is chosen to implement a subscription mechanism that allows students to receive notifications when new TA positions are added. This pattern enables a one-to-many dependency between the TAPositionSystem (Subject) and UserObserver (Observer) classes, ensuring that all subscribed students are notified of new TA positions without requiring tight coupling between the classes. The Observer pattern promotes loose coupling and separation of concerns by allowing the Subject to maintain a list of observers and notify them without knowing their concrete implementations. This makes it easy to add, remove, or modify observers without affecting the Subject or other observers. By decoupling the classes, the Observer pattern enhances the system's flexibility, maintainability, and extensibility.

## Running the code

1. Ensure you have Python 3 installed on your system.

2. Clone this repository or download the source code.

3. Open a terminal or command prompt and navigate to the directory containing the source code for either behavioral, creational, or structural

4. Run the desired script for each design pattern:

   - Creational -> python3 Factory.py
   - Structural -> python3 Adapter.py
   - Behavioral -> python3 Observer.py


5. Observe the output in the terminal or command prompt to see the results of each design pattern demonstration.
