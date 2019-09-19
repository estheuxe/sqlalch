from sqlalchemy import create_engine
import os

if os.path.exists('some.db'):
	os.remove('some.db')

e = create_engine('sqlite:///some.db', echo=True)

e.execute('''
	create table employee (
		emp_id integer primary key,
		emp_name varchar
	)
''')

e.execute('''
	create table employee_of_month (
		emp_id integer primary key,
		emp_name varchar
	)
''')

e.execute('''insert into employee(emp_name) values ('ed')''')
e.execute('''insert into employee(emp_name) values ('jack')''')
e.execute('''insert into employee(emp_name) values ('fred')''')

result = e.execute('''
	select emp_id, emp_name from 
	employee where emp_id=:emp_id
	''', emp_id=3)

result2 = e.execute('select * from employee')

row = result.fetchone()

print(row)

print(type(row)) # sqlalchemy.engine.result.RowProxy ALSO dict

print(row['emp_name'])

print("*" * 30)

print(result2.fetchall()) # list of dicts

result.close()

result2.close()