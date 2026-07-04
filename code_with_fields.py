# https://youtu.be/PAmSNMsQu8s

from pydantic import BaseModel, Field

# Fields add extra information and validation rules that to your model
# that plain type hints cannot express.

class Person(BaseModel):
    # three dots says it is required
    name: str = Field(..., min_length=5, max_length=10)
    age: int = Field(..., ge=1, le=100)  # default=36, gt=0)
    zipcode: str = Field(..., pattern=r'^\d{5}$')

person = Person(name="Trevor", age=10, zipcode="12345")
print(person)