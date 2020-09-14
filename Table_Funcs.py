# -*- coding: utf-8 -*-
import pymysql

 
def SQL_To_JSON( Query, cursor): 

    cursor.execute(Query)
    Result_Rel = cursor.fetchall()
    
    resultDict = {"0":{"Titel":"Titel", "Autor":"Autor", "Verlag":"Verlag", "Sprache":"Sprache", "ISBN":"ISBN"}}
    
    i = 1
    
    for Row in Result_Rel:
        
        resultDict.update({str(i):{"Titel":str(Row[0]), "Autor":Row[1], "Verlag":Row[2], "Sprache":Row[3], "ISBN":Row[4]}})
        i = i + 1
        
    return resultDict
 
 
def addToDB( bookData, db ):
    
    cursor = db.cursor()
    
    volume_info = bookData["items"][0] 
    author = bookData["items"][0]["volumeInfo"]["authors"][0]
    titel = bookData["items"][0]["volumeInfo"]["title"]
    ISBN = bookData["items"][0]["volumeInfo"]["industryIdentifiers"][1]["identifier"]
    nPage = volume_info["volumeInfo"]["pageCount"]
    language = volume_info["volumeInfo"]["language"]
    
    
    if len(titel) > 50:
        titel = titel[0:50]
    
    query = "INSERT INTO BookDB.Books(Titel,Autor,Sprache,ISBN) VALUES(%s,%s,%s,%s)"
    args = (str(titel), str(author), str(language), str(ISBN))
    try:    
        cursor.execute(query, args)
        db.commit()
    except:
        pass
    
