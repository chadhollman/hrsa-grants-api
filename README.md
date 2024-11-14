# REST API for Maternal Health Grant Databases

## Data sources 
https://data.hrsa.gov/data/download 

https://www.fns.usda.gov/pd/wic-program

## Overview
We collected data from the sources above. Then cleaned that data with pandas scripts before exporting them to clean CSV matching SQLite tables. A separate set of scripts then creates a SQLite DB with those matching tables, and then loads the CSVs into the SQLite database for use in our Flask application.
Using this database, we created a Flask application that provides a simple REST API with routes for returning JSON serialized data for analytical use.


## Using Our API

## Ethical Considerations
We came through the data through public sources and were sure to clean up any data involving any non-public individuals so that they would not appear on any of our API returns.

## Slide Presentation
https://docs.google.com/presentation/d/1DqMg4RfkKT_jn_7MWw8fxfaO51xFHkT6UACjOiGmZ5o/edit?usp=sharing
