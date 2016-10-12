__author__ = 'Andy'
import csv
import datetime
import time
'''
		<Category amount_is_percentage="false" budget="40000" color="255" desc="" fixed="no" hide_balance_graph="yes" hide_pie_graph="yes" name="food" sort_by="DATE" sort_reverse="no">
			<Spent amount="27225" desc="" recurring="no" tentative="no" time="1462086000" where="Food BOA"/>
		</Category>
		<Category amount_is_percentage="false" budget="35000" color="65535" desc="" fixed="no" hide_balance_graph="yes" hide_pie_graph="yes" name="gas + clipper" sort_by="DATE" sort_reverse="no">
			<Spent amount="28024" desc="" recurring="no" tentative="no" time="1462086000" where="Gas/Clipper BOA"/>
		</Category>
		<Category amount_is_percentage="false" budget="25000" color="16711680" desc="" fixed="no" hide_balance_graph="yes" hide_pie_graph="yes" name="Shopping" sort_by="DATE" sort_reverse="no"/>
		<Category amount_is_percentage="false" budget="25000" color="16711680" desc="" fixed="no" hide_balance_graph="yes" hide_pie_graph="yes" name="Entertainment" sort_by="DATE" sort_reverse="no">
			<Spent amount="24751" desc="" recurring="no" tentative="no" time="1462086000" where="Entertainment BOA"/>
		</Category>
		<Category amount_is_percentage="false" budget="60000" color="16711680" desc="" fixed="no" hide_balance_graph="yes" hide_pie_graph="yes" name="Travel" sort_by="DATE" sort_reverse="no"/>
		<Category amount_is_percentage="false" budget="40000" color="16711680" desc="" fixed="no" hide_balance_graph="yes" hide_pie_graph="yes" name="Misc" sort_by="DATE" sort_reverse="no">
			<Spent amount="3801" desc="" recurring="no" tentative="no" time="1462086000" where="Misc BOA"/>
			<Spent amount="3801" desc="" recurring="no" tentative="no" time="1462086000" where="Misc BOA"/>
		</Category>
'''
rows_sum = {}
category_xml = {}
category_details = {}

def boa(statement):
	reader = csv.DictReader(open(statement))
	for row in reader:
		xml = '<Spent amount="{}" desc="" recurring="no" tentative="no" time="{}" where="{}"/>'.format(format_amount(row['Amount']), convert_time(row['Posted Date']), row['Payee'] if row['Payee'] else row['Address'])
		#calculate sum
		if row['Category']:
			try:
				rows_sum[row['Category']] = float(row['Amount']) + rows_sum[row['Category']] if row['Category']in rows_sum else float(row['Amount'])
			except ValueError:
				print str(row['Amount']) + "+=this is wrong? debit"
		#make xml format dict
			category_xml[row['Category']] = category_xml[row['Category']]+[xml] if row['Category'] in category_xml else [xml]




def format_amount(num):
	return int(-float(num)*100)

def convert_time(date):
	#m/d/y
	m, d, y = map(int, date.split("/"))
	temp = datetime.date(y, m, d)
	return int(time.mktime(temp.timetuple()))

def print_xml():
	for k, v in category_xml.iteritems():
		print k
		for str in v:
			print str

boa('May2016boa.csv')
# print category_sum
# print sum(category_sum.values())

print_xml()