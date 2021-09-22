"""
A menu - you need to add the database and fill in the functions. 
"""
from peewee import *

db = SqliteDatabase('records.sqlite')

class Record(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.country}, {self.catches}'


def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    db.connect()
    db.create_tables([Record])

    # Test data
    # Record.delete().execute()

    # tom = Record(name='Tom', country='USA', catches=43)
    # tom.save()

    # zoe = Record(name='Zoe', country='UK', catches=10)
    # zoe.save()

    # bob = Record(name='Bob', country='China', catches=38)
    # bob.save()

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    # print('todo display all records')
    records = Record.select()
    if records:
        for record in records:
            print(record)
    else:
        print("There are no records in the database")


def add_new_record():
    # print('todo add new record. What if user wants to add a record that already exists?')
    new_name = input('What is the name of the record holder? - ')
    name_in_db = Record.get_or_none(name=new_name)
    if name_in_db:
        print('A record already exists for this person in the database')
    else:
        new_country = input('What country are they from? - ')
        new_catches = int(input('What is the name of the record holder? - '))
        new_record = Record(name=new_name, country=new_country, catches=new_catches)
        new_record.save()


def edit_existing_record():
    # print('todo edit existing record. What if user wants to edit record that does not exist?') 
    edit_name = input('What is the name of the person whose record you wish to edit? - ')
    name_in_db = Record.get_or_none(name=edit_name)
    if name_in_db:
        new_number_of_catches = int(input('What is their new number of catches? - '))
        updated_record = Record.update(catches=new_number_of_catches).where(Record.name == edit_name).execute()
        # print(updated_record)
    else:
        print('Sorry, no record found in the database with that name.')


def delete_record():
    # print('todo delete existing record. What if user wants to delete record that does not exist?') 
    name_to_delete = input('What is the name of the record you would like to delete? - ')
    name_in_db = Record.get_or_none(name=name_to_delete)
    if name_in_db:
        rows_deleted = Record.delete().where(Record.name==name_to_delete).execute()
    else:
        print('This record does not exist in the database.')

        
if __name__ == '__main__':
    main()