from faker import Faker
from classes_test import Updater


fake = Faker("en_UK")
seed = 1

Faker.seed()
name = fake.name()
filename = name.split()[-1]

Faker.seed()
address = fake.address()

print(name)
print(filename)

#orginal file, in allow, updated
test1 = Updater() 
test1.add_file_to_originals(filename, name, address)
test1.add_to_allowlist(filename)
test1.add_file_to_updates(filename, name, fake.address())
##expect updated file in finals

#orginal file, in drop, updated
test2 = Updater() 
test2.add_file_to_originals(filename, name, address)
test2.add_to_droplist(filename)
test2.add_file_to_updates(filename, name, fake.address())
##expect updated file in finals


#orginal file, in drop, not updated
test3 = Updater() 
test3.add_file_to_originals(filename, name, address)
test3.add_to_droplist(filename)
##expect nothing in finals


#orginal file, in allow, not updated
test4 = Updater() 
test4.add_file_to_originals(filename, name, address)
test4.add_to_allowlist(filename)
##expect original file in finals

#no original file, in drop, updated
test5 = Updater()
test5.add_to_droplist(filename)
test5.add_file_to_updates(filename, name, fake.address())
##expect updated file in finals

#original file, different name in drop
test6 = Updater() 
test6.add_file_to_originals(filename, name, address)
test6.add_to_droplist("Hello")

#original file, different name in allow
test7 = Updater() 
test7.add_file_to_originals(filename, name, address)
test7.add_to_allowlist("Hello")

