from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.email())
print(fake.address())
print(fake.administrative_unit())

data = {
    "name": fake.name(),
    "administrative_unit": fake.administrative_unit(),
    "address": fake.address(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=110)
}

print(data)


