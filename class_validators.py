
from pydantic import BaseModel, model_validator
from typing import Optional

# class validation is context dependent;
# i.e., if one field is x, these other fields need to be y.
class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_passwords_match(self):
        print(f"{vars(self)=}")
        if self.password != self.confirm_password:
            print("oh no")
            raise ValueError("passwords do not match")
        return self

# user = User(password=1, confirm_password="abc")
# print(user)


class ItemToShip(BaseModel):
    name: str
    needs_shipping: bool
    shipping_address: Optional[str] = ""

    @model_validator(mode="after")
    def item_check(self):
        print(f"{vars(self)=}")
        if self.needs_shipping and not self.shipping_address:
             raise ValueError(f"Shipping address not provided for {self.name}.")
        return self


# item = ItemToShip(name="toy", needs_shipping=True, shipping_address="1 main street")
# item = ItemToShip(name="toy", needs_shipping=False)  # , shipping_address="")
# print(item)

class File(BaseModel):
    pass

class ItemToUpload(BaseModel):
    type_: str | File
    path:    Optional[str] = None

    @model_validator(mode="after")
    def path_check(self):
        if isinstance(self.type_, File) and (self.path is None or not self.path):
            raise ValueError("path not provided for file upload.")
        return self

# x1 = ItemToUpload(type_="hello")
# print(x1)
# x2 = ItemToUpload(type_ = File(), path="abc")
# print(x2)
x3 = ItemToUpload(type_ = File(), path="")
print(x3)
