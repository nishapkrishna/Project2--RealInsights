RealInsights

For this project we sought to use API calls to fetch and return nationwide real estate data from multiple sources and then visualize that data to illustrate how property values have changed over time. The period of time we chose to on was 2012 to 2017. Our initial source of data from Kaggle.com was converted from CSV format to JSON and loaded to MongoDB. We then employed Flask API to call the housing data and display it on an interactive map of the United States using Plotly and Choropleth map. To drill down further we included a feature allowing the user to see data on the top 5 highest values in the country or inspect value change by state.

Link for RealInsights: https://stormy-oasis-20946.herokuapp.com/

Specific Requirements

1.	Visualization must include a Python Flask powered RESTful API, HTML/CSS, JavaScript, and at least one database (MySQL, MongoDB,           SQLite, etc.)

2.	Project should fall into one of the below four tracks:
    
    • A custom "creative" D3.js project (i.e. non-standard graph or chart)
    
    • A combination of Web Scraping and Leaflet ,Plotly and Choropleth map
    
    • A dashboard page with multiple charts all updating from the same data
    
    • A "thick" server that performs multiple manipulations on data in a database prior to visualization (must be approved)

3.	Project should include at least one JS library that we did not cover.

4.	Project must be powered by a dataset with at least 100 records.

5.	Project must include some level of user-driven interaction (e.g. menus, dropdowns, textboxes, etc.)

6.	Final visualization should ideally include at least three views

![alt text](https://github.com/nishapkrishna/RealInsights/blob/master/screencapture-localhost-5000-map-2019-05-22-13_29_13.png)
