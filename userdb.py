import sqlite3
import expensedata as ed
connection = sqlite3.connect("muser.db")
cursor = connection.cursor()




def userdbs(uid,pas):
	a=[uid,pas]
	
	strings = """INSERT INTO USER VALUES ("{username}", "{passw}");"""
	
	sql_command = strings.format(username=a[0], passw=a[1])
	cursor.execute(sql_command)
	connection.commit()
	import main

def usercheck(s,p):
	found=0
	if s=="" or p=="":
		found=1
	
	else:
		cursor.execute("SELECT * FROM USER") 
		result = cursor.fetchall() 
		for r in result:
			for i in xrange(len(s)) :
				for j in xrange(len(p)):
					if s[i] in r[0] and s[j] in r[1]:
						found= 0
						continue
					else:
						found=1
						continue
	return found
		
	"""if all(any(i in r[0] for i in s) and  any(j in r[1] for j in p))==True:
			found= 0
			continue
			
		else:
			found=1
			continue
	return found
	
	"""
