from peewee import *

db = SqliteDatabase('cats.sqlite')

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.color}, {self.age}'

db.connect()
db.create_tables([Cat])

Cat.delete().execute() # Clear database

zoe = Cat(name='Zoe', color='Ginger', age=3)
zoe.save()

holly = Cat(name='Holly', color='Tabby', age=5)
holly.save()

fluffy = Cat(name='Fluffy', color='Black', age=1)
fluffy.save()

cats = Cat.select()
for cat in cats:
    print(cat)

list_of_cats = list(cats)

""" CRUD Operations
Create - insert
READ - select
UPDATE - 
DELETE
"""

fluffy.age = 2
fluffy.save()
print('After fluffy birthday')
cats = Cat.select()
for cat in cats:
    print(cat)


Cat.update(age=6).where(Cat.name =='Holly').execute() # Cam update many rows if needed
print('After Holly birthday')
cats = Cat.select()
for cat in cats:
    print(cat)

# print(rows_modified) ??

buzz = Cat(name='Buz', color='Gray', age=3)
buzz.save()

cats_who_are_3 = Cat.select().where(Cat.age == 3)
for cat in cats_who_are_3:
    print(cat, 'is three')

cats_with_l_in_name = Cat.select().where(Cat.name % '*l*')
for cat in cats_with_l_in_name:
    print(cat, ' has l in name')

cats_with_b_in_name = Cat.select().where(Cat.name.contains('b'))
for cat in cats_with_b_in_name:
    print(cat, ' has b in name')

zoe_from_db = Cat.get_or_none(name='Zoe')
print(zoe_from_db)

cat_1 = Cat.get_by_id(Cat.id == 1)
print(cat_1)

total = Cat.select().count()
print(total)

total_cats_who_are_5 = Cat.select().where(Cat.age == 5).count()
print(total_cats_who_are_5)

cats_by_name = Cat.select().order_by(Cat.name)
print(list(cats_by_name))

cats_by_age = Cat.select().order_by(Cat.age.desc(), Cat.name.desc())
print(list(cats_by_age))

first_3 = Cat.select().limit(3)
print(list(first_3))


# Delete
rows_delete = Cat.delete().where(Cat.name == 'Holly').execute()
print(rows_delete, list(Cat.select()))