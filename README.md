# REST API for Maternal Health Grant Databases

## Data sources 
https://data.hrsa.gov/data/download 

https://www.fns.usda.gov/pd/wic-program

## Overview
We collected data from the sources above. Then cleaned that data with pandas scripts before exporting them to clean CSV matching SQLite tables. A separate set of scripts then creates a SQLite DB with those matching tables, and then loads the CSVs into the SQLite database for use in our Flask application.
Using this database, we created a Flask application that provides a simple REST API with routes for returning JSON serialized data for analytical use.

## Setting up for local development
- (optional) in api.py uncomment line 178 and comment in line 179 to toggle local development mode on
- install python3 as well as the follower python libraries: pandas, flask, flask-restful
- Download the following file into the /data folder https://data.hrsa.gov//DataDownload/DD_Files/FS_EHB_AWARD_GRANT_FA_AGR_MVX.csv 
- run in this order EHB Grants.py, combined_active_program_codes.py, combine_active_award_codes.py with the python command to clean data and repopulate the data/output folder
- If a database.sqlite file exists in the root dir of the project delete it
- run in this order create_db_schema.py, and populate_db.py
- run api.py in your environment as you see fit
- (optional) on local just running api.py is fine. However if you want to test this in a server you will have to configure port 5000 to be opne, and will want to run api.py in a detached terminal multiplexer such as screen. If you want to server it will SSL you will need a WSGI server such as, Gunicorn, and then will have to configure a reverse proxy such as, Ngnix, to server that with SSL. Something like the certbot package from Let's Encrypt can be used to obtain a SSL certificate. This entire step is optional for development, and even for demoing on a basic server. However all of the above should be done to use this in production.

## Using Our API
takes Grantee_Name, and returns info on all grants they have been awarded
- /name/Virginia%20Commonwealth%20University
- /name/University%20Of%20Texas%20At%20Austin
- /name/UNIVERSITY%20OF%20MISSOURI%20SYSTEM  

takes a Grant_Activity_Code, and returns the Grantee_Name
- /code/H17
- /code/H49
- /code/T79  

returns Who, What, Where, and How Much re: grants within a state from 2023(When)
replace with any state abbreviation
- /topgrants/VA
- /topgrants/TX
- /topgrants/FL  

take a Program_Name to get Grant_Activity_Code from one table, and then use it to reference
another table and return all data regarding who received that grant Program_Name
- /program/Regional%20Genetics%20Networks%20
- /program/State%20Maternal%20Health%20Innovation%20Program%20
- /program/EMSC%20Targeted%20Issue%20Grants%20  

## Ethical Considerations
We came through the data through public sources and were sure to clean up any data involving any non-public individuals so that they would not appear on any of our API returns.

## Slide Presentation
https://docs.google.com/presentation/d/1DqMg4RfkKT_jn_7MWw8fxfaO51xFHkT6UACjOiGmZ5o/edit?usp=sharing
