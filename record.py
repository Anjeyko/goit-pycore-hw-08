from name import Name
from phone import Phone
from birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))
    
    def edit_phone(self, old_number, new_number):
       self.phones = [Phone(new_number) if phone.value == old_number else phone for phone in self.phones]

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                print("Phone removed")

    def find_phone(self, name):
        phone_numbers = []
        if self.name.value == name:
            for phone in self.phones:
               phone_numbers.append(phone.value)

        return phone_numbers
            
    def add_birthday(self, date):
        self.birthday = Birthday(date)
        return "Birthday added"
    
    def show_birthday(self):
        return self.birthday.value.date()
 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"