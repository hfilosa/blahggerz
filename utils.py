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
	
def addPost(user, time, message):
	conn = sqlite3.connect("posts.db")
	c = conn.cursor()
	n = findPostNum() + 1
	c.execute('INSERT INTO postsList VALUES (?, ?, ?, ?)', (user, time, message, n))
	conn.commit()
	conn.close()
	#print("success")
	
def findPostNum():
	conn = sqlite3.connect("posts.db")
	c = conn.cursor()
	nums = c.execute('SELECT postsList.postNum FROM postsList ORDER BY postsList.postNum DESC')
	for x in nums:
		return x[0]
		break

def deletePost(postNum):
	conn = sqlite3.connect("posts.db")
	c = conn.cursor()
	c.execute('DELETE FROM postsList WHERE postsList.postNum = ?', (postNum,))
	conn.commit()
	conn.close()
	print("success")
	
def getPosts():
	conn = sqlite3.connect("posts.db")
	c = conn.cursor()
	posts = c.execute("SELECT DISTINCT * FROM postsList ORDER BY postsList.postNum DESC")
	conn.commit()
	return posts
	conn.close()

	