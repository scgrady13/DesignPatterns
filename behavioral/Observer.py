from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, position):
        pass


class UserObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, position):
        print(f"{self.name} notified of new TA position: {position}")


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, position):
        pass


class TAPositionSystem(Subject):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, position):
        for observer in self.observers:
            observer.update(position)

    def add_ta_position(self, position):
        self.notify(position)


if __name__ == "__main__":
    ta_position_system = TAPositionSystem()

    student1 = UserObserver("Alice")
    student2 = UserObserver("Bob")

    ta_position_system.attach(student1)
    ta_position_system.attach(student2)

    ta_position_system.add_ta_position("Data Structures TA")
    # Output:
    # Alice notified of new TA position: Data Structures TA
    # Bob notified of new TA position: Data Structures TA

    ta_position_system.add_ta_position("Algorithms TA")
    # Output:
    # Alice notified of new TA position: Algorithms TA
    # Bob notified of new TA position: Algorithms TA
