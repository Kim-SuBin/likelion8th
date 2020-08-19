from faker import Faker

myfake = Faker()

print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.random_number())
print(myfake.sentence())