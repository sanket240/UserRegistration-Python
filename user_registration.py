import re


class UserRegistration:
    def __init__(self):
        self.first_name = "^[A-Z][a-zA-Z]{2,}$"
        self.last_name = "^[A-Z][a-zA-Z]{2,}$"

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
