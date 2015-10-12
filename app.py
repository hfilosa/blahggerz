from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route("/index", methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    if request.method=="POST":
        button = request.form['button']
        uname=request.form['username']
        pword=request.form['password']
        if button=="Login":
            if utils.authenticate(uname,pword):
                return render_template("homepage.html",uname=uname)
            else:
                return "Wrong combo"
        else:
            return "bye"

#Debug is true to get better error messages
#Run the app. The host COULD be IP address, but normally put it down as 0.0.0.0 so that anyone can use the app.
if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=8000)
