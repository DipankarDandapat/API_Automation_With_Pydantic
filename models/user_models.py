from pydantic import BaseModel, EmailStr

class Geo(BaseModel):
    lat: str
    lng: str

class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo

class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str

class User(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    address: Address
    phone: str
    website: str
    company: Company


class UserCreate(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr

class NewUser(BaseModel):
    name: str
    username: str
    email: EmailStr

