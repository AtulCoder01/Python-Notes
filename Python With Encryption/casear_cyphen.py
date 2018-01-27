msg = input('Enter the Text:')
key = 15
mode = 'Encrypt'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translate = ''
msg = msg.upper()
for symbol in msg:
	if symbol in LETTERS:
		num = LETTERS.find(symbol)
		if mode == 'Encrypt':
			num = num + key #shift one letter
		elif mode == 'Decrypt':
			num = num - key 
	
		if num >= len(LETTERS):
			num = num - len(LETTERS)
		elif num < 0:
			num = num + len(LETTERS)
		translate = translate + LETTERS[num]
	else:
		translate = translate + symbol

print (translate)
