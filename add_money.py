def money():
	note = [2000, 500, 100, 50, 10]
	j = 0
	add = 0
	total_note = 0
	for i in range(len(note)):
		num_of_note = input("Enter Number of "+str(note[i])+" Note : ")
		if num_of_note != '':
			total_note = total_note + int(num_of_note)
			add = add + int(num_of_note) * int(note[i])
			j += 1
			i += 1
	print("Total Notes =", total_note)
	print("Total Rupees =", add,"/-")

if __name__ == '__main__':
	money()
