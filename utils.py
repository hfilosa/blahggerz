import shelve, sqlite3
from pymongo import MongoClient
import random

data_base = 'data'

#database is 'userList'
#table of user is 'users'
#fields: uname, passwd

def authenticate(name, word):
        connection = MongoClient()
        db = connection['userList']
        x = list(db.users.find({'uname':name}))
        print x
        print len(x) #works
        print "\n-------"
        if len(x) != 0:
                n = list(db.users.find({'uname' : name} , {'passwd': word}))
                print n
                print len(n)
                if len(n) != 0:
                        print "Success"
                        return "success"
                return "fail"
        return "noUser"

def add(uname, pword):
        connection = MongoClient()
        db = connection['userList']
        g = list(db.users.find({"uname":uname}))
        print g
        try:
                x = len(g)
        except:
                x = 0
        #x = db.collection.count({uname: "uname"})
        print(x)
        if x > 0:
                return "taken"
        db.users.insert({'uname' : uname} , {'passwd': pword})
        return "success"

def addPost(userN, timeT, message):
        connection = MongoClient()
        db = connection['userList']
        a = 0
        posts_has_id = True
        while(posts_has_id):
                a = random.randint(0, 10000)
                posts_has_id = hasPost(a)
                db.posts.insert({'user' : userN, 'time': timeT, 'msg' : message, 'postNum' : a})
                #	c.execute('INSERT INTO postsList VALUES (?, ?, ?, ?)', (user, time, message, n))
                #print("success")
                
def hasPost(postN):
        connection = MongoClient()
        db = connection['userList']
        x = list(db.posts.find({'postNum':postN}))
        return not(len(x) == 0)

def deletePost(postN):
        connection = MongoClient()
        db = connection['userList']
        #	c.execute('DELETE FROM postsList WHERE postsList.postNum = ?', (postNum,))
        db.posts.remove({'postNum' : postN})
        print("success")
	
def getPosts():
	connection = MongoClient()
        db = connection['userList']
        allPosts = list(db.posts.find({}))
        #	posts = c.execute("SELECT DISTINCT * FROM postsList ORDER BY postsList.postNum DESC")
        return allPosts
