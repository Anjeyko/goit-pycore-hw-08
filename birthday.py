from field import Field
from datetime import datetime

DATE_FORMAT = "%d.%m.%Y"

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
        return f"{self.value.strftime(DATE_FORMAT)}"