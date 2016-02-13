#######################################################
# Author:	Charlene Y. Quiz
# Studnum:	2013-68102
# CMSC128 Assignment 001
# Git repo: cmsc128-ay2015-16-assign001-py
#######################################################

######wordsToNum######
# Accepts a whole number from 0 to 100000 and prints
# on screen the number in word form
#FUNCTION DEFINITION##
def wordsToNum( inputstr ):
	i = 0
	outputnum = 0
	temp = 0
	
	##declaration of dictionaries
	numbers = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven' : 7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19}

	tens = {'ten':10, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90}

	places = {'million':1000000, 'thousand':1000, 'hundred':100}

	input_list = inputstr.split();
	x = len(input_list)

	##wordsToNum implementation
	while ( len(input_list) > 0 ):												#while the list is not empty
		if ( numbers.has_key(input_list[0])) :									#checks if word is less than 20
			temp += numbers[input_list[0]];					
			del input_list[0]													#remove input as it is added
		elif (tens.has_key(input_list[0]) ) :									#checks if word is a multiple of ten
			temp += tens[input_list[0]]
			del input_list[0]
		elif (places.has_key(input_list[0])):									#checks if word shows place
			if (input_list[0] == 'hundred' and 'thousand' in input_list) :		#check if the place is 'hundred thousand'
				outputnum += temp*100000
				del input_list[0]
			else :																#else, use key and multiply to value
				outputnum += temp*places[input_list[0]]
				del input_list[0]
			temp = 0

	outputnum += temp															#accumulate answer in outputnum	
	return outputnum															#return outputnum
#END OF FUNCTION DEF##



######numToWords######
# Accepts a number in word form
# and returns it in numerical form
#FUNCTION DEFINITION##
def numToWords( inputnum ):
	y = 1000000
	thousand = False;
	
	##declaration of dictionaries
	digits = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}

	tens = {0:"", 1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"};

	places = {100:"hundred", 1000:"", 100000:"hundred", 1000000:"million", 0:"", 10000:"", 10:"", 1:""};

	##numToWords implementation
	while (inputnum >= 0 and y > 0):
		x = inputnum/y
		if ( y < 1000 ) :								#if y < 1000, there are less complications in conversion so it is separated
			if ( y != 10) :								#use conditional statements to find the right word from the dictionary
				print digits[x],
				if ( x != 0 ) :
					print places[y],
			elif (y == 10) :
				if ( inputnum > 19 ) :
					print tens[x],
				else :
					print digits[inputnum],
		elif ( y > 1000 and y < 1000000) :
			if ( y != 10000) :
				print digits[x],
				if ( x != 0 ) :
					print places[y],
					thousand = True						#use thousand variable as flag to show that 'thousand' should be printed	
			elif (y == 10000) :
				if ( inputnum > 19 ) :
					print tens[x],
					if (x != 0) :
						thousand = True
				else :
					print digits[inputnum],
					if (inputnum != 0) :
						thousand = True	
		else :											#basically, this would be x million
			print digits[x],
			if (x != 0) :
				print places[y],
	
		if ( y == 1000 and thousand == True) :
			print "thousand",
	
		inputnum = inputnum%y
		y /= 10
	print ''
	return
#END OF FUNCTION DEF##



######wordsToCurrency######
# Accepts two arguments: the first argument is 
# the number in word form and the second argument is either JPY, PHP, USD. 
# The function returns the number in words to its numerical form
# with a prefix of the currency
####FUNCTION DEFINITION####
def wordsToCurrency( inputstr, currency):
	##concatenate currency and number in numerical form
	return currency + str(wordsToNum(inputstr))
####END OF FUNCTION DEF####



######numberDelimited######
# Accepts three arguments:
# [1] number from 0 to 1000000
# [2] delimiter to be used
# [3] number of jumps when the delimiter will appear
####FUNCTION DEFINITION####
def numberDelimited(inputnum, delimiter, jumps):
	numString = str(inputnum)
	numStringLen = len(numString)
	mid = numStringLen - jumps

	##slice the number based on number of jumps, insert delimiter and print the rest of the number
	print "%s%s%s" % (numString[:(mid)],delimiter,numString[mid:numStringLen])	

	return
####END OF FUNCTION DEF####


####FUNCTION CALLS####
#wordsToNum("one million three hundred fifty seven thousand two hundred twenty three")
#numToWords(1567234)
#wordsToCurrency("one thousand two hundred thirty four", "USD")
#numberDelimited(1234, ',', 3)





