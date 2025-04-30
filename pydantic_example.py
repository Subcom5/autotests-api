from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    #address: Address
    is_active: bool = Field(alias="isActive")

user_data = {
    "id": 1,
    'name': 'Name',
    'email': 'name@example.com',
    "isActive": True
}

user = User(**user_data)
print(user.model_dump())