# field validators
# https://youtu.be/QM98ehowhsQ
from pydantic import BaseModel, field_validator

class Person(BaseModel):
    """ a class to represent a simple person """
    #name: str
    f_name: str
    l_name: str
    age: int



    # @field_validator("name")
    # def name_must_be_valid(cls, v):
    #     if len(v) < 3:
    #         raise ValueError("Name must be at least 3 characters")
    #     return v

    @field_validator("age")
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Age must be positive")
        return v

    @field_validator("f_name", "l_name")
    # name gets passed in as n
    def check_name_is_alpha(cls, n):
        if not n.isalpha():
            raise ValueError("Name must be alphabetic")
        # we can modify the value to return
        return n.title()

# joe = Person(name="    ", age=36)
joe = Person(f_name="joe", l_name="smith", age=36)
print(joe)