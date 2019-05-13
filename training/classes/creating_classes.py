# Run python in interactive mode, import Tire classes, and create our car object
#
# python3.7 -i creating_classes.py
#   from tire import Tire, SnowTire
#   tire = SnowTire('P', 205, 65, 15, 2)
#   tires = [tire, tire, tire, tire]
#   honda = Car(tires=tires, engine="4-cyl")

#   A bound method needs to be called with ()
#   <bound method Car.description of <__main__.Car object at 0x10a03db00>>
#       honda.wheel_circumference()
#       honda.wheel_description()

class Car:
    """
    Docstring describing the class.
    Car models a car with tires and an engine
    """

    def __init__(self, engine, tires):
        """
        this __init__ method happens when we create a new instance of something.  Its a dunder or double under method (__)
        """
        self.engine = engine
        self.tires = tires
        #pass   #placehold for future functionality to avoid errors.

    def description(self):
        print(f"A car with an {self.engine} engine, and {self.tires} tires")

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0
