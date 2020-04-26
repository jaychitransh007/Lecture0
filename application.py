from flask import Flask

app = Flask("__main__")

@app.route("/")
def index():
    greet_string = "Hello World!"
    return greet_string

@app.route("/<string:name>")
def hello(name):
    greet_string = f"Hello, {name.capitalize()}!"
    return "<h1>"+greet_string+"<h1>"
