import shelve

def authenticate(uname,pword):
	itWorked = False
	s = shelve.open('users.db')
	user = str(uname)
	account = s.has_key(user)
	if (account and s[user]["password"] == pword):
		itWorked = True
	else:
		itWorked = False
	s.close()
	return itWorked

def add(uname, pword):
	response = "failed"
	s = shelve.open('users.db', writeback = True)
	user = str(uname)
	password = str(pword)
	if (s.has_key(user)):
		return "taken"
	else:
		s[user] = {'password' : password}
		response = "success"
	s.close
	return response
		
	
	