from flask import Flask, jsonify
from flask_restful import Resource, Api
import sqlite3
import pandas as pd

# United States of America Python Dictionary to translate States,
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "Virgin Islands, U.S.": "VI",
}
    
# invert the dictionary
abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))

app = Flask(__name__)
api = Api(app)

def get_db():
    DATABASE = 'database.sqlite'
    conn = sqlite3.connect(DATABASE)
    return conn

# takes grantee name, and returns all grant names they have been awarded
@app.route('/name/<name>', methods=['GET'])
def get_user_record(name):
    conn = get_db()
    # traditional sql cursor not used in favor of a pandas dataframe for simplicity
    # using the cursor would be more preformant
    cursor = conn.cursor()
    
    query = f"SELECT * FROM maternal_ehb_grantees WHERE Grantee_Name = '{name}'"
    
    df = pd.read_sql(query, conn)
    conn.close()
    
    # record = False
    if len(df)!=0:
        return jsonify({
            "record": df.to_dict(orient = 'records')
        })
    else:
        return jsonify({"error": "User record not found"}), 404

# takes an activity code, and returns the Grantee_Name
@app.route('/code/<code>', methods=['GET'])
def get_activity_code(code):
    conn = get_db()
    query = f"SELECT * FROM maternal_ehb_active WHERE Grant_Activity_Code = '{code}'"

    df = pd.read_sql(query, conn)
    df = df["Grantee_Name"]
    conn.close()

    # df = df.
    if len(df)!=0:
        return jsonify({
            "record": df.to_dict()
        })
    else:
        return jsonify({"error": "User record not found"}), 404

# returns top grants from 2023 by $ amount
@app.route('/topgrants/<topgrants>', methods=['GET'])
def get_top_grants(topgrants):
    conn = get_db()
    
    query = f"SELECT * FROM maternal_ehb_2023 WHERE State = '{topgrants}'"
    df = pd.read_sql(query, conn)
    df = df[['Financial_Assistance', 'County', 'State', 'Grantee_Name', 'Program_Name']]
    conn.close()
    
    # record = False
    if len(df)!=0:
        return jsonify({
            "record": df.to_dict(orient = 'records')
        })
    else:
        return jsonify({"error": "User record not found"}), 404
    
# take a Program_Name to get Grant_Activity_Code from one table, and then use it to reference
# another table and return all data regarding who received that grant Program_Name
@app.route('/program/<program>', methods=['GET'])
def get_program(program):
    conn = get_db()
    query = f"SELECT * FROM combined_award_program_codes WHERE Grant_Program_Name = '{program}'" 
    df = pd.read_sql(query, conn)

    grant_code = df['Grant_Activity_Code'].iloc[0]
    query = f"SELECT * FROM maternal_ehb_active WHERE Grant_Activity_Code = '{grant_code}'"
    df = pd.read_sql(query, conn)

    conn.close()
    
    # record = False
    if len(df)!=0:
        return jsonify({
            "record": df.to_dict(orient = 'records')
        })
    else:
        return jsonify({"error": "User record not found"}), 404
         
# mimimal route example
@app.route('/return/<name>')
def return_name(name):
    return {'returned string from url': name}

@app.route('/')
def example(name):
    return {
        'n2': name,
        'takes grantee name, and returns all grant names they have been awarded': 'http://67.205.145.13:5000/name/Virginia%20Commonwealth%20University',
        'takes grantee name, and returns all grant names they have been awarded': 'http://67.205.145.13:5000/name/University%20Of%20Texas%20At%20Austin',
        'takes grantee name, and returns all grant names they have been awarded': 'http://67.205.145.13:5000/name/UNIVERSITY%20OF%20MISSOURI%20SYSTEM',
        'takes an activity code, and returns the Grantee_Name': 'http://67.205.145.13:5000/code/H17',
        'takes an activity code, and returns the Grantee_Name': 'http://67.205.145.13:5000/code/H49',
        'takes an activity code, and returns the Grantee_Name': 'http://67.205.145.13:5000/code/H79',
        'returns top grants from 2023 by $ amount, replace with any state abbreviation': 'http://67.205.145.13:5000/topgrants/VA',
        'returns top grants from 2023 by $ amount, replace with any state abbreviation': 'http://67.205.145.13:5000/topgrants/TX',
        'returns top grants from 2023 by $ amount, replace with any state abbreviation': 'http://67.205.145.13:5000/topgrants/FL'
    }

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')