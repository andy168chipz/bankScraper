__author__ = 'Andy'
import csv
import re
from textblob.classifiers import NaiveBayesClassifier


# Helper method for retuning a dataset for the classifier
def dataset(name):
	reader = csv.DictReader(open(name))
	return [(re.compile('|'.join(map(re.escape, row['Address'].split()))).sub('', row['Payee']), row["Type"]) for row in reader]

def main():
	pass


def boa(filename):
	"""
	For BOA style statement CSV file
	:param filename:
	:return: return an array of all statements with the addition of a type
	"""
	#training data and test data
	trainingSet = dataset('training.csv')
	testSet = dataset('test.csv')

	#Train the Classifier
	cl = NaiveBayesClassifier(trainingSet)
	cl.update([('NETFLIX.COM NETFLIX.COM CA','Shopping_Entertainment_Miscellaneous')])

	# print "Accuracy using test.csv %f" %cl.accuracy(testSet)
	stmt_reader = csv.DictReader(open(filename))
	for row in stmt_reader:
		row['Type'] = cl.classify(row['Payee'])
		print row

def chase():
	pass


def ae():
	pass


if __name__ == '__main__':
	boa('stmt_boa.csv')