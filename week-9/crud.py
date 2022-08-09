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
from flask import Flask, render_template
import json

#create a flask app

app = Flask(__name__)

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



if __name__ == "__main__":
    app.run()

    