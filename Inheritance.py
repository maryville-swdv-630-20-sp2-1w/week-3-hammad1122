class Vehicle:

    def __init__(self, make, model):

        self.make = make

        self.model = model

class Car(Vehicle):

    def __init__(self, make, model, mileage):

        Vehicle.__init__(make, model)

        self.mileage = mileage

class Bus(Vehicle):

    def __init__(self, make, model, capacity):

        Vehicle.__init__(make, model)

        self.capacity = capacity

class Truck(Vehicle):

    def __init__(self, make, model, size):

        Vehicle.__init__(make, model)

        self.size = size
            