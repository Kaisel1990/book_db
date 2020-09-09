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


sql_insert = "INSERT INTO BookDB.Test_Database\
 VALUES (2, 'Gabi')\
"

mycursor.execute(sql_insert)
mydb.commit()


#~ mycursor.execute('DROP TABLE BikeTrainerDB.TrUsers')

#~ sql_query = "CREATE TABLE BikeTrainerDB.TrUsers \
#~ (UID SMALLINT NOT NULL AUTO_INCREMENT,\
 #~ Name VARCHAR(30),\
 #~ Prename VARCHAR(30) NOT NULL ,\
 #~ Weight REAL ,\
 #~ Height SMALLINT,\
 #~ PRIMARY KEY (UID))"

#~ mycursor.execute(sql_query)

#~ sql_insert = "INSERT INTO BikeTrainerDB.TrUsers\
 #~ VALUES (1, NULL,'Daniel',74, 180)\
#~ "
#~ sql_delete = "DELETE FROM BikeTrainerDB.TrUsers WHERE UID = 3"
#~ mycursor.execute(sql_delete)
#~ mydb.commit()

#~ sql_reset = " ALTER TABLE BikeTrainerDB.TrUsers AUTO_INCREMENT = 1"
#~ mycursor.execute(sql_reset)
#~ mydb.commit()


#~ sql_delete = "DELETE FROM BikeTrainerDB.TrCatalogue WHERE User = 1 and TID = 1"

#~ mycursor.execute(sql_delete)
#~ mydb.commit()


#~ mycursor.execute('DROP TABLE BikeTrainerDB.TrEntries')

#~ sql_query = "CREATE TABLE BikeTrainerDB.TrEntries \
#~ (EID SMALLINT NOT NULL,\
 #~ TID SMALLINT NOT NULL,\
 #~ UID SMALLINT NOT NULL,\
 #~ Time REAL NOT NULL,\
 #~ Speed REAL NOT NULL,\
 #~ Power REAL NOT NULL,\
 #~ Level SMALLINT NOT NULL ,\
 #~ PRIMARY KEY (TID,EID),\
 #~ FOREIGN KEY (UID,TID) REFERENCES BikeTrainerDB.TrCatalogue(User, TID) ON DELETE CASCADE)"

#~ mycursor.execute(sql_query)

#~ sql_insert = "INSERT INTO BikeTrainerDB.TrEntries\
 #~ VALUES (1, 1, 1, 0, 30, 120, 1)\
#~ "

#~ mycursor.execute(sql_insert)
#~ mydb.commit()

# Lesen
#~ mycursor.execute("SELECT * FROM BikeTrainerDB.TrDat ")
#~ print(mycursor.fetchall())
