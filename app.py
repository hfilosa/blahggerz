from flask import Flask, render_template, request, redirect
import datetime
import utils
import sqlite3
import shelve

app = Flask(__name__)

#print utils.add('peter', 'stuyvesant')s
#print utils.authenticate('wayez', 'chowdhury')
# SQLITE POST TABLE CREATION 
#posts = "posts.db" 
#con=sqlite3.connect(posts)
#c = con.cursor()


#currentTime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
#print utils.addPost('wayez', currentTime, 'test post')
#print utils.deletePost(2)
#print utils.deletePost(3)

currentUser = ""

@app.route("/index", methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html", log  = "" )
    if request.method=="POST":
        button = request.form['button']
        username=request.form['username']
        password=request.form['password']
        if button=="Login":
            if utils.authenticate(username,password) == "success":
                currentUser = username
                posts = utils.getPosts()
                return render_template("posts.html", username=username, posts = posts, comments = [])
            elif utils.authenticate(username,password) == "noUser":
            	return render_template("index.html", log = "noUser")
            else:
            	return render_template("index.html", log = "fail")
        #if button=="Post":            
        else:
            return "bye"
            
@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method=="GET":
    	return render_template("register.html", taken = False, success = False)
    if request.method=="POST":
        button = request.form['button']
        username=request.form['username']
        password=request.form['password']
        if button=="Register":
        	response = utils.add(username,password)
        	if response == "taken":
        		return render_template("register.html", taken = True, success = False)
        	elif response == "success":
        		return render_template("register.html", taken = False, success = True)
        	else:
        		return "Wrong combo"
        #if button=="Post":            
        else:
            return "bye"

@app.route("/postnew", methods=["GET","POST"])
def postnew():
    if request.method=="GET":
        return render_template("postnew.html", username = currentUser)
    if request.method=="POST":
    	postButton = request.form['postButton']
    	uname = currentUser
    	time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    	msg = request.form['post']
    	if postButton == "post": 
            utils.addPost(uname, time, msg)
            posts = utils.getPosts()
            return render_template("posts.html", username = currentUser, posts = posts, comments = [])
            #return render_template("postnew.html")
    else:
            return "doodoo"

@app.route("/posts", methods=["GET","POST"])
def posts():
	posts = utils.getPosts()
	if request.method=="GET":
		return render_template("posts.html", username = "", posts = posts, comments = [])
	if request.method=="POST":
		button = request.form['button']
		if button == "Write New Post":
			return render_template("postnew.html", username = currentUser)
		return render_template("posts.html", username = currentUser, posts = posts, comments = [])


        
#Debug is true to get better error messages
#Run the app. The host COULD be IP address, but normally put it down as 0.0.0.0 so that anyone can use the app.
if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=8000)
