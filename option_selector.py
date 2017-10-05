def opt():
	import enterdata as ed
	import viewdata as vd
	import option_selector as o
	import os
	import sys
	print"\n\t options:"
	print"\t. enter expense"
	print"\t. enter income"
	print"\t. view expense"
	print"\t. view stat"
	print"\t. quit"
	option=str(raw_input("\t> enter your option: "))
	a=["enter expense","view expense","view stat","enter income","quit"];
	if option in a:
		if option.lower()==a[0]:
			print "\n\tentering into your module::"
			ed.enter_data()
			
		elif option.lower()==a[1]:
			print "\n\tsearching your data::"
			vd.view_data()
			
		elif option==a[2]:
			print "\n\tanalysing your stats::\n\t"
			vd.view_stat()
			
		elif option.lower()==a[3]:
			ed.enter_income()
			
		elif option==a[4]:
			print "\n\t\t     quitting..."
			print "\t         see you soon buddy "
			for i in xrange(200):
				print"\n\n\t\t -                 "
			import main
			
	else:
		o.opt()
		print "\tsorry wrong option, enter correct option.."
	
	
	
	

