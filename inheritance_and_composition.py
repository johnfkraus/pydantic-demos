# https://youtu.be/EQYzBmrPN1k

from pydantic import BaseModel

# inheritance - 'is a',
# composition - 'has a',

# our base class
class Vehicle(BaseModel):
    wheels: int
    age: int

class Motorbike(Vehicle):
    racing: bool  # true if a race bike

class Bus(Vehicle):
    passengers: int

# m = Motorbike(wheels=2, age=3, racing=True)
# print(m)
# b = Bus(wheels=8, age=10, passengers=50)
# print(b)

# Composition

class Address(BaseModel):
    street: str
    city: str

class Person(BaseModel):
    name: str
    age: int
    address: Address | dict

# p = Person(name="joe", age=36, address="123 main st")
p = Person(name="joe",
           age=36,
           address=Address(street="123 main st", city="nyc"))
print(p)

p2 = Person(name="joe",
           age=36,
           address={"street": "123 main st", "city": "nyc"})
print(p2)