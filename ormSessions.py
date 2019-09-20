from sqlalchemy.orm import Session

session = Session(bind=engine)

session.add(ed_user)

#	or

session.add_all([
	User(name='wendy', fullname='Wendy Weatthed'),
	User(name='mary', fullname='Mary Contrary'),
	User(name='fred', fullname='Fred Flinstone')
])

ed_user.fullname = 'Ed Jones'
session.dirty 	# shows edited data

session.new 	# new objects 

session.commit() 	# saves changes

session.rollback() 	# otkat