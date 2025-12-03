from faker import Faker
from classes_test import Updater

#source into venv

fake = Faker("en_UK")
names = []
filenames = []

Faker.seed(1)
for i in range(1):  # Change 2 to however many you need
    name = fake.name()
    names.append(name)
    filenames.append(name.split()[-1])

# address = fake.address()

# print(names)
# print(filenames)

#just code freestyle to generate data
test = Updater()

# test.clear_filenames(filenames)
test.add_file_to_originals(filenames[0], names[0], fake.address())


test.add_file_to_updates(filenames[0], names[0], fake.address())
test.add_to_allowlist("HELLO")

# test.clear_filenames(filenames)



# #orginal file, in allow, updated
# test1 = Updater() 
# test1.add_file_to_originals(filename, name, address)
# test1.add_to_allowlist(filename)
# test1.add_file_to_updates(filename, name, fake.address())
##expect updated file in finals

# #orginal file, in drop, updated
# test2 = Updater() 
# test2.add_file_to_originals(filename, name, address)
# test2.add_to_droplist(filename)
# test2.add_file_to_updates(filename, name, fake.address())
# ##expect updated file in finals


# # orginal file, in drop, not updated
# test3 = Updater() 
# test3.add_file_to_originals(filename, name, address)
# test3.add_to_droplist(filename)
# #expect nothing in finals


# #orginal file, in allow, not updated
# test4 = Updater() 
# test4.add_file_to_originals(filename, name, address)
# test4.add_to_allowlist(filename)
# ##expect original file in finals

# #no original file, in drop, updated
# test5 = Updater()
# test5.add_to_droplist(filename)
# test5.add_file_to_updates(filename, name, fake.address())
# ##expect updated file in finals

# #original file, different name in drop
# test6 = Updater() 
# test6.add_file_to_originals(filename, name, address)
# test6.add_to_droplist("Hello")


#original file, different name in allow
# test7 = Updater() 
# test7.add_file_to_originals(filename, name, address)
# test7.add_to_allowlist("Hello")

# original file, no allow or drop list
# test8 = Updater() 
# test8.add_file_to_originals(filename, name, address)


# #no allow or drop list, updated file
# test9 = Updater() 
# test9.add_file_to_updates(filename, name, address)

# original file, different name in allow, updated file
# test10 = Updater() 
# test10.add_file_to_originals(filename, name, address)
# test10.add_to_allowlist("Hello")
# test10.add_file_to_updates(filename, name, fake.address())

# original file, different name in allow, updated file
# test11 = Updater() 
# test11.add_file_to_originals(filename, name, address)
# test11.add_to_droplist("Hello")
# test11.add_file_to_updates(filename, name, fake.address())

# original file, different name in allow, updated file
# test12 = Updater() 
# test12.add_file_to_originals(filename, name, address)
# test12.add_file_to_updates(filename, name, fake.address())

# #multiple files in original, all same files in drop, all updated files in updated
# test13 = Updater() 
# test13.add_file_to_originals(filename, name, fake.address())
# test13.add_file_to_originals(filename2, name2, fake.address())

# test13.add_to_allowlist(filename, filename2)

# test13.add_file_to_updates(filename, name, fake.address())
# test13.add_file_to_updates(filename2, name2, fake.address())


#just code freestyle to generate data
# test = Updater()
# for _ in range (10):
    
#     Faker.seed(1)
#     test.add_file_to_originals(filename, name, fake.address())
#     test.add_file_to_originals(filename2, name2, fake.address())

#     test.add_to_droplist(filename, filename2)

#     test.add_file_to_updates(filename, name, fake.address())
