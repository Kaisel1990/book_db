# -*- coding: utf-8 -*-
import pymysql

mydb = pymysql.connect(host='127.0.0.1',user='root',passwd='Synthe01',port=3306)

mycursor = mydb.cursor()


#~ try:
    #~ mycursor.execute('CREATE DATABASE BookDB')
#~ except pymysql.err.ProgrammingError:
    #~ pass
#~ mycursor.execute('DROP TABLE BookDB.Test_Database')


#~ sql_query = "CREATE TABLE BookDB.Test_Database \
#~ (UID SMALLINT NOT NULL,\
 #~ User VARCHAR(30) NOT NULL,\
 #~ PRIMARY KEY (UID))"


#~ mycursor.execute(sql_query)


#~ sql_insert = "INSERT INTO BookDB.Test_Database\
 #~ VALUES (2, 'Gabi')\
#~ "

#~ mycursor.execute(sql_insert)
#~ mydb.commit()

sql_query = "CREATE TABLE BookDB.Books \
(Titel VARCHAR(50) NOT NULL,\
 Autor VARCHAR(50) NOT NULL,\
 Verlag VARCHAR(50) ,\
 Sprache VARCHAR(10) ,\
 ISBN VARCHAR(15) NOT NULL ,\
 PRIMARY KEY (ISBN))"


mycursor.execute(sql_query)


