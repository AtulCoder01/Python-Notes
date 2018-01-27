msg = input('Please input the Text:')
translate = ''
i = len(msg)-1
while i>=0:
	translate = translate + msg[i]
	i -= 1
print ('your Reversed Text is:'+translate)
