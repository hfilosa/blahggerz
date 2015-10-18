import shelve, sqlite3

def authenticate(uname,pword):
	conn = sqlite3.connect("userList.db")
	c = conn.cursor()
	q = 'SELECT usersList.user FROM usersList WHERE usersList.pass = %(user)s'
	userN = str(uname)
	passW = str(pword)
	result = c.execute('SELECT DISTINCT usersList.pass FROM usersList WHERE usersList.user = ?', (userN,))
	#result = c.execute('SELECT DISTINCT usersList.user FROM usersList WHERE usersList.user == ? AND usersList.pass == ?', cred)
	for x in result:
		if x == passW:
			return "success"
		return "fail"
	return "noUser"
	conn.commit()
	conn.close()
	
	#itWorked = False
	#s = shelve.open('users.db')
	##user = str(uname)
	#account = s.has_key(user)
	#if (account and s[user]["password"] == pword):
	#	itWorked = True
	#else:
	#	itWorked = False
	#s.close()
	#return itWorked

def add(uname, pword):
	response = "failed"
	s = shelve.open('users.db', writeback = True)
	user = str(uname)
	password = str(pword)
	if s.has_key(user):
		response = "taken"
	else:
		s[user] = {'password' : password}
		response = "success"
	s.close()
	return response
		
	
	