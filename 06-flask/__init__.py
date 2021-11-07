from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
	return render_template("home.html")


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=3000)

"""
Line 1 imports Flask

Line 3 instantiates Flask with app variable, using the __name__ attribute

Line 6 sets up a route / for your home, or default, page. When a user goes to http://localhost:3000/, you can set up particular code to be triggered

Line 7 creates a function called home. In this case it's loading the home.html template from templates directory.

Line 11 tests to make sure the right script is being run

Line 9 runs the application from the app variable we initialized so that the user can visit the web application by going http://localhost:3000
"""
