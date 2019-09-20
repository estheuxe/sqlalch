from sqlalchemy import select
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()

e = create_engine('sqlite:///some.db', echo=True)

metadata = MetaData()

connection = e.connect()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	pw = Column(String)

	addresses = relationship("Address", backref="user",
		order_by="Address.id")

sel = select([User.name, User.fullname]).\
	where(User.name == 'ed').\
	order_by(User.id)

print(connection.execute(sel).fetchall())

#query = connection.query(User).filter(User.name == 'ed').order_by(User.id)
#query.all()