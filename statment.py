__author__ = 'Andy'
import csv
import datetime
import time

rows_sum = {}
category_xml = {}
category_details = {'Food':( 40000, 255),
					'Gas':( 35000, 65535),
					'Shopping':( 25000, 16711680),
					'Entertainment':( 25000, 12632256),
					'Travel':( 60000, 16776960),
					'Misc':( 40000, 16711935),
					'Insurance':( 50000, 16711680)}
banks = ['ae', 'boa', 'chase', 'citi']


def scrape(statement):
	try:
		reader = csv.DictReader(open(statement))
	except IOError, e:
		print e
		return
	for row in reader:
		xml_string = xml(row['Amount'], row['Posted Date'], row['Payee'], row['Address'])
		#calculate sum
		if row['Category']:
			try:
				rows_sum[row['Category']] = float(row['Amount']) + rows_sum[row['Category']] if row['Category']in rows_sum else float(row['Amount'])
			except ValueError:
				print str(row['Amount']) + "+=this is wrong? debit"
		#make xml format dict
			category_xml[row['Category']] = category_xml[row['Category']]+[xml_string] if row['Category'] in category_xml else [xml_string]


def xml(amount, date, payee, address):
		return '<Spent amount="{}" desc="" recurring="no" tentative="no" time="{}" where="{}"/>'.format(format_amount(amount), convert_time(date), payee if payee else address)


def format_amount(num):
	print type(num), num
	return int(-float(num)*100)



def convert_time(date):
	#m/d/y
	m, d, y = map(int, date.split("/"))
	temp = datetime.date(y, m, d)
	return int(time.mktime(temp.timetuple()))


def print_xml():
	for k, v in category_xml.iteritems():
		print '<Category amount_is_percentage="false" budget="{}" color="{}" desc="" fixed="no" hide_balance_graph="yes" hide_pie_graph="yes" name="{}" sort_by="DATE" sort_reverse="no">'.format(category_details[k][0],category_details[k][1],k)
		for str in v:
			print str
		print '</Category>'


def print_statements(month):
	#get from each
	for x in banks:
		print x, month
		scrape('statements/{}/{}2016.csv'.format(x, month))
	print_xml()

# print_statements('May')

scrape('statements/boa/May2016.csv')