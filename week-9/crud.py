#crud application for products in a store

#what are we storing about products
#inventory_level
#name
#description
#id
#price
#id,name,description,price (products.csv)

#create a product

#read product data

#update a product

#delete a product

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import json

#create a flask app

app = Flask(__name__)

@app.route("/") #home route
def index():
    return render_template("base.html")

#route to display all products
@app.route("/products")
def get_products(): #list all the products
    #read my products file
    product_list = pd.read_csv("/Users/sun/Desktop/python-15/week-9/products.csv")

    #parse data
    #parsed_data = json.loads(product_list.to_json())
    #return parsed_data

#return a list that looks like this
#i [{id: , name, description, price}, {id: , name, description, price}]
    #return product_list.to_dict('records') #.to_dict convert to dictionary
    #return render_template('products.html', name="Son")

    return render_template('products.html', products=product_list.to_dict('records'))

#route to add new product
@app.route("/products/new", methods=["GET", "POST"])
def add_new_product():
    if request.method == "GET":
        return render_template("new-product.html")
    else:
        #save form data in products.csv file
        #fetch the current products from file
        products = pd.read_csv("/Users/sun/Desktop/python-15/week-9/products.csv")
        product_list = products.to_dict("records")

        #add new product to list
        product_name = request.form["name"]
        product_description = request.form["description"]
        product_price = request.form["price"]
        new_product = {}

        new_product_id = product_list[len[product_list] - 1].id + 1
        new_product["id"] = new_product_id
        new_product["name"] = product_name
        new_product["description"] = product_description       
        new_product["price"] = product_price

        product_list.append(new_product)

        #print(product_list)
        #write updated list to file

        #grad the indexes (to prevent pandas from adding its own each time)
        
        df = pd.DataFrame(product_list).set_index("id")
        df.to_csv("products.csv")

        
        return redirect(url_for("products.html"))

#edit route
@app.route("/products/<id>")
def edit_product(id):
    #1. fetch the list products from the csv file
    products = pd.read_csv("/Users/sun/Desktop/python-15/week-9/products.csv")
    
    #2. find the product that matches the given id
    for product in products:
        pass
    #3. create a new template to update the product 

    #3.1 use the same form that we use to create new product

    #3.2 set the value of each field to the corresponding product data
    #understand the flow of web design thursday 5-6
    #create route and template
    pass
    
if __name__ == "__main__":
    app.run(debug=True) #running app in debug mode

    