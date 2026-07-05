# https://youtu.be/ftVI8ILTRA4
from pydantic import BaseModel
from typing import Literal

regular = Literal["in-stock", "on-loan"]
extra = Literal["in-repair"]

class Car(BaseModel):
    status: regular | extra  # Literal["in-stock", "on-loan"]

# car = Car(status="abc")
car = Car(status="in-stock")