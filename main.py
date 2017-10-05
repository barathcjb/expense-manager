import os
import newuser
os.system('cls')
os.system("mode con: cols=70 lines=40" )
os.system('color 0B')
title="Daily Expense Manager"
os.system('echo '"\033]0;{}\007"''.format(title))
print "\n\n\n\t\tWELCOME TO EXPENSE MANAGER...."
print "\n\n\t\t. Sign up"
print "\n\t\t. Sign in"
print "\n\t\t. Chat with CJB"

ch=str(raw_input("\n\n\t\t\t________\b\b\b\b\b\b\b\b"))

if ch=="" or ch==" ":
		print"\n\t           (enter something)"
		import main
		
		
elif ch.lower()in ["signin" ,"sign in"]:
		os.system('cls')
		newuser.olduser()
		

elif ch.lower() in["signup","sign up"]:
		os.system('cls')
		newuser.adduser()
		
			
elif ch.lower() in ["chatwithcjb","chat with cjb"]:
		os.system('cls')
		import chatbot
		chatbot.cjb()
		
else:
		os.system('cls')
		import main
	

	
		
	




