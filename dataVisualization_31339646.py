import parser_31339646
import matplotlib.pyplot as plt

"""
This file will implement two functions to visualise the statistics as some form of graphs. The implementation of these two
functions make use of the external Python package including Matplotlib
"""

def visualizeWordDistribution(inputFile, outputImage):
	"""Function to visualize vocabulary size for each post using a bar chart"""
	"""Initializing the variables to be used"""
	y0 = 0
	y10 = 0
	y20 = 0
	y30 = 0
	y40 = 0
	y50 = 0
	y60 = 0
	y70 = 0
	y80 = 0
	y90 = 0
	y100 = 0

	x = open(inputFile, 'r', encoding="utf8")
	y = x.readlines()
	for l in y[2:-2]:

		x = parser_31339646.Parser(l)                 #calling imported function
		if x.getVocabularySize() < 10:					#calculating vocab size
			y0 += 1
		elif x.getVocabularySize() > 9 and x.getVocabularySize() < 20:
			y10 += 1
		elif x.getVocabularySize() > 19 and x.getVocabularySize() < 30:
			y20 += 1
		elif x.getVocabularySize() > 29 and x.getVocabularySize() < 40:
			y30 += 1
		elif x.getVocabularySize() > 39 and x.getVocabularySize() < 50:
			y40 += 1
		elif x.getVocabularySize() > 49 and x.getVocabularySize() < 60:
			y50 += 1
		elif x.getVocabularySize() > 59 and x.getVocabularySize() < 70:
			y60 += 1
		elif x.getVocabularySize() > 69 and x.getVocabularySize() < 80:
			y70 += 1
		elif x.getVocabularySize() > 79 and x.getVocabularySize() < 90:
			y80 += 1
		elif x.getVocabularySize() > 89 and x.getVocabularySize() < 100:
			y90 += 1
		elif x.getVocabularySize() > 99:
			y100 += 1

	n = []
	n.append(y0)
	n.append(y10)
	n.append(y20)
	n.append(y30)
	n.append(y40)
	n.append(y50)
	n.append(y60)
	n.append(y70)
	n.append(y80)
	n.append(y90)
	n.append(y100)

	n2 = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100', 'Others']
	plt.figure(figsize=(12, 12))				#Increasing the figure size for the plot
	plt.title("Word Number Distribution")
	"""Adding the labels and title for plot"""
	plt.xlabel("Vocabulary Size")
	plt.ylabel("Number of post of their respective size")
	plt.bar(n2, n)             #ploting a bar chart
	print("Word Number Distribution plot has been successfully created and has been saved in the root folder.")
	return plt.savefig(outputImage)



def visualizePostNumberTrend(inputFile, outputImage):
	"""
	This function displays the trend of the post number in the Q&A site. First the number of questions and answers
	is calculated for each quarter. Then following the time order, you should draw a line chart to annotate the
	number of posts in each quarter.
	"""
	q15q3, q15q4, q16q1, q16q2, q16q3, q16q4, q17q1, q17q2, q17q3, q17q4, q18q1, q18q2, q18q3, q18q4, q19q1 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	a15q3, a15q4, a16q1, a16q2, a16q3, a16q4, a17q1, a17q2, a17q3, a17q4, a18q1, a18q2, a18q3, a18q4, a19q1 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	x = open(inputFile, 'r', encoding="utf8")
	y = x.readlines()
	for l in y[2:-2]:

		x = parser_31339646.Parser(l)				#instantiating the classes from imported class
		if x.dateQuarter == '2015Q3':				#calculating the number of questions or answers
			if x.type == '1':
				q15q3 += 1							#calculating the number of questions
			elif x.type == '2':
				a15q3 += 1							#calculating the number of answers
		elif x.dateQuarter == '2015Q4':
			if x.type == '1':
				q15q4 += 1
			elif x.type == '2':
				a15q4 += 1
		elif x.dateQuarter == '2016Q1':
			if x.type == '1':
				q16q1 += 1
			elif x.type == '2':
				a16q1 += 1
		elif x.dateQuarter == '2016Q1':
			if x.type == '1':
				q16q1 += 1
			elif x.type == '2':
				a16q1 += 1
		elif x.dateQuarter == '2016Q2':
			if x.type == '1':
				q16q2 += 1
			elif x.type == '2':
				a16q2 += 1
		elif x.dateQuarter == '2016Q3':
			if x.type == '1':
				q16q3 += 1
			elif x.type == '2':
				a16q3 += 1
		elif x.dateQuarter == '2016Q4':
			if x.type == '1':
				q16q4 += 1
			elif x.type == '2':
				a16q4 += 1
		elif x.dateQuarter == '2017Q1':
			if x.type == '1':
				q17q1 += 1
			elif x.type == '2':
				a17q1 += 1
		elif x.dateQuarter == '2017Q2':
			if x.type == '1':
				q17q2 += 1
			elif x.type == '2':
				a17q2 += 1
		elif x.dateQuarter == '2017Q3':
			if x.type == '1':
				q17q3 += 1
			elif x.type == '2':
				a17q3 += 1
		elif x.dateQuarter == '2017Q4':
			if x.type == '1':
				q17q4 += 1
			elif x.type == '2':
				a17q4 += 1
		elif x.dateQuarter == '2018Q1':
			if x.type == '1':
				q18q1 += 1
			elif x.type == '2':
				a18q1 += 1
		elif x.dateQuarter == '2018Q2':
			if x.type == '1':
				q18q2 += 1
			elif x.type == '2':
				a18q2 += 1
		elif x.dateQuarter == '2018Q3':
			if x.type == '1':
				q18q3 += 1
			elif x.type == '2':
				a18q3 += 1
		elif x.dateQuarter == '2018Q4':
			if x.type == '1':
				q18q4 += 1
			elif x.type == '2':
				a18q4 += 1
		elif x.dateQuarter == '2019Q1':
			if x.type == '1':
				q19q1 += 1
			elif x.type == '2':
				a19q1 += 1

	questionslist = []
	answerslist = []
	questionslist.append(q15q3)
	questionslist.append(q15q4)
	questionslist.append(q16q1)
	questionslist.append(q16q2)
	questionslist.append(q16q3)
	questionslist.append(q16q4)
	questionslist.append(q17q1)
	questionslist.append(q17q2)
	questionslist.append(q17q3)
	questionslist.append(q17q4)
	questionslist.append(q18q1)
	questionslist.append(q18q2)
	questionslist.append(q18q3)
	questionslist.append(q18q4)
	questionslist.append(q19q1)

	answerslist.append(a15q3)
	answerslist.append(a15q4)
	answerslist.append(a16q1)
	answerslist.append(a16q2)
	answerslist.append(a16q3)
	answerslist.append(a16q4)
	answerslist.append(a17q1)
	answerslist.append(a17q2)
	answerslist.append(a17q3)
	answerslist.append(a17q4)
	answerslist.append(a18q1)
	answerslist.append(a18q2)
	answerslist.append(a18q3)
	answerslist.append(a18q4)
	answerslist.append(a19q1)
	plt.clf()
	time = ['2015Q3', '2015Q4', '2016Q1', '2016Q2', '2016Q3', '2016Q4', '2017Q1', '2017Q2', '2017Q3', '2017Q4', '2018Q1', '2018Q2', '2018Q3', '2018Q4', '2019Q1']
	plt.figure(figsize=(12,12))
	"""Adding the labels and title for plot and increasing figure size"""
	plt.title("Post Number Trend")
	plt.xlabel("Time")
	plt.ylabel("Number of post per Quarter")
	plt.plot(time, questionslist, label='Questions')
	plt.plot(time, answerslist, label='Answers')
	plt.legend(loc='upper right')
	print("\nPost Number Trend plot has been successfully created and has been saved in the root folder.")
	return plt.savefig(outputImage)				#saving output image



if __name__ == "__main__":

	f_data = "data.xml"
	f_wordDistribution = "wordNumberDistribution.png"
	f_postTrend = "postNumberTrend.png"
	
	visualizeWordDistribution(f_data, f_wordDistribution)
	visualizePostNumberTrend(f_data, f_postTrend)
