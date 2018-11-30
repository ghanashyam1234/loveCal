#python program to input electricity unit and calculate total electricity bill according to given condition
#for first 50 units Rs 0.50/unit
#for next 100 units Rs 0.75/unit
#for next 100 units Rs 1.2/unit
#for unit above 250 Rs 1.5/unit
#An additional surcharge of 20%is added to bill

unit=int(input("enter your unit: "))
if(unit<=50):
	bill1=unit*0.5
	tb1=bill1+(bill1*20)/100
	print("your bill is:",tb1)
elif(unit<=150):
	bill2=(50*.5)+(unit-50)*.75
	tb2=bill2+(bill2*20)/100
	print("your bill is",tb2)
elif(unit<=250):
	bill3=(50*.5)+(100*.75)+(unit-150)*1.2
	tb3=bill3+(bill3*20)/100
	print("your bill is",tb3)
elif(unit>250):
	bill4=(50*.5)+(100*.75)+(100*1.2)+(unit-250)*1.5
	tb4=bill4+(bill4*20)/100
	print("your bills is",tb4)
