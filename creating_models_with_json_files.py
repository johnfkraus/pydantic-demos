# https://youtu.be/wJJ32FJxY-8

import json
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    location: str

    @classmethod
    def make_person_from_json(cls, file_path: str) -> "Person":
        """ read in a json file, return a Person instance """
        with open(file_path) as file:
            return cls(**json.loads(file.read()))


person = Person.make_person_from_json("person.json")
print(person)

# with open("person.json") as file:
#     contents = json.loads(file.read())
#     person = Person(**contents)
#     # print(contents, type(contents))
#     print(person)

