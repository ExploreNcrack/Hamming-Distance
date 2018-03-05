

def hamming_distance(inputstring,distance,current_index):

	if distance==0:

		print(inputstring)
		return


	else:
		before = inputstring
			
		for i in range(current_index,len(inputstring)):
			if inputstring[i] == '0':
				hamming_distance(before[:i]+'1'+before[i+1:],distance-1,i+1)
			elif inputstring[i] == '1':
				hamming_distance(before[:i]+'0'+before[i+1:],distance-1,i+1)

			before = inputstring


input_string = input('Please enter a continuous 0 and/or 1s (eg:01010101): ')
#input_string = '0000101010101010'
distance = 5
inputstring = input_string

if len(inputstring) < distance:
	print('invalid distance input')

else:
    
	for i in range(len(inputstring)):
		if i + distance <= len(inputstring): 
			if inputstring[i]=='0':
				
				inputstring=inputstring[:i] + '1' + inputstring[i+1:]
				
			elif inputstring[i]=='1':

				inputstring=inputstring[:i] + '0' + inputstring[i+1:]
				
			

			hamming_distance(inputstring ,distance-1,i+1,)

			

			inputstring = input_string

		else:
			break



