import re


class UserRegistration:
    def __init__(self):
        self.first_name = "^[A-Z][a-zA-Z]{2,}$"
        self.last_name = "^[A-Z][a-zA-Z]{2,}$"
        self.email = "^[a-zA-z]{3}[0-9a-zA-Z\\.\\_\\-\\+]*@[a-z]*\\.(co|com.au|in|net|in|com.com|com|)$"

    def first_name_validation(self, first_name_input):
        if re.match(self.first_name, first_name_input):
            print("Valid first name")
            return "Happy"
        else:
            print("Invalid first name ")
            return "Sad"

    def last_name_validation(self, last_name_input):
        if re.match(self.last_name, last_name_input):
            print("Valid Last name")
            return "Happy"
        else:
            print("Invalid Last Name ")
            return "Sad"

    def email_validation(self, email_input):
        if re.match(self.email, email_input):
            print("Valid Email")
            return "Happy"
        else:
            print("Invalid Email ")
            return "Sad"
