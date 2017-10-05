import os
import time
import chatbot as c
import chatdb as ch
import random
os.system('cls')
os.system('color 3F')
print"\n\n\t\tCHATBOT CJB WELCOMES YOU"
print"\t\t"+time.asctime( time.localtime(time.time())),"\r"
print"\n\n\t    Hello dude, I am CJB your friend\n \t  while you learn how the app works,\n \t  ask me anything you want to know...\n \t  you can share your emotions too :)"


def cjb():
	query=str(raw_input("\n\t> enter your query: ____________________\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b"))
	ch.chatdbs(query)
	c.entity(query.lower())
			
def entity(s):
	bad_entity=["fuck",'sex','suck','asshole',"rape",'dick',"boobs",'sappu','dickhead',"go fuck yourself","kunju","penis","you will die of aids",'shit','bitch','vagina','pussy','punda','soothu','sunni','chutiya','behnchod','thevdiya','kundi']
	exit_entity=["quit",'exit','go back','leave','bye',"goodbye","goodbye!"]
	love_entity=['love','marriage','like','marry','kiss','beautiful']
	name_entity=["name","iam",'help']
	enter_expense_entity=["enter","expense"]
	view_expense_entity=['view','expense']
	salutation_entity=['hi','hello','hai','hii','haii',"hey"]
	enter_income_entity=['enter','income']
	login_entity=['register','login','signup','signin','username','password']
	date_entity=['date','calendar','time','year','month','day']
	gender_entity=['are you man or woman','are you male or female','are you a man','are you a woman','are you a male','are you a female','are you man','are you woman','are you male','are you female']
	maths_entity=['+','-','/','*','%']
	human_emotions_entity=['happy','sad','angry','frustrated','tensed','bored','boring']
	general_entity=['how are you','what is your name','who are you','who is your creator','how do you call me','favourite','who is your developer','are you a robot','are you robot']
	response_entity=['ok','oh thats great','hmm','okay','thats great','thats good','then','sorry','meet you','shut up','shutup',"dont talk"]
	travel_entity=['journey','travel','fly','voyage','bike ride','adventure']
	savings_entity=['savings','tips','financial tips','financial health','financial']
	humour_entity=[' do you know biggest joke of century??\n\t Indian Demonetisation'," Dentist: This will hurt a little.\n\t Patient: OK.\n\t Dentist: I have been having an affair with\n\t\t your wife for a while now.",' A woman in a bikini reveals about 90% of her body....\n\t and yet most men are so polite they only look at the\n\t covered parts.',' A naked women robbed a bank.\n\t Nobody could remember her face.'," police: whats your date of birth\n\t accused: 12 february\n\t police: which year?\n\t accused: every year bro :p"," a guy to his father:If I ever go missing,\n\t you should put my picture on beer rather\n\t than milk bottles.\n\t This way, my friends will find me faster."]


	query_list=list(map(str,s.split()))
	
	if s=="" :
		print"\n\t talk something dude..."
		c.cjb()
		
	elif any(i in s for i in maths_entity):
		print"\n\t OOPS! sorry I am poor at math :p"
		c.cjb()
		
	elif any(i in query_list for i in savings_entity):
		print"\n\t    INSIGHTS TO GOOD FINANCIAL HEALTH"
		print"\t. budget for monthly and annual expenses"
		print"\t. differentiate between needs and wants"
		print"\t. save more and avoid unnecessary expenses"
		print"\t. list all financial goals and budget & stick to it"
		print"\t. invest accordingly"
		print"\t. remember equities and share investments are for \n\t  long term wealth creation,debt is for medium to\n\t  long term"
		c.cjb()
		
	elif any(i in s for i in gender_entity):
		print"\n\t I am a chatbot :)"
		print"\t am I clever ?"
		c.cjb()
		
	elif any(i in s for i in response_entity):
		print"\n\t ok :)"
		c.cjb()
	
	elif any(i in s for i in general_entity):
		
		for j in general_entity:
			if j in s:
				if j==general_entity[0]:
					print"\n\t I am fine..How are you?"
					temp=str(raw_input("\t> ________________\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b"))
					if temp in ['good','fine','happy']:
						print"\n\t thats good to hear"
					elif temp in ['bad','not fine','not happy','not','no']:
						print"\n\t oh! dont worry. Things will get alright :)"
					else:
						print"\n\t always remember karma is a boomerang :)"
						
				elif j ==general_entity[1]:
					print"\n\t I am CJB the chatbot. :)"
					
				elif j==general_entity[2]:
					print"\n\t I am CJB the chatbot. :)"
					
				elif j==general_entity[3] or j==general_entity[6]:
					print"\n\t My creator is a genius named Barath CJB..\n\t thus my name is derived from his last name"
					
				elif j==general_entity[4]:
					print"\n\t I usually call people 'dude'"
					
				elif j==general_entity[5]:
					print"\n\t Sorry I am unbiased"
					print"\t your's: "
					temp=str(raw_input("\t> ___________________\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b"))
					print"\n\t thats good to hear :)"
				
				elif j==general_entity[7] or j==general_entity[8]:
					print"\n\t No! I am a chatbot"
					
		c.cjb()
	
	elif any(i in query_list for i in human_emotions_entity):
		for j in human_emotions_entity:
			if j in query_list:
				print"\n\t why are you feeling ",j," ?"
				temp=str(raw_input("\t> _____________________\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b"))
				if j==human_emotions_entity[0]:
					print"\n\t oh! thats great to hear"
				elif j ==human_emotions_entity[1] or j ==human_emotions_entity[5] or  j ==human_emotions_entity[6] :
					print"\n\t oh! thats very sad to hear"
					print"\t can I tell a joke?"
					temps=str(raw_input("\t> _______________\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b"))
					if temps in ['yes','yeah','ok']:
						print"\n\t",random.choice(humour_entity)
						tempt=str(raw_input("\n\t> good one? "))
						if tempt in ['good','yes','yeah','nice']:
							print"\n\t Thank you dude:)"
							c.cjb()
						else:
							print"\n\t",random.choice(humour_entity)	
					else:
						print"\n\t ok :)"
					c.cjb()
				elif j==human_emotions_entity[2]:
					print"\n\t please be calm...good things will finally fall in place"
				elif j==human_emotions_entity[3]:
					print"\n\t please be calm...relax yourself"
				else:
					print"\n\t karma is a boomerang"
		c.cjb()
	
	elif any(i in query_list for i in bad_entity):
		print"\n\t I feel humiliated...please talk politely"
		c.cjb()

	elif any(i in query_list for i in exit_entity):
		print"\n\t  I will miss you...see you soon!"
		for i in range(4):
			print"\t\t\t\t      \b\b"
			os.system('color 1A')
			os.system('color 2B')
			os.system('color 3C')
			os.system('color 4D')
			
		os.system('cls')
		import main
		
	elif any(i in query_list for i in love_entity):
		print"\n\t I love you too..."
		c.cjb()
		
	elif any(i in query_list for i in name_entity):
		print"\n\t Hello, how may I help you?"
		c.cjb()
	
	elif any(i in query_list for i in salutation_entity):
		print"\n\t Hello dude, How may I help you?"
		c.cjb()
		
	elif all(i in query_list for i in enter_expense_entity):
		print"\n\t\t INSIGHTS TO ENTER EXPENSE"
		print"\t. if you are already a user of the application sign in"
		print"\t. if not sign up and register yourself"
		print"\t. then sign in to the application and then enter your\n\t  income to start the day with"
		print"\t. options appear, choose enter expense"
		print"\t. enter a valid expenditure and the amount spent on it"
		print"\t. if your expense not found in the list, type add"
		print"\t. now you can add your own expense!"
		print"\t. HOLA! your expense is added to the database"
		
		s=str(raw_input("\n\t> satisfied: "))
		if s.lower()=="yes" or s.lower()=="yeah":
			print"\t good to hear! :)"
			print"\t now please dont spend too much, else you will\n\t become poor one day"
		elif s.lower() in bad_entity:
			print"\t I asked if you are satisfied or not?"
			print"\t Learn manners first"
			
		else:
			print"\t mail your query to me at cjb@gmail.com\n\t I will give a clear explanation"
		c.cjb()
	
	elif all(i in query_list for i in view_expense_entity):
		print"\n\t\t INSIGHTS TO VIEW EXPENSE"
		print"\t. if you are already a user of the application sign in"
		print"\t. if not sign up and register yourself"
		print"\t. then sign in to the application and then enter your\n\t  income to start the day with"
		print"\t. options appear, choose enter expense"
		print"\t. enter a valid expenditure and the amount spent on it"
		print"\t. HOLA! your expense is added to the database"
		print"\t. options appear, choose view expense"
		print"\t. HOLA again! your expenses are displayed"
		print"\t. to view your stats too, choose view stat in options"
		print"\t. HOLA again dude! your expense stats are shown"
		
		s=str(raw_input("\n\t> satisfied: "))
		if s.lower()=="yes" or s.lower()=="yeah":
			print"\t good to hear! :)"
			print"\t now please dont spend too much, else you will\n\t become poor one day"
			
		elif s.lower() in bad_entity:
			print"\t I asked if you are satisfied or not?"
			print"\t Learn manners first"
			
		else:
			print"\t mail your query to me at cjb@gmail.com\n\t I will give a clear explanation"
		c.cjb()
		
	elif all(i in query_list for i in enter_income_entity):
		print"\n\t\t INSIGHTS TO ENTER INCOME"
		print"\t. if you are already a user of the application sign in"
		print"\t. if not sign up and register yourself"
		print"\t. then sign in to the application and then enter your\n\t  income to start the day with"
		print"\t. if you want to add more income choose enter income\n\t option from the option menu"
		print"\t. add more income in the given field and view your\n\t income sheet"
		
		s=str(raw_input("\n\t> satisfied: "))
		if s.lower()=="yes" or s.lower()=="yeah":
			print"\t good to hear! :)"
			print"\t now please dont spend too much, else you will\n\t become poor one day"
			
		elif s.lower() in bad_entity:
			print"\t I asked if you are satisfied or not?"
			print"\t Learn manners first"
			
		else:
			print"\t mail your query to me at cjb@gmail.com\n\t I will give a clear explanation"
		c.cjb()
	
	elif any(i in query_list for i in login_entity):
		print"\n\t\t INSIGHTS TO REGISTER AND LOGIN"
		print"\t. if you are already a user of the application sign in"
		print"\t. if not sign up and register yourself"
		print"\t. then sign in to the application and then enter your\n\t  income to start the day with"	
		
		s=str(raw_input("\n\t> satisfied: "))
		if s.lower()=="yes" or s.lower()=="yeah":
			print"\t good to hear! :)"
			print"\t now please dont spend too much, else you will\n\t become poor one day"
			
		elif s.lower() in bad_entity:
			print"\t I asked if you are satisfied or not?"
			print"\t Learn manners first"
			
		else:
			print"\t mail your query to me at cjb@gmail.com\n\t I will give a clear explanation"
		c.cjb()
	
	elif any(i in query_list for i in date_entity):
		print"\n\t today's date and time is ", time.asctime( time.localtime(time.time()))
		c.cjb()
		
	elif any(i in s for i in travel_entity):
		print"\n\t WOW! thats good to hear.."
		print"\t be careful and stay safe"
		print"\t happy adventure :)"
		c.cjb()
		
	else:
		print"\n\t I dont understand you :("
		print"\t please ask this to google :)"
		c.cjb()
	
	
