def view_data():
	import expensedata as e
	import option_selector as o
	import enterdata as ed
	import os
	os.system('cls')
	p=0
	print "\n\n\n"
	tot=0
	for k in e.expenses.values():
		print "\t",e.expenses.keys()[p],"\t"," = ",k
		p+=1
		
	print "\tyour income       = ",e.income
	print "\ttotal expenditure = ",e.expenditure
	print "\tbalance available = ",e.balance
	o.opt()

def return_stat():
	import expensedata as e
	import option_selector as o
	import enterdata as ed
	p=0
	tot=0
	for k in e.expenses.values():
		print "\t",e.expenses.keys()[p],"\t"," = ",k
		p+=1
		tot+=int(k)
	print "\ttotal expenses today = ",ed.cnt
	print "\ttotal expenditure    = ",e.expenditure
	print "\tbalance available    = ", e.balance
	
def view_stat():
	import expensedata as ed
	import matplotlib.pyplot as p
	import option_selector as o
	import matplotlib.patches as pa
	import numpy as np
	import viewdata as vd
	import os
	os.system('cls')
	print "\n"
	vd.return_stat()
	keys_list=[]
	for k in xrange(len(ed.expenses)):
		keys_list.append(k)
	
	print"\t"
	p.xlabel("\nEXPENSE",fontweight='bold')
	p.ylabel("EXPENDITURE\n",fontweight='bold')
	p.title("EXPENSE STATS\n",fontweight='bold')
	x=np.arange(len(ed.expenses))
	p.xticks(x,ed.expenses.keys())
	fig = p.gcf()
	fig.set_size_inches(8,6)
	fig.patch.set_facecolor('green')
	fig = p.gcf()
	fig.canvas.set_window_title('EXPENSE DATA')
	ax = p.gca()
	ax.tick_params(axis='x', colors='yellow')
	ax.tick_params(axis='y', colors='yellow')
	a=['Balance=',str(ed.balance)];
	s=" ".join(a)
	p.text(.85,.95,s,bbox=dict(facecolor='red',alpha=0.5), horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
	p.bar(x, height= ed.expenses.values(),facecolor='blue', edgecolor='white')
	p.show()
	o.opt()
	os.system('cls')
	p.close('all')
	
	
