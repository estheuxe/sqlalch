from sqlalchemy import String, Numeric, DateTime, Integer
from sqlalchemy import Enum, Table, MetaData, Column
from sqlalchemy import create_engine, Index
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy import inspect
from sqlalchemy.dialects import sqlite
from sqlalchemy import select
import os

if os.path.exists('some.db'):
	os.remove('some.db')

e = create_engine('sqlite:///some.db', echo=True)

metadata = MetaData()

# ************************************************************
# creating table______________________________________________

fancyTable = Table('fancy', metadata,
	Column('key', String(50), primary_key=True),	
	Column('timestamp', DateTime),
	Column('amount', Numeric(10, 2)),
	Column('type', Enum('a', 'b', 'c'))
)

# fancyTable.create(e)		# but i use metadata.create_all(e)
# print(fancy_table.c)________________________________________
# ************************************************************
# setting indexes_____________________________________________

myTable = Table('mytable', metadata,
	# an indexed column, with index "ix_mytable_col1"
	Column('col1', Integer, index=True),
	
	# a uniquely indexed column with index "ix_mytable_col2"
	Column('col2', Integer, index=True, unique=True),
	
	Column('col3', Integer),
	Column('col4', Integer),
	
	Column('col5', Integer),
	Column('col6', Integer),
)

Index('idx_col34', myTable.c.col3, myTable.c.col4)

Index('myindex', myTable.c.col5, myTable.c.col6, unique=True)
# _____________________________________________________________
# *************************************************************
# foreign keys_________________________________________________

userTable = Table('user', metadata,
	Column('id', Integer, primary_key=True),
	Column('name', String)
)

addressesTable = Table('address', metadata,
	Column('id', Integer, primary_key=True),
	Column('email_address', String(100), nullable=False),
	Column('user_id', Integer, ForeignKey('user.id')) # a mojno ForeignKeyConstraint
)

anotherOneTable = Table('another', metadata,
	Column('id', Integer, primary_key=True),
	Column('name', String),
	Column('another name', String),
	Column('another_id', Integer),
	ForeignKeyConstraint(
			['id', 'another_id'],
			['address.id', 'address.user_id']
		)
)
# ______________________________________________________________
# **************************************************************
# creating
metadata.create_all(e)

# dropping(deleting) of table
myTable.drop(e)

# reflexion
# user_reflected = Table('user', metadata, autoload=True, autoload_with=e)

print(userTable.c)		# not displayed

metadata.reflect(bind=e)

# after reflect
print(addressesTable.c) # displayed

# introspection (to determine types etc.)
inspector = inspect(e)

print(inspector.get_table_names())

print(inspector.get_columns('address'))

print(inspector.get_foreign_keys('another'))

print("\n\n\n" + "*" * 30 + "\n\n\n")

e.execute('''insert into user(name) values ('ed')''')
e.execute('''insert into user(name) values ('ped')''')
e.execute('''insert into user(name) values ('hed')''')

# compilation__________________________________________

expression = userTable.c.name + 'ed'
compiled = expression.compile(dialect=sqlite.dialect())
print(compiled.params)
#______________________________________________________

# SELECT________________________________________________________________

select_stmt = select([userTable]).order_by(userTable.c.name)
# or select([userTable.c.name]).where(userTable.c.name == 'ed')

connection = e.connect()

#result = connection.execute(select_stmt)

#for rrr in result:
#	print(rrr)

print(connection.execute(select_stmt).fetchall())

# https://lectureswww.readthedocs.io/6.www.sync/2.codding/9.databases/2.sqlalchemy/2.sql_expressions.html#insert