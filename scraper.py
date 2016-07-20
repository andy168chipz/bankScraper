__author__ = 'Andy'
import csv
import re
from textblob.classifiers import NaiveBayesClassifier

# Helper method for retuning a dataset for the classifier


def datasetboa(name):
	reader = csv.DictReader(open(name))
	return [(re.compile('|'.join(map(re.escape, row['Address'].split()))).sub('', row['Payee']), row["Type"]) for row in reader]


def datasetchase(name):
	reader = csv.DictReader(open(name))
	return [(row['Description'], row['Type']) for row in reader]


def boa(filename):
	"""
	For BOA style statement CSV file
	:param filename:
	:return: return an array of all statements with the addition of a type
	"""
	#training data and test data
	trainingSet = datasetboa('training.csv')
	testSet = datasetboa('test.csv')

	#Train the Classifier
	cl = NaiveBayesClassifier(trainingSet)
	cl.update([('NETFLIX.COM NETFLIX.COM CA','Shopping_Entertainment_Miscellaneous')])

	# print "Accuracy using test.csv %f" %cl.accuracy(testSet)
	stmt_reader = csv.DictReader(open(filename))
	for row in stmt_reader:
		row['Type'] = cl.classify(row['Payee'])
		print row


def chase(filename):
	"""

	For chase style statement CSV file
	:param filename:
	:return: return an array of all statements with the addition of type
	"""
	trainingSet = datasetchase('stmt_chase.csv')
	cl = NaiveBayesClassifier(trainingSet)
	# print "Accuracy using test.csv %f" %cl.accuracy(testSet)
	stmt_reader = csv.DictReader(open(filename))
	for row in stmt_reader:
		row['Type'] = cl.classify(row['Description'])
		print row


def ae():
	pass

#set up dictionary for actions
choice = {
	"boa": boa,
	"chase": chase,
	"ae": ae
}

if __name__ == '__main__':
	chase('stmt_chase.csv')
	# boa('stmt_boa.csv')