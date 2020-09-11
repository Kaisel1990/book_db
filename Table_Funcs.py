# -*- coding: utf-8 -*-
import pymysql

 
def SQL_To_JSON( Query, cursor): 

    cursor.execute(Query)
    Result_Rel = cursor.fetchall()
    
    resultDict = {"0":{"ID":"ID", "Name":"Name"}}
    
    i = 1
    
    for Row in Result_Rel:
        
        resultDict.update({str(i):{"ID":str(Row[0]), "Name":Row[1]}})
        i = i + 1
        
    return resultDict
 
    
if __name__ == '__main__':

    mydb = pymysql.connect(host='127.0.0.1',user='root',passwd='Synthe01',port=3306)
    cursor = mydb.cursor()

    sql_query = "SELECT * from BookDB.Test_Database"
    print SQL_To_JSON(sql_query, cursor)
    
