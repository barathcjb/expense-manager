import sqlite3
import os
connection = sqlite3.connect("muser.db")
cursor = connection.cursor()


def seeall():
	cursor.execute("SELECT * FROM USER") 
	result = cursor.fetchall()	 
	for r in result:
		print r,"\n"
	ch=str(raw_input("\n\t> press 's' to go home\n\t        'b' to go back: "))
	if ch=='s':
		import main
	elif ch=='b':
		os.system('cls')
		import newuser
		newuser.olduser()
	else:
		print"\t wrong input"
		import adminUser
		adminUser.seeall()

def drop():

	sql_command="""
	DROP TABLE USER;"""
	
	cursor.execute(sql_command)
	connection.commit()

def create():
	sql_command="""
	CREATE TABLE USER(
	USERNAME VARCHAR(10),
	PASSWORD VARCHAR(10));"""
	
	cursor.execute(sql_command)
	connection.commit()

def truncateit():
	sql_command="""
	DELETE FROM USER;"""
	
	cursor.execute(sql_command)
	connection.commit()


