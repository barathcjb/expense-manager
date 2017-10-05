
def adduser():
	import os
	import expensedata as ed
	import newuser as n
	import getpass
	import option_selector as o
	import userdb as u
	os.system('color 9F')	
	print "\n\n\n\t\t WELCOME TO EXPENSE MANAGER "
	print 	  "\n\t\t       Hello new user"
	s=str(raw_input("\n\t>username: "))
	p=getpass.getpass("\t>password: ")
	
	if s==p or len(s)<8 or " " in s or " " in p :
		print"\n\t username and password cannot be same"
		print"\t username must be of minimum 8 characters"
		print"\t username cannot contain spaces"
		n.adduser()
		
	else:
		res=u.usercheck(s,p);
		if res==1:
			print"\n\t Hola! you became our user"
			u.userdbs(s,p)
					
		else:
			print"\n\t user already exists"
			n.adduser()
			
	n.olduser
		
def olduser():
	import os
	import getpass
	import newuser
	import userdb
	import time
	import chatdb
	import enterdata as ed
	os.system('color 4D')
	print("\n\n\n\n\t\t !!!!HELLO USER!!!!")
	print       "\n\t\t       Sign In     "    
	print "\r\r\n\t          welcome to the day\n\t      "+time.asctime( time.localtime(time.time())),"\r"
	s=str(raw_input("\n\t> username: ")).lower()
	p=getpass.getpass("\n\t> password: ").lower()
	
	if s==" " and p==" ":
		print"\n\tsorry wrong input"
		newuser.olduser()
		
	elif s=="admin" and p=="admin":
		import adminUser as ad
		os.system('cls')
		print"\n\n\t\t welcome admin"
		print"\n\t1. view users: "
		print"\t2. drop db:"
		print"\t3. create db:"
		print"\t4. truncate db:"
		print"\t5. chat check:"
		try:
			ch=int(input("\n\t> enter your option: "))
		except :
			print"\n\twrong input type"
		if ch==1:
			os.system('cls')
			print"\n\t analysing..."
			ad.seeall()

		elif ch==2:
			try:
				os.system('cls')
				print"\n\t dropping..."
				ad.drop()
			except:
				newuser.olduser()
				
		elif ch==3:
			try:
				os.system('cls')
				print"\n\t creating...."
				ad.create()
			except:
				newuser.olduser()
				
		elif ch==4:
			try:
				os.system('cls')
				print"\n\t truncating..."
				ad.truncateit()
			except:
				newuser.olduser()
		
		elif ch==5:
			try:
				os.system('cls')
				print"\n\t getting..."
				chatdb.chatcheck()
				temp=input("\t press 'h' to go home: ")
				if temp=='h':
					os.system('cls')
					chatdb.close()
					import main
				else:
					newuser.olduser()
			except:
				newuser.olduser()
		else:
			print"\n\t wrong input!!"
			ad.close()
			newuser.olduser()

	else:
		 ret=userdb.usercheck(s,p);
		 if ret==0:
			 os.system('cls')
			 ed.enter_income()
		 else:
			 os.system('cls')
			 print"\n\t username password mismatch"
			 newuser.olduser()
			 
			 
		
