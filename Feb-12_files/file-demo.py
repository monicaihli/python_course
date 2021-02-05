a_file = open('./myfile.txt', encoding='utf-8')
contents_1 = a_file.read() # read the whole thing as one string

contents_2 = a_file.readline() 	#return one line at a time

contents_3 = a_file.readlines() # returns the entire file as a list of lines

a_file.close()
print('a')