from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from flask import Flask,jsonify

#import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/test")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('price.html')

@app.route('/line')
def line():
    return render_template('line_chart.html')

@app.route('/data')
def data():
    return render_template('data.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

# Route to render index.html template using data from Mongo
@app.route('/get_all_data',methods=['GET'])
def get_all_data():
    import pandas as pd
    # Find one record of data from the mongo database
    output=[]
    for s in mongo.db.housing_data.find():
        output.append({'State': s['State'], 'Year': s['Year'], 'Avg Listing price': round(s['Avg Listing Price'],2), 'Active Listing Count': s['Active Listing Count']})

    return jsonify(output)

# Route to render index.html template using data from Mongo
@app.route('/get_data',methods=['GET'])
def get_data():
    import pandas as pd
    # Find one record of data from the mongo database
    output=[]
    for s in mongo.db.housing_data.find():
        output.append({'State': s['State'], 'Year': s['Year'], 'Avg Listing price': round(s['Avg Listing Price'],2)})

    return jsonify(output)

# Route that will trigger the scrape function
if __name__ == "__main__":
    app.run(debug=True)