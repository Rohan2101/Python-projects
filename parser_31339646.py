import preprocessData_31339646
import re
"""
The main function of this file is to further parse the given row of the data in XML format.
"""
class Parser:
	"""
	Docstring for ClassName,this is the constructor required for creating instances of this class. The inputString
	will be the row of data from the XML file.
	"""
	def __init__(self, inputString):								#using the constructor to instantiate the class
		self.inputString = inputString
		self.ID = self.getID()
		self.type = self.getPostType()
		self.dateQuarter = self.getDateQuarter()
		self.cleanBody = self.getCleanedBody()

	def __str__(self):
		# returning the print ID, Question/Answer/Others, creation date, the body content of respective row
		return f'{self.ID}, {self.type}, {self.dateQuarter}, {self.cleanBody}'



	def getID(self):
		"""extracting the ID of each row using the split function"""
		z = self.inputString.split("row Id=\"")
		z1 = z[1][0:10]
		z2 = z1.split("\"")
		ID = z2[0]
		return ID


		

	def getPostType(self):
		"""Using the split function to extract the post type of the row"""
		z = self.inputString.split("PostTypeId=\"")
		z1 = z[1][0:10]
		z2 = z1.split("\"")
		posttype = z2[0]
		return posttype

	def getDateQuarter(self):
		"""Extracting the quarter and year of the post for its respective row"""
		z = self.inputString.split("CreationDate=\"")
		z1 = z[1][0:10]
		if z1[0:4] == '2015':
			if z1[5:7] == '09' or z1[5:7] == '08' or z1[5:7] == '07':
				return '2015Q3'
			elif z1[5:7] == '10' or z1[5:7] == '11' or z1[5:7] == '12':
				return '2015Q4'
		elif z1[0:4] == '2016':
			if z1[5:7] == '01' or z1[5:7] == '02' or z1[5:7] == '03':
				return '2016Q1'
			elif z1[5:7] == '04' or z1[5:7] == '05' or z1[5:7] == '06':
				return '2016Q2'
			elif z1[5:7] == '07' or z1[5:7] == '08' or z1[5:7] == '09':
				return '2016Q3'
			elif z1[5:7] == '10' or z1[5:7] == '11' or z1[5:7] == '12':
				return '2016Q4'
		elif z1[0:4] == '2017':
			if z1[5:7] == '01' or z1[5:7] == '02' or z1[5:7] == '03':
				return '2017Q1'
			elif z1[5:7] == '04' or z1[5:7] == '05' or z1[5:7] == '06':
				return '2017Q2'
			elif z1[5:7] == '07' or z1[5:7] == '08' or z1[5:7] == '09':
				return '2017Q3'
			elif z1[5:7] == '10' or z1[5:7] == '11' or z1[5:7] == '12':
				return '2017Q4'
		elif z1[0:4] == '2018':
			if z1[5:7] == '01' or z1[5:7] == '02' or z1[5:7] == '03':
				return '2018Q1'
			elif z1[5:7] == '04' or z1[5:7] == '05' or z1[5:7] == '06':
				return '2018Q2'
			elif z1[5:7] == '07' or z1[5:7] == '08' or z1[5:7] == '09':
				return '2018Q3'
			elif z1[5:7] == '10' or z1[5:7] == '11' or z1[5:7] == '12':
				return '2018Q4'
		elif z1[0:4] == '2019':
			if z1[5:7] == '01' or z1[5:7] == '02' or z1[5:7] == '03':
				return '2019Q1'
			elif z1[5:7] == '04' or z1[5:7] == '05' or z1[5:7] == '06':
				return '2019Q2'
			elif z1[5:7] == '07' or z1[5:7] == '08' or z1[5:7] == '09':
				return '2019Q3'
			elif z1[5:7] == '10' or z1[5:7] == '11' or z1[5:7] == '12':
				return '2019Q4'
		

	def getCleanedBody(self):
		"""Importing the preprocessingline function from preprocessdata to extact the clean row body"""
		z = preprocessData_31339646.preprocessLine(self.inputString)
		return z
		

	def getVocabularySize(self):
		"""Getting the number of unique words in the cleaned body converted in lower case using the sub and split function"""
		z = re.sub(",|\.|\'|\?|\(|\)|\:", "", self.cleanBody)
		z1 = z.split(" ")

		uniqueWords = []
		for i in z1:
			if i == '':
				pass
			elif i == ' ':
				pass
			elif i == '   ':
				pass
			elif not i.lower() in uniqueWords:
				uniqueWords.append(i.lower())

		return len(uniqueWords)
		




