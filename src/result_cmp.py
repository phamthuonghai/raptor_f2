import csv
import string
from optparse import OptionParser
from operator import itemgetter

def file_to_map(filecontent):
	rows = list(filecontent)
	res = {}
	for row in rows:
		parse_data = row.split()
		res[parse_data[1]] = {}
		for i in range(2, len(parse_data)):
			new_parse = parse_data[i].split('-')
			res[parse_data[1]][new_parse[1]] = new_parse[0]

	return res

def delete0(d):
	t = []
	for k1, v1 in d.iteritems():
		for k2, v2 in v1.iteritems():
			if (v2 == '0.00'):
				t.append((k1,k2))

	for item in t:
		del d[item[0]][item[1]]

	return d

def cmpr(f1, f2):
	dict1 = delete0(file_to_map(open(f1)))
	dict2 = delete0(file_to_map(open(f2)))
	
	if (len(dict1) != len(dict2)):
		return "Diff in size dict1 vs dict2 = " + len(dict1) + " " + len(dict2)

	for k1, v1 in dict1.iteritems():
		t1 = sorted(v1.values(), reverse = True)
		t2 = sorted(dict2[k1].values(), reverse = True)
		if (t1 != t2):
			print t1
			print t2
			return "Diff at key " + k1
	return "Identical"

if __name__ == "__main__":
	optparser = OptionParser()
	optparser.add_option('-i', '--f1',
						dest='file1',
						help='path to file #1',
						default='')
	optparser.add_option('-o', '--f2',
						dest='file2',
						help='path to file #2',
						default='')

	(options, args) = optparser.parse_args()
	print cmpr(options.file1, options.file2)