from flask import Flask, jsonify
from flask_restful import Resource, Api
import sqlite3
import pandas as pd

app = Flask(__name__)
api = Api(app)

def get_db():
    DATABASE = '/Users/samsonweiser/class/DATA-PT-EAST-JULY-071524/10-Advanced-SQL/1/Activities/02-Stu_IceCream_Connection/Resources/icecreamstore.sqlite'
    conn = sqlite3.connect(DATABASE)
    # conn.row_factory = sqlite3.Row
    return conn

@app.route('/name/<name>', methods=['GET'])
def get_user_record(name):
    conn = get_db()
    cursor = conn.cursor()
    
    query = f"SELECT * FROM icecreamstore WHERE Flavors = '{name}'"
    # query = "SELECT * FROM icecreamstore WHERE Flavors = ?"
    # query = "SELECT * FROM icecreamstore"

    df = pd.read_sql(query, conn)

    # cursor.execute(query)
    # cursor.execute(query)

    # record = cursor.fetchone()

    # print(record)
    
    conn.close()
    
    # record = False
    if len(df)!=0:
        return jsonify({
            "message": "User record found",
            "record": df.to_dict(orient = 'records')
        })
    else:
        return jsonify({"error": "User record not found"}), 404

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

@app.route('/return/<name>')
def return_name(name):
    return {'n2': name}

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