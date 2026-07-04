#
from typing import Annotated
from pydantic import BaseModel, AfterValidator

def check_name(name: str) -> str:
    if len(name) < 1 or len(name) > 10:
        raise ValueError("Name must be between 1 and 10 characters")
    return name

# We define the name of our type, FirstName
# Annotated[] takes two things: base type and AfterValidator with a check parameter
FirstName = Annotated[str, AfterValidator(check_name)]

class Person(BaseModel):
    name: FirstName

a = Person(name="")
