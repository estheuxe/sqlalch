from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

userTable = Table('user', metadata,
	Column('id', Integer, primary_key=True),
	Column('name', String),
	Column('fullname', String)
)

print(userTable.c) # columns (user.id, user.name, user.fullname)

print(userTable.c.name) # user.name

print(userTable.c.name.type) # VARCHAR

print(userTable.primary_key)

print("\n\n" + "*" * 30)

print(userTable.delete())