past_passwords = ['titanic1911','ibiza1972','montecarlo799']

class PasswordManager:
    
    def __init__(self, past_passwords):
        self.old_passwords = past_passwords
        
    def get_password(self):
        return self.old_passwords[-1]
    
    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password changed successfully!")
        else:
            print("Old password cannot be reused, try again")
            
    def is_correct(self, password_check):
        return password_check == self.old_passwords[-1]

# Practiing inheritance and updating methods in a class

class PasswordManagerUpdated(PasswordManager):     #inheriting PasswordManager class
    
    def __init__(self, past_passwords):            #constructor
        self.old_passwords = past_passwords
    
    def set_password(self, new_password):          #new method to set a password
        import string      
        for i in new_password:                     # checks if punctuation is present in the new password
            if i not in string.punctuation:
                punctuation = 0
            else:
                punctuation = 1
                break           
        if punctuation == 0:                       # if punctuation not present...
            if new_password not in self.old_passwords:    # and the new password is not an old one
                self.old_passwords.append(new_password)   # add as a new password
                print("Password changed successfully!")
            else:
                print("Old password cannot be reused, try again")
        else:                                    
            print("Cannot have punctuation in password, try again")
            
    def suggest_password(self):                    # new method to suggest a random password
        import string
        import random
        random_password = ''.join(random.choices(string.ascii_letters, k=15))     # generates a random string of 15 letters
        self.set_password(random_password)                                    # sets it as password if eligible
        return random_password                                                # returns the random password 

# Testing functionality below

past_passwords = PasswordManagerUpdated(past_passwords)

past_passwords.old_passwords
print(past_passwords.get_password())

past_passwords.set_password('ibiza1972')
print(past_passwords.get_password())

past_passwords.set_password('oktoberfest%2022')
print(past_passwords.get_password())

past_passwords.set_password('oktoberfest2022')
(past_passwords.get_password())

suggested_pass = past_passwords.suggest_password()
print(past_passwords.is_correct(suggested_pass))
