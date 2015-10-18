import shelve, sqlite3

def authenticate(uname,pword):
	conn = sqlite3.connect("userList.db")
	c = conn.cursor()
	q = 'SELECT usersList.user FROM usersList WHERE usersList.pass = %(user)s'
	userN = str(uname)
	passW = str(pword)
	result = c.execute('SELECT DISTINCT usersList.pass FROM usersList WHERE usersList.user = ?', (userN,))
	#result = c.execute('SELECT DISTINCT usersList.user FROM usersList WHERE usersList.user == ? AND usersList.pass == ?', cred)
	return loginResponse(result, passW)
	conn.commit()
	conn.close()

def loginResponse(realPass, inputPass):
	for x in realPass:
		if x[0] == inputPass:
			return "success"
		return "fail"
	return "noUser"
	
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
	conn = sqlite3.connect("userList.db")
	c = conn.cursor()
	userN = str(uname)
	passW = str(pword)
	result = c.execute('SELECT DISTINCT usersList.user,usersList.pass FROM usersList WHERE usersList.user = ?', (userN,))
	for x in result:
		if x[0] == userN:
			response = "taken"
	if response != "taken":
		response = "success"
		inputUser(userN, passW)
	conn.commit()
	conn.close()
	return response

def inputUser(username, password):
	conn = sqlite3.connect("userList.db")
	c = conn.cursor()
	c.execute('INSERT INTO usersList VALUES (?, ?)', (username, password))
	conn.commit()
	conn.close()