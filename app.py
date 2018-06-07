from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("login.html")

@app.route("/studentSignUp")
def studentSignUp():
	return render_template("studentSignUp.html")
	
@app.route("/adminSignUp")
def adminSignUp():
	return render_template("adminSignUp.html")
	
@app.route("/studentProfile", methods = ["POST"])
def studentProfile():
	return render_template("studentProfile.html")
	
@app.route("/jobProfile", methods = ["POST"])
def jobProfile():
	return render_template("jobProfile.html")
	
@app.route("/editJobProfile")
def editJobProfile():
	return render_template("editJobProfile.html")
	
@app.route("/jobsList", methods = ["POST"])
def jobsList():
	return render_template("jobsList.html")
	
@app.route("/test")
def test():
	return render_template("test.html")
	
@app.route("/testResult")
def testResult():
	return render_template("testResult.html")
	
if __name__ == "__main__":
	app.run()
