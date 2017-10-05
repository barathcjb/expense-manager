import sqlite3
connection = sqlite3.connect("chat.db")
cursor = connection.cursor()

"""sql_command=\"""
CREATE TABLE CHATDATA(
QUESTIONS VARCHAR);\"""
"""


#cursor.execute(sql_command)
#connection.commit()

def chatdbs(s):
	
	strings = """INSERT INTO CHATDATA VALUES ("{questions}");"""	
	sql_command = strings.format(questions=s)
	cursor.execute(sql_command)
	connection.commit()

def chatcheck():
	import os
	os.system('cls')
	cursor.execute("SELECT * FROM CHATDATA") 
	result = cursor.fetchall() 
	for r in result:
		print r,"\n"
		

