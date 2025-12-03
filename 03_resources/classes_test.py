import os
class Updater(): 

    def __init__(self):
        self.file_path_allow = "/Users/romeenrg/Projects/Testing_skills/challenge/03_resources/target_directory/allowlist"
        self.file_path_drop = "/Users/romeenrg/Projects/Testing_skills/challenge/03_resources/target_directory/droplist"
    pass

    def add_file_to_originals (self, filename, name, address):
        file_path_originals = "/Users/romeenrg/Projects/Testing_skills/challenge/03_resources/target_directory/originals/" + filename
        with open(file_path_originals, 'w') as file:
            file.write(f"{name}\n")
            file.write(address)
            return

    def add_file_to_updates (self, filename, name, address):
        file_path_updates = "/Users/romeenrg/Projects/Testing_skills/challenge/03_resources/target_directory/updates/" + filename
        with open(file_path_updates, 'w') as file:
            file.write(f"{name}\n")
            file.write(address)
            return



    def add_to_droplist (self, names):
            if os.path.exists(self.file_path_allow):
                os.remove(self.file_path_allow)

            
            with open(self.file_path_drop, 'w') as file:
                file.writelines(f"{name}\n" for name in names) 
            return  

    def add_to_allowlist (self, names):
        if os.path.exists(self.file_path_drop):
                os.remove(self.file_path_drop)
        
        with open(self.file_path_allow, 'w') as file:
                file.writelines(f"{name}\n" for name in names)
            
    

    def clear_filenames(self, filenames):

        if os.path.exists(self.file_path_allow):
                os.remove(self.file_path_allow)

        if os.path.exists(self.file_path_drop):
                os.remove(self.file_path_drop)

        for i in range(len(filenames)):
            filepath1 = "/Users/romeenrg/Projects/Testing_skills/challenge/03_resources/target_directory/originals/" + filenames[i]
            if os.path.exists(filepath1):
                os.remove(filepath1)

            filepath2 = "/Users/romeenrg/Projects/Testing_skills/challenge/03_resources/target_directory/updates/" + filenames[i]
            if os.path.exists(filepath2):
                os.remove(filepath2)

            

            finalspath = "/Users/romeenrg/Projects/Testing_skills/challenge/03_resources/target_directory/finals/" + filenames[i]
            if os.path.exists(finalspath):
                os.remove(finalspath)

