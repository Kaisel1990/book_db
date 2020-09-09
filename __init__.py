from flask import *
from Table_Funcs import *
import pymysql as sql
import pandas as pd
import json
mydb = pymysql.connect(host='127.0.0.1',user='root',passwd='Synthe01',port=3306)
cursor = mydb.cursor()


app = Flask(__name__)

@app.route("/interactive/")

def interactive():
    return render_template('interactive.html')
    
    
@app.route('/background_process')
def background_process():
            
    sql_query = "SELECT * from BookDB.Test_Database"
    dicti = SQL_To_JSON(sql_query, cursor)
    return json.dumps(dicti) 
            
    
if __name__ == "__main__":
    app.run(debug=True)
