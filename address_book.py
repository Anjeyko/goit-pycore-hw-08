from collections import UserDict
from datetime import datetime, timedelta

DATE_FORMAT = "%d.%m.%Y"

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        try:
            record = self.data[name]
            return record
        except KeyError:
            return None

    def delete(self, name):
        try:
            del self.data[name]
            print(f"Contact {name} deleted")
        except KeyError:
            return f"There is no contanct with name {name}"
    
    def get_upcoming_birthdays(self):
        current_dt = datetime.today().date()
        arr = []
        for name, record in self.data.items():
            if record.birthday:
                date = record.birthday.value.replace(year=current_dt.year).date()

                if date < current_dt:
                    arr.append({'name': name, 'congratulation_date': (date + timedelta(365)).strftime(DATE_FORMAT)})
                elif (date - current_dt) <= timedelta(7):
                    if date.weekday() > 4:
                        if date.weekday() == 5:
                            arr.append({'name': name, 'congratulation_date': (date + timedelta(2)).strftime(DATE_FORMAT)})
                        else:
                            arr.append({'name': name, 'congratulation_date': (date + timedelta(1)).strftime(DATE_FORMAT)})
                    else:
                        arr.append({'name': name, 'congratulation_date': date.strftime(DATE_FORMAT)})
        return arr  
                