import json
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ValidationError


# 1. Define the schema
class Organization(BaseModel):
    name: str
    address: Optional[str] | None = None
    city: str | None = None
    state: str | None = None
    zipcode: str | None = None


class User(BaseModel):
    # if there is no default value, the property is required
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    organization: Optional[list[Organization]] = None
    friends: list[int] = []


# 2. Validate incoming data (e.g., from an API or database)
external_data: list[dict] = [{
    'id': '123',  # Pydantic automatically coerces this string into an integer
    'signup_ts': '2017-06-01 12:22',  # Coerced into a datetime object
    'friends': [1, '2', b'3'],  # Coerced into a list of integers
    'organization': [{
        'name': 'Acme Inc.',
    }]
},
    {
        'id': '112',  # Pydantic automatically coerces this string into an integer
        'signup_ts': '2017-06-01 12:22',  # Coerced into a datetime object
        'friends': [21, '12', 32],  # Coerced into a list of integers
        'organization': [{
            'name': 'Zerox Inc.',
            'address': '1223 Bud Doggett\'s Way',
            'city': 'New York',
            'alias': [
                "Zerox",
                "Zero",
                "Z-Funk"
            ]
        }]
    },
    {
        # 'id': '123',  # Pydantic automatically coerces this string into an integer
        'signup_ts': datetime.now(),  # Coerced into a datetime object
        'friends': [211, '112', b'1113'],  # Coerced into a list of integers
        'organization': [{
            'name': 'Acme Inc.',
        }]
    },
]

for index, item in enumerate(external_data):
    try:
        user: User = User(**item)
        # print(f"{user.id=}")  # Output: 123
        print(f"Item {index} is valid, apparently:")
        print(f"{user=}")
        user_dump: dict = user.model_dump()
        print(f"{user_dump=}")

    except ValidationError as e:
        print(f"Item {index} is not valid, apparently:")
        error_json_string: str = e.json()
        error_list = json.loads(error_json_string)
        # print(f"{error_list=}")
        for error_index, error in enumerate(error_list):
            print(f"{error_index=}: {error=}")
        print(f"{e=}")
