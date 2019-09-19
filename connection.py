from sqlalchemy import create_engine

# connection to DB
e = create_engine('sqlite:///some.db', echo=True)

# in memory
# e = create_engine('sqlite:///:memory:', echo=True)

# transaction
connection = e.connect()

trans = connection.begin()

connection.execute('insert into employee (emp_name) values (:emp_name)', emp_name='wendy')

trans.commit()

result = connection.execute('select * from employee')

print(result.fetchall())

connection.close()

# trans.close()		# rollback 
# trans.commit()	# confirm tr
# trans.rollback()	# cancel