import re

def preprocessLine(inputLine):
	"""
	Cleaning the information in the body tags of each row of file
	"""
	i = inputLine.split("Body=")						#using the split function to get the body data from the row
	y1 = re.sub('&lt;', '<', i[1])						#converting the special characters to their original form using the referencing table
	y2 = re.sub('&gt;', '>', y1)
	y3 = re.sub('&amp;', '&', y2)
	y4 = re.sub('&quot;', '\"', y3)
	y5 = re.sub('&apos;', '\'', y4)
	y6 = re.sub('&#xA;', ' ', y5)
	y7 = re.sub('&#xD;', ' ', y6)
	y8 = re.sub('<[\w| |\/\":.\-=]*>', '', y7)				#cleaning the data off all the html tags
	# y8 = re.sub('<.*>', '', y7)
	y9 = re.sub('\/>', '', y8)								#further cleaning the data using the sub function of re libary
	y10 = re.sub('<.*>', '', y9)
	y11 = re.sub('https:\/\/[\S]*|http:\/\/[\S]*', ' ', y10)			#removing the https hyperlinks from the body text
	return y11





def splitFile(inputFile, outputFile_question, outputFile_answer):
	"""
	Upon completion of the pre-processing tasks the contents of the post will be saved as two
	individual files and an output confirmation will be printed. The preprocessLine() function is called within
	this function.
	"""
	x = open(inputFile, 'r', encoding="utf8")						#opening the input xml file
	q = open(outputFile_question, 'a', encoding="utf8")
	q1 = open(outputFile_answer, 'a', encoding="utf8")
	y = x.readlines()												#using the readlines function to read the lines
	for inputLine in y[2:-2]:										#not reading the first two and last lines of the xml file
		preprocessline = preprocessLine(inputLine)
		z = inputLine.split('PostTypeId=\"')
		if z[1][0] == '1':

			q.write(preprocessline + "\n")
		elif z[1][0] == '2':
			
			q1.write(preprocessline + "\n")
	x.close()
	q1.close()
	q.close()
	print("File has been successfully split into Questions and Answers")
	return True





if __name__ == "__main__":

	f_data = "data.xml"
	f_question = "question.txt"
	f_answer = "answer.txt"

	splitFile(f_data, f_question, f_answer)
