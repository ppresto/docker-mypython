# interactive mode
#
# python3.7 -i person.py
#   person = Person(first, last, age, bday)
#   family = [person, person, person, person]

class Person:
    """
    Person stores all personal info on an individual.
    """

    def __init__(self, first, last, age, bday):
        self.first = first or ""
        self.last = last or ""
        self.age = age or ""
        self.bday = bday or ""

    def setFirst(self, update):
        self.first = update

    def setLast(self, last):
        self.last = last

    def setAge(self, age):
        self.age = int(age)

    def setBday(self, bday):
        self.bday = str(bday)

    def desc(self):
        print(f"My name is {self.first} {self.last}. I was born on {self.bday} and I'm {self.age} years old.")
