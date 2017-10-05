cnt=0
new_value=0.0
new_key=0.0

def enter_data():
	print "\n\n\n\twelcome to Expense Manager...."
	import time 
	import calendar
	import datetime
	import expensedata as ed
	import option_selector as o 
	import enterdata as e
	import math
	import os
	os.system('cls')
	j=0
	print "\n\n\tYour expense on ",time.asctime( time.localtime(time.time())),"in:- \n"
	for i in  ed.expenses.keys():
		print "\t",j+1," ",i
		j+=1	
	
	ins=str(raw_input("\t> your expense today in: "))
	if ins=="add":
		try:
			key=str(raw_input("\t> your new expense in: "))
		except:
			print"\n\t Wrong input type"
			key=str(raw_input("\t> your new expense in: "))
		try:
			val=float(input("\t> your expenditure: "))
		except:
			print"\n\t Wrong input type"
			val=float(input("\t> your expenditure: "))
			
		ed.expenditure += val
		ed.balance-=val
		e.cnt+=1
		ed.expenses[key]=val
		print "\t",key," = ",val
		j=0
		o.opt()
			
	
	elif int(ins)<len(ed.expenses)+1:
		n=int(ins)	
		try:
			exp=float(input("\t> your expense: "))
		except:
			print"\n\t re enter"
			exp=float(input("\t> your expense: "))
		e.new_value=exp
		e.new_key=n
		if ed.expenses.has_key(ed.expenses.keys()[n-1]):
			exp+=ed.expenses.values()[n-1]
			ed.expenditure+=exp
			ed.balance-=exp
			ed.expenses.update({ed.expenses.keys()[n-1]: exp})
			print "\t",ed.expenses.keys()[n-1]," = ",exp
			e.cnt+=1
			j=0
			o.opt()
			
	else:
		import enterdata as e
		print "\n\t wrong input"
		e.enter_data()
			
		

def enter_income():
	import option_selector as o
	import enterdata as ed
	import expensedata as e
	print "\n\n\tentering into module..."
	print"\n\tavailable balance  = ",e.balance
	try:
		inc=float(input("\t> enter your income:  "))
		e.income+=inc
	except :
		print"\n\twrong value type"
		print"\t  enter again"
		ed.enter_income()
	e.balance+=inc
	print "\tyour income is     = ",inc
	print"\tyour new balance   = ",e.balance
	o.opt()
	
	

	
	




	
	
		
			
	
