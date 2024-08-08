from field import Field
    
class Phone(Field):
    def __init__(self, phone_number):
        try:
            self.value  = self.validation(phone_number)
        except ValueError:
            print("Phone should be 10 numbers only")


    def validation(self, number):
        if len(number) == 10 and number.isdigit():
            return number
        else:
            raise ValueError

