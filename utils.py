import shelve, sqlite3
from pymongo import MongoClient

data_base = 'data'

#database is 'userList'
#table of user is 'users'
#fields: uname, passwd

def authenticate(name,word):
	connection = MongoClient()
        db = connection['userList']
#	q = 'SELECT usersList.user FROM usersList WHERE usersList.pass = %(user)s'

	if db.users.find({'uname':name}):
		#print "here"
		if db.users.find({'uname' : name} , {'passwd': word}):
			return "sucess"
		print here
		return "fail"
	return "noUser"



def add(uname, pword):
	connection = MongoClient()
        db = connection['userList']
	if db.users.find({'uname': uname}):
		print db.users.find({'uname': uname},{uname:False})
		return "taken"
	db.users.input({'uname' : uname} , {'passwd': pword})
	return "success"
	
def addPost(userN, timeT, message):
	connection = MongoClient()
	db = connection['userList']
	n = findPostNum() + 1
	db.posts.insert({'user' : userN, 'time': timeT, 'msg' : message})
#	c.execute('INSERT INTO postsList VALUES (?, ?, ?, ?)', (user, time, message, n))
	#print("success")
	
def findPostNum():
	connection = MongoClient()
	db = connection['userList']
	nums = c.execute('SELECT postsList.postNum FROM postsList ORDER BY postsList.postNum DESC')
	for x in nums:
		return x[0]
		break

def deletePost(postN):
	connection = MongoClient()
	db = connection['userList']
#	c.execute('DELETE FROM postsList WHERE postsList.postNum = ?', (postNum,))
	db.posts.remove({'postNum' : postN})
	print("success")
	
def getPosts():
	connection = MongoClient()
	db = connection['userList']
	allPosts = db.posts.find({})
#	posts = c.execute("SELECT DISTINCT * FROM postsList ORDER BY postsList.postNum DESC")
	return allPosts

	
