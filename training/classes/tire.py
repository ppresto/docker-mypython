import math

class Tire:
    """
    Tire represents a tire that would be used with an automobile
    """

    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def circumference(self):
        """
        The circumference of the tire in inches.
        Below is a doctest. Run this using: 'python3.7 -m doctest -v tire.py'
        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        # mill / 25.4 = inches
        # diameter * pi = circumference
        #side_wall_inches = (self.width * (self.ratio / 100)) / 25.4
        total_diameter = self._side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        """
        Represents the Tire information in standard notation present on the side of a tire.  Example: 'P215/65R15'
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}"
                + f"{self.construction}{self.diameter}")

    def _side_wall_inches(self):
        """ internal to the class to reuse code """
        return (self.width * (self.ratio / 100)) / 25.4

class SnowTire(Tire):
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        """
        Inherit the Tire __init__ variables and just add 1 for snow tires called chain_thickness.  We could
        also do this explicitly calling the Tire class often seen in Python 2 like here.
        Tire.__init__(self, tire_type, width, ration, diameter, brand, construction)

        We can also use super()
        """
        super().__init__(tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness

    def circumference(self):
        """
        The circumference of a tire with snow chains in inches
        >>> tire = SnowTire('P', 205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        """
        total_diameter = (self._side_wall_inches() + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        """
        super will call parent __repr__ method and allow us to add something additional to it.
        """
        return super().__repr__() + " (Snow)"
