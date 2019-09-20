from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper, relationship

metadata = MetaData()

user = Table('user', metadata,
	Column('id', Integer, primary_key=True),
	Column('name', String),
	Column('fullname', String),
	Column('password', String)
	)

address = Table('address', metadata,
	Column('id', Integer, primary_key=True),
	Column('user_id', Integer, ForeignKey('user.id')),
	Column('email_address', String)
	)

class User(object):
	pass

class Address(object):
	pass

print(dir(User))

mapper(
	User, user,
	properties={
		'addresses': relationship(Address, backref='user',
			order_by=address.c.id)
	})

print("*" * 40)

print(dir(User))

mapper(Address, address)