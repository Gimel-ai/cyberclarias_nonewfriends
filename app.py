from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("Are you our friend?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	if (request.form['name_input']) == "Ruben" or (request.form['name_input']) == "Rafael" or (request.form['name_input']) == "Mario" or (request.form['name_input']) == "Alejandro" or (request.form['name_input']) == "Jorgito":
		flash("You are my brother " + str(request.form['name_input']) + ", CYBERCLARIAS FOR EVER!")
	else:
		flash("Get the fuck out of here " + str(request.form['name_input']) + ", NO NEW FRIENDS!!!")
	return render_template("index.html")


	
	
