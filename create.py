import sqlite3, datetime
from pymongo import MongoClient

data_base = 'data'
conn = MongoClient()
db = conn['userList']

currentTime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:\%M:%S')
users = {'uname':"Randy", 'passwd':"pwd"}
posts = {}

db.users.insert({'uname': "Chlo" , 'passwd': "pass"})
db.posts.insert({'user': "Chlo" , 'time': currentTime , 'msg' : "Trying to Mongo", 'postNum' : 1})
db.comments.insert({'user' : "Chloe" , 'time' : currentTime, 'msg' : "good luck", 'commNum' : 1})

###CREATED TABLE CONTAINING USERNAMES AND PASSWORDS AND HARDCODED ALL OF OUR NAMES INTO IT
#c.execute('''CREATE TABLE usersList (user text, pass text)''')
#c.execute("INSERT INTO usersList VALUES ('wayez','chowdhury')")
#c.execute("INSERT INTO usersList VALUES ('winton','yee')")
#c.execute("INSERT INTO usersList VALUES ('kathy','wang')")
#c.execute("INSERT INTO usersList VALUES ('jerry','lei')")

###FOR DEVUGGING PURPOSES
#q = 'SELECT DISTINCT usersList.user,usersList.pass FROM usersList'
#result = c.execute(q)
#p = 0
#for x in result:
#	print x

#c.execute('''CREATE TABLE postsList (user text, time text, msg txt, postNum int)''')
#c.execute('''CREATE TABLE comments (user text, time text, msg txt, postNum int)''')
#currentUser = "wayez"
#currentTime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
#message = "This is the very first post of blahggerz"
#c.execute("INSERT INTO postsList VALUES (?, ?, ?, 1)", (currentUser, currentTime, message))


