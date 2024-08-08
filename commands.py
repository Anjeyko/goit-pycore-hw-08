from record import Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return f"There is no contact with name {args[0][0]}."
        except IndexError:
            return "Please provide corret args after command"
        except Exception as e:
            return f"Error occured: {e}"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
    if len(args) != 3:
        return "Incorrect input: Provide next args [name] [old_number] [new_number]"
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        return "Contact not found"

@input_error
def show_phone(args, book):
    name, *_ = args
    record = book.find(name)
    if record:
        return record.find_phone(name)
    else:
        return "Contact not found"
    
@input_error
def add_birthday(args, book):
    if len(args) != 2:
        return "Incorrect input: Provide next args [name] [date]"
    name, date = args
    record = book.find(name)
    if record:
        return record.add_birthday(date)
    else:
        return "Contact not found"

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record:
        return record.show_birthday()

@input_error
def birthdays(book):
    return book.get_upcoming_birthdays()

@input_error
def show_all(book):
    return '\n'.join(str(record) for record in book.data.values())