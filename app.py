# app.py
from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)




@app.route('/')
def home():
	return render_template("index.html")



@app.route("/login",methods=["GET","POST"])
def login():
	username=request.form.get("username")
	password=request.form.get("password")
	print(username,password)
	return "Please wait for 24hrs generating"




if __name__ == '__main__':
    app.run(debug=True)
