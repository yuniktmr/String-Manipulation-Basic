#CSCI 450 Section 1
#Student Name: Yunik Tamrakar
#Student ID: 10602304
#Homework #7
#Program that uses oython function to perform word count, frequency and string replacement operation
#In keeping with the Honor Code of UM, I have neither given nor received assistance
#from anyone other than the instructor.
#----------------------
#--------------------
#method to get number of words in string
def wordCount(a):
	b = a.split(" ")
	count = 0
	for word in b:
		count = count + 1
	print("The number of words is {}".format(count))
#method to get the most repititive word
def mostFrequentWord(b):
	c = b.split(" ")
	dict = {}
	#mapping word with its wordcount.
	for word in c:
		dict[word] = c.count(word)
	max = 0
	for word in dict:
		if (dict[word] > max):
			max = dict[word]
	for word in dict:
		if(dict[word] == max):
			print('The word with max occurence is', word)
#method to replace the words in the string
def replaceWord(a, d ,c):
	words = a.split(" ")
	wordCheck = False
	for word in words:
		if d == word:
			wordCheck = True
	if wordCheck:
		print("\nOriginal is ",a)
		print("The new string after replacement is ",a.replace(d,c))	
	else:
		print("Word not found")
#main method to call the functions
a= input("Enter a word\n")
wordCount(a)
mostFrequentWord(a)
b = input("\nEnter a word you want to be replaced. Separate them with a space\n")
c  = b.split(" ")
#invoke the replaceWord method
replaceWord(a, c[0], c[1])

