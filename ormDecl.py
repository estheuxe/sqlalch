from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	pw = Column(String)

	addresses = relationship("Address", backref="user",
		order_by="Address.id")

class Address(Base):
	__tablename__ = 'address'

	id = Column(Integer, primary_key=True)
	user_id = Column(ForeignKey('user.id'))
	email_address = Column(String)

address1 = Address(email_address="ghostous@example.com")
address2 = Address(email_address="merredit@example.com")
address3 = Address(email_address="kenstone@example.com")
address4 = Address(email_address="brighton@example.com")
address5 = Address(email_address="lesteron@example.com")
address6 = Address(email_address="gippoley@example.com")

user1 = User(name="Vasya", fullname="Vasily", pw="12345")
user1.addresses = [address1, address2]

user2 = User(name="Oleg", fullname="Olejka", pw="gangsta2")
user2.addresses = [address3, address4]

user3 = User(name="Vitaly", fullname="Vitaly Vyacheslavovich", pw="lookaround")
user3.addresses = [address5, address6]

print(address1.user.name)