import shelve, sqlite3
from pymongo import MongoClient

data_base = 'userList'

#database is 'userList'
#table of user is 'users'
#fields: uname, passwd

def authenticate(uname,pword):
	conn = MongoClient()
        db = connection[data_base]
	q = 'SELECT usersList.user FROM usersList WHERE usersList.pass = %(user)s'
	userN = str(uname)
	passW = str(pword)
        result = db.users.find({username : userN} , {passwd: 1})

#	result = c.execute('SELECT DISTINCT usersList.pass FROM usersList WHERE usersList.user = ?', (userN,))

	return loginResponse(result, passW)

def loginResponse(realPass, inputPass):
	for x in realPass:
		if x[0] == inputPass:
			return "success"
		return "fail"
	return "noUser"


def add(uname, pword):
	response = "failed"
	conn = MongoClient()
        db = connection[data_base]
	userN = str(uname)
	passW = str(pword)

        result = db.users.find({uname : userN})
#	result = c.execute('SELECT DISTINCT usersList.user,usersList.pass FROM usersList WHERE usersList.user = ?', (userN,))
	for x in result:
		if x[0] == userN:
			response = "taken"
	if response != "taken":
		response = "success"
		inputUser(userN, passW)

	return response

def inputUser(username, password):
	conn = MongoClient()
	db = connection[data_base]
        db.users.insert({uname : username , passwd : password})
#	c.execute('INSERT INTO usersList VALUES (?, ?)', (username, password))
	
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

	
