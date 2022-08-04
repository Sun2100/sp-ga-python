#import flask library import flask class
from flask import Flask

#understanding VIRTUAL MACHINE
app = Flask(__name__)
################################### ALWAYS static route before parameter route
#order of the route matters
@app.route("/")# the home route
def index():
    return "hello world"

#create a new route (/hello)
#a routh is a python function
#return "hey there!"
@app.route("/hello")
def say_hello():
    return "hey there!"

#create a route called classmates
#return a list of your classmates
@app.route("/classmates")
def get_classmates():
    return {"/response_code": 200, "data": ["dan", "pavel", "enzo", "son", "priscilla", "ella", "sanjeev"]}
######################################
#use a route parameter
@app.route("/<name>")
def self_hello(name):
    return f"hey there {name}!"

#implement a route that returns the classmate that matches an id
#create a list of dictionaries, with each name having an id
#names = [{"id": 1, "name": "dan"}, {"id": 2, "name": "pavel"}, {"id": 3, "name": "enzo"}, {"id": 4, "name": "son"}, {"id": 5, "name": "prescilla"},{"id": 6, "name": "ella"}, {"id": 7, "name": "sanjeev"}]
# /classmates/<id>
@app.route("/classmates/<id>")
def get_classmate(id):
    names = [{"id": 1, "name": "dan"}, {"id": 2, "name": "pavel"}, {"id": 3, "name": "enzo"}, {"id": 4, "name": "son"}, {"id": 5, "name": "prescilla"},{"id": 6, "name": "ella"}, {"id": 7, "name": "sanjeev"}]
    for num in names:
        if num["id"] == int(id):
            #name = num["name"]
            #return f"{id}, {name}"
            return num
    return {"/response-code": 404} #if not found (error message)

#make sure that items in the list are proper json (use double quotations)

if __name__ == "__main__":
    app.run()
