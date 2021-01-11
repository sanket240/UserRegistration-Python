import re


class UserRegistration:
    def __init__(self):
        self.name = "^[A-Z][a-zA-Z]{2,}$"

    def get_first_name(self, first_name_input):
        if re.match(self.name, first_name_input):
            print("Valid first name")
            return "Happy"
        else:
            print("Invalid first name ")
            return "Sad"
