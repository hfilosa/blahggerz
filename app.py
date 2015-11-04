from flask import Flask, render_template, request, redirect, url_for, session
import datetime
import utils
import sqlite3
import shelve
from pymongo import MongoClient

app = Flask(__name__)

currentUser = ""

@app.route("/index", methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
def index():
    if 'logged_in' not in session:
        session['logged_in'] = False
    if 'user' not in session:
        session['user'] = 'Anonymous'
    if request.method=="GET":
        return render_template("index.html", log  = "", s=session )
    if request.method=="POST":
        button = request.form['button']
        username=request.form['username']
        password=request.form['password']
        if button=="Login":
            result = utils.authenticate(username,password)
            if result == "success":
                currentUser = username
                session['user'] = username
                session['logged_in'] = True
                session['posts'] = utils.getPosts()
                return redirect("/posts")
            elif result == "noUser":
            	return render_template("index.html", log = "noUser", s=session)
            else:
            	return render_template("index.html", log = "fail", s=session)
        else:
            return "bye"
            
@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method=="GET":
    	return render_template("register.html", taken = False, success = False, s=session)
    if request.method=="POST":
        button = request.form['button']
        username=request.form['username']
        password=request.form['password']
        if button=="Register":
            response = utils.add(username,password)
            print response
            if response == "taken":
                return render_template("register.html", taken = True, success = False, s=session)
            elif response == "success":
                return render_template("register.html", taken = False, success = True, s=session)
            else:
                return "Wrong combo"
        else:
            return "bye"


@app.route("/postnew", methods=["GET","POST"])
def postnew():
    if session['logged_in'] == False:
        return redirect('/index')
    if request.method=="GET":
        return render_template("postnew.html", username = session['user'], s=session)
    if request.method=="POST":
        postButton = request.form['postButton']
        uname = session['user']
        time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        msg = request.form['post']
        utils.addPost(uname, time, msg)
        posts = utils.getPosts()
        return redirect("/posts") #render_template("posts.html", username = currentUser, posts = posts, comments = [])

        
@app.route("/posts", methods=["GET","POST"])
def posts():
    posts = utils.getPosts()
    if session['logged_in'] == False:
        return redirect('/index')
    if request.method=="GET":
        return render_template("posts.html", username = session['user'], posts = posts, comments = [], s=session)
    if request.method=="POST":
        button = request.form['button0']
        if button == "Write New Post":
            return redirect("/postnew") #("postnew.html", username = currentUser)
        return render_template("posts.html", username = session['user'], posts = posts, comments = [],s=session)


@app.route("/logout")
def logout():
    session['user'] = "Anonymous"
    session['logged_in'] = False
    return redirect('/index')
        
#Debug is true to get better error messages
#Run the app. The host COULD be IP address, but normally put it down as 0.0.0.0 so that anyone can use the app.
if __name__=="__main__":
    app.debug=True
    app.secret_key = "My name is Ted"
    app.run(host='0.0.0.0',port=8000)
