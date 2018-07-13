from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("login.html")
	
@app.route("/signUp")
def signUp():
	return render_template("signUp.html")
	
@app.route("/studentProfile", methods = ["POST"])
def studentProfile():
	return render_template("studentProfile.html")

@app.route("/jobProfile")
def jobProfile1():
	return render_template("jobProfile.html")
	
@app.route("/Profile", methods = ["POST","GET"])
def jobProfile():
	#retrieving form data
	val_signUp=request.form['p']
	usern=request.form['user_name']
	psw=request.form['password']
	#call insert_user module with the above variables as arguments for the insert operation
	insert_user(usern,psw,val_signUp)
	#render respective templates checking if it is Admin/Student
	if(val_signUp=="Admin"):
		return render_template("jobProfile.html")
	elif(val_signUp=="Student"):
		return render_template("studentProfile.html")
	
@app.route("/applicantList", methods = ["POST"])
def applicantList():
	return render_template("applicantList.html")
	
@app.route("/home", methods = ["POST","GET"])
def jobsList():
	user_logIn=request.form['user1']
	pass_logIn=request.form['password1']
	val_logIn=request.form['r']
	users = select_user()
	for user in users:
		if user[0]==user_logIn and user[1]==pass_logIn:
			if(val_logIn=="Admin"):
				return render_template("applicantList.html")
			elif(val_logIn=="Student"):
				return render_template("jobsList.html")
		else:
			print("false")
		
@app.route("/studentJobsList", methods = ["POST"])
def studentJobsList():
	return render_template("jobsList.html")
	
@app.route("/test", methods = ["POST"])
def test():
	return render_template("test.html")

@app.route("/testInstructions")	
def testInstructions():
	return render_template("testInstructions.html")
	
@app.route("/testResult")
def testResult():
	return render_template("testResult.html")
	
if __name__ == "__main__":
	app.run()
