import random
Name1=str(input("""Enter your Name: """))
Name2=str(input("""\nEnter your friend name:"""))
ran=random.randint(30,100)
if(ran<=50):
	print("\n",Name1,"you donot love",Name2,"...your love % is only :",ran,"%")
elif(ran<70):
	print("\n",Name1,"you love ",Name2,"...but your love % is only",ran,"%")
elif(ran<90):
	print("n",Name1,"you love ",Name2,"very much..I advice you to marry",Name2,"soon...your love % is",ran)
else:
	print("""\ni don't have any word to expain your love,,,
		you are a true lover""",Name2,""" is very lucky thats why""",Name2,"""found you ...
		I wish both of you for success of your relation and love 
		your love % is very high that our machine can not able to disply it..""")



condition=str(input("""\nDo you wanna play again[yes/no]:
 """))
while(condition=='yes'):
	Name1=str(input("\nEnter your Name: "))
	Name2=str(input("\nEnter your friend Name: "))
	ran=random.randint(30,100)
	if(ran<50):
		print("\n",Name1,"you donot love",Name2,"...your love % is only :",ran,"%")
	elif(ran<70):
		print("\n",Name1,"you love ",Name2,"...but your love % is only",ran,"%")
	elif(ran<90):
		print("\n",Name1,"you love ",Name2,"very much..I advice you to marry",Name2,"soon...your love % is",ran)
	else:
		print("""\ni don't have any word to expain your love,,,
		you are a true lover""",Name2,""" is very lucky thats why""",Name2,"""found you ...
		I wish both of you for success of your relation and love 
		your love % is very high that our machine can not able to disply it..""")

	condition=str(input("\nDo you wanna play again[yes/no]: "))