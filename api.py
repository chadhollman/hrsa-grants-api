from flask import Flask, jsonify
from flask_restful import Resource, Api
import sqlite3
import pandas as pd

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
    # traditional sql cursor not used in favor of a panda's dataframe for simplicity
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
    query = f"SELECT * FROM maternal_ehb_awarded WHERE Grant_Activity_Code = '{code}'"

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
    
# mimimal route example
@app.route('/return/<name>')
def return_name(name):
    return {'n2': name}

# takes an activity code, and determines if it is active or not
# @app.route('/awarded/<code>', methods=['GET'])
# def get_activity_code(code):
#     conn = get_db()
#     query = f"SELECT * FROM maternal_ehb_awarded WHERE Grantee_Name = '{code}'"

if __name__ == '__main__':
    app.run(debug=True)

# code I added, but then removed
# class IceCreamName(Resource):
#     def get(self, name):
#         # return json of the row associated with an ice cream name
#         return {}

# api.add_resource(IceCreamName, '/IceCreamName/<string:name>')

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()