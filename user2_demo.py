# https://youtu.be/wTHq_5jZmmY
from typing import Optional, List

from pydantic import BaseModel

# default: if not passed in, set to some value
# optional: allows you to pass None
class User(BaseModel):
    """ a class to represent a simple user """
    name: str
    age: int
    passed_induction: bool
    # years_service: int = 0  # if not provided, set it to 0; cannot pass None
    # Optional lets us pass None instead of an int
    # years_service: Optional[int]  # you must pass a value, which can be None
    # years_service: Optional[int] = 0  # if you don't pass a value, it will be 0; you can pass None
    years_service: int | float | str  # can't pass None; can pass 1, 1.5, "1 week"
    awards: List[str | int]

# user1 = User(name="john", age=36, passed_induction=True)  # , years_service=None)
#print(user1)
# user2 = User(name="john", age=36, passed_induction=True, years_service=None)
#print(user2)
# for val in [1, 1.5, "1 week"]:
#     user3 = User(name="john", age=36, passed_induction=True, years_service=val)
#     print(user3)

user4 = User(name="john", age=36, passed_induction=True, years_service=1, awards=["award1", "award2", 5])
print(user4)


# print(dir(User))

