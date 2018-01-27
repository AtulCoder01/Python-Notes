def main():
	mymsg = input('Enter the text to Encrypt:')
	mykey = 8
	ciphertext = encryptMessage(mykey, mymsg)
	print (ciphertext)

def encryptMessage(key, message):
	ciphertext = ['']*8
	for col in range(key):
		pointer = col
		while pointer < len(message):
			ciphertext[col] += message[pointer]
			pointer += key
	return ''.join(ciphertext)

if __name__ == '__main__':
	main()
