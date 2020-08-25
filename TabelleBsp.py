from flask import *
from Table_Funcs import *
import pandas as pd

app = Flask(__name__)

@app.route("/tables")
def show_tables():
    
    #~ return render_template('view.html',tables=['<table><tr><td>Name</td> <td>ISBN</td>  <td>Titel</td></tr><tr><td>Kaiser</td> <td>1234</td>  <td>Iwas mit Stahl</td></tr></table>'], titles = ['na', 'Namen'])
    return render_template('view.html',tables=[SQL_To_HTML_Table()], titles = ['na', 'Namen'])

if __name__ == "__main__":
    app.run(debug=True)
