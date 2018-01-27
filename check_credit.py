def which_card(an):
	y=int(an[0]+an[1]+an[2]+an[3]+an[4]+an[5])#store 6 digit in A/C Number
	if (y>=501800 and y<501900) or (y>=502000 and y<502100) or (y>=503800 and y<503900) or (y>=589300 and y<589400) or (y>=630400 and y<630500) or (y>=675900 and y<676000) or (y>=676100 and y<676400):
		return "Maestro"
	elif (y>=510000 and y<560000) or (y>=222100 and y<=272099):
		return "MasterCard"
	elif y>=400000 and y<500000:
		if (y>=402600 and y<402700) or (y>=417500 and y<417501) or (y>=450800 and y<450900) or (y>=484400 and y<484500) or (y>=491300 and y<491400) or (y>=491700 and y<491800):
			return "Visa Electron"
		else :
			return "Visa"
	elif (y>=637000 and y<640000):
		return "InstaPayment"
	elif (y>=352800 and y<=358900):
		return "JCB"
	elif (y>=601100 and y<601200) or (y>=644000 and y<648000) or (y>=650000 and y<660000) or (y>=622126 and y<=622925) or (y>=648000 and y<650000):
		return "Discover"
	elif (y>=340000 and y<350000) or (y>=370000 and y<380000):#15 number
		return "American Express"
	elif y>=300000 and y<306000:
		return "Diners Club-Carte Blanche"
	elif y>=360000 and y<370000:
		return "Diners Club-International"
	elif y>=540000 and y<550000:
		return "Diners Club-USA & Canada"
	

def vailed_card(x):#x is A/C Number
	x=x[::-1]
	print(x)
	add=0
	for y in range(0,len(x)):
		if y%2!=0:
			z=int(x[y])*2
			if(z>9):
				z=z-9#z=1+(z-10)
				#z=str(z)
				#z=int(z[0]+z[1])	
		else:
			z=int(x[y])
		add=add+z
	if add%10==0:
		return "Vailed"
	else:
		return "Invailed"

if __name__=='__main__':
	ac = input("Enter your Cradit Card Number: ")
	print("*******************************************************")
	card_nm=which_card(ac)
	card_vailidate=vailed_card(ac)
	if card_vailidate=="Vailed":
		print("Card Name:",card_nm)
		print("Your Card is",card_vailidate)
	else:
		print("Your Card is",card_vailidate)
	print("*******************************************************")



	

