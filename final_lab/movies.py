#GOAL: create a movie recorder site that takes in movie name, type and date to store into a csv file 
#so that users can keep track of their favorite lists of movies and films

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import json


#create a flask app

app = Flask(__name__)

@app.route("/") #home route
def index():
    return render_template("base.html")

@app.route("/home")
def return_home():
    word = "GOAL: create a movie recorder site that takes in movie name, type and date to store into a csv file so that users can keep track of their favorite lists of movies and films"
    return render_template("home.html", words=word)

#route to display all products
@app.route("/my/films")
def get_films(): #list all the products
    #read my products file
    movie_list = pd.read_csv("films.csv")

    return render_template('films.html', products=movie_list.to_dict('records'))


#add new films
@app.route("/new", methods=["GET", "POST"])
def add_new_film():
    if request.method == "GET":
        return render_template("new-films.html")
    else:
        
        #save form data in products.csv file
        #fetch the current products from file
        products = pd.read_csv("films.csv")
        film_list = products.to_dict("records")

        #add new product to list
        product_name = request.form["name"]
        product_type = request.form["type"]
        product_date = request.form["date"]
        new_product = {}

        new_product_id = film_list[len(film_list) - 1]["id"] + 1

        new_product["id"] = new_product_id
        new_product["name"] = product_name
        new_product["type"] = product_type       
        new_product["date"] = product_date

        film_list.append(new_product)

        
        #write updated list to file

        #grad the indexes (to prevent pandas from adding its own each time)
        
        df = pd.DataFrame(film_list).set_index("id")
        df.to_csv("films.csv")

        #return render_template('base.html')
        return redirect(url_for('get_films')) #not products.html


#route to edit each product


@app.route('/my/films/<id>', methods=["GET", "PUT", "POST"])
def edit_product(id):
    #1. read the list products from the csv file
    product_list = fetch_film_list()
    #2. find the product that matches the given id
    selected_product = None
    for product in product_list:
        if product['id'] == int(id):
            selected_product = product
            break
    #if it is a GET request, show the form with the data filled out in the form fields
    if request.method == 'GET':
        #return the edit-product template
        return render_template('edit-product.html', product=selected_product)
    
    else:
        data = {
            'id': product['id'],
            'name': request.form['name'],
            'description': request.form['type'],
            'price': request.form['date']
        }
        #update product list by replacing existing product with updated one
        #again, search for the one with matching id
        update_product(product_list, data)
        #write the changes to the file
        df = pd.DataFrame(product_list).set_index('id')
        df.to_csv('films.csv')
        return redirect(url_for('get_films'))

#delete film
@app.route('/my/films/<id>/delete', methods=['POST','DELETE'])
def delete_film(id): 
    delete_film(request.form['delete'])
    return redirect(url_for('get_films'))

def fetch_film_list():
    films = pd.read_csv("films.csv")
    return films.to_dict("records")

def update_product(product_list, new_product):
    for idx in range(len(product_list)):
        if new_product['id'] == product_list[idx]['id']:
            product_list[idx] = new_product
            break
    
def delete_film(id):
    product_list = fetch_film_list()
    new_list = [product for product in product_list if not (product['id'] == int(id)) ]
   
    df = pd.DataFrame(new_list).set_index("id")
    df.to_csv("films.csv")
    
if __name__ == "__main__":
    app.run(debug=True) #running app in debug mode


    