from faker import Faker
import os
class Updater(): 

    def __init__(self):
        self.file_path_allow = "/Users/romeenrg/Projects/Testing_skills/extending-testing-resources/unit2/03_resources/target_directory/allowlist"
        self.file_path_drop = "/Users/romeenrg/Projects/Testing_skills/extending-testing-resources/unit2/03_resources/target_directory/droplist"
    pass

    def add_file_to_originals (self, filename, name, address):
        file_path_originals = "/Users/romeenrg/Projects/Testing_skills/extending-testing-resources/unit2/03_resources/target_directory/originals/" + filename
        with open(file_path_originals, 'w') as file:
            file.write(f"{name}\n")
            file.write(address)
            return

    def add_file_to_updates (self, filename, name, address):
        file_path_updates = "/Users/romeenrg/Projects/Testing_skills/extending-testing-resources/unit2/03_resources/target_directory/updates/" + filename
        with open(file_path_updates, 'w') as file:
            file.write(f"{name}\n")
            file.write(address)
            return



    def add_to_droplist (self, f):
            if os.path.exists(self.file_path_allow):
                os.remove(self.file_path_allow)

            
            with open(self.file_path_drop, 'w') as file:
                file.write(f)
            return  



    def add_to_allowlist (self, f):
        if os.path.exists(self.file_path_drop):
                os.remove(self.file_path_drop)
        
        with open(self.file_path_allow, 'w') as file:
                file.write(f) 
        return 