from flask import Flask, render_template, request, redirect
import utils
import sqlite3

app = Flask(__name__)

@app.route("/index", methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    if request.method=="POST":
        button = request.form['button']
        username=request.form['username']
        password=request.form['password']
        if button=="Login":
            if utils.authenticate(username,password):
                return render_template("homepage.html",username=username)
            else:
                return "Wrong combo"      
        else:
            return "bye"


@app.route("/postnew", methods=["GET","POST"])
def postnew():
    posts = "posts.sqlite"
    if request.method=="GET":
        return render_template("postnew.html")
    if request.method=="POST":
        con=sqlite3.connect(posts)
        c = con.cursor()
      # make username a universal variable?
        postButton = request.form['"postButton']
        uname = ""
        time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        msg = request.form['post']
        if postButton = "post": 
            c.execute("INSERT INTO posts VALUES(uname, time, msg)")
            return redirect("/index")
        
        

#Debug is true to get better error messages
#Run the app. The host COULD be IP address, but normally put it down as 0.0.0.0 so that anyone can use the app.
if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=8000)
