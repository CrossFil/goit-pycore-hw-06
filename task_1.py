from collections import UserDict

class Feild:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

class Name(Feild):
    pass

class Phone(Feild):
    def phone(self, number):
        if not isinstance(number, str) or not number.isdigital() or len(number) != 10:
            raise ValueError("Phone number must be a string of 10 digits.")
        super().__init__(number)


class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        print(f'Phone number {phone} not fount')

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, number):
        for p in self.phones:
            if p.value == number:
                return p
        return None

    def __str__(self):
        return f'Contact name: {self.name.value}, phone: {"; ".join(str(p.value) for p in self.phones)}'

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

if __name__ == '__main__':

    book = AddressBook()

    john_record = Record('John')
    john_record.add_phone('1234567890')
    john_record.add_phone('5555555555')
    book.add_record(john_record)

    jane_record = Record('Jane')
    jane_record.add_phone('9876543210')
    book.add_record(jane_record)

    for record in book.data.values():
        print(record)

    john = book.find('John')
    john.edit_phone('1234567890', '1112223333')
    john.remove_phone('5555555555')
    print(john)

    found_phone = john.find_phone('5555555555')
    print(f'{john.name}: {found_phone}')

    book.delete('Jane')



