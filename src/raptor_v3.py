"""
	python raptor.py -p "./" -o temp_BYS.csv -a BYS -c sg
"""

import csv
import string
from math import sqrt
from optparse import OptionParser
from operator import itemgetter
import os

import time

class Algorithms:
    ORIG, BYS, VTD, VSZ = range(4)

def file_to_map(filecontent):
	rows = list(filecontent)
	res = {}
	for row in rows:
		parse_data = string.split(row)
		res[parse_data[0]] = set(parse_data[1:])
	return res

def list_intersect(l1, l2):
	return list(set(l1).intersection(l2))

def apply_jaccard(algo, size, sku_src, sku_dst, purchase_map, view_map, cart_map):
	res = {}

	if (size <= 0):
		return res

	sku_use_unfiltered = sku_src.union(sku_dst)

	for sku1 in sku_use_unfiltered:
		res[sku1] = {}
		
	# Filter single sku
	if (algo == Algorithms.ORIG or algo == Algorithms.BYS):
		sku_use = sorted([sku for sku in sku_use_unfiltered if sku in purchase_map])
	elif (algo == Algorithms.VTD):
		sku_use = sorted([sku for sku in sku_use_unfiltered if sku in cart_map or sku in purchase_map])
	else:
		sku_use = sorted([sku for sku in sku_use_unfiltered if sku in view_map])

	for sku1 in sku_use:
		for sku2 in sku_use:
			if (sku1 < sku2):

				view_sku = (view_map.get(sku1, set([])), view_map.get(sku2, set([])))
				purchase_sku = (purchase_map.get(sku1, set([])), purchase_map.get(sku2, set([])))
				cart_sku = (cart_map.get(sku1, set([])), cart_map.get(sku2, set([])))

				ints_cart = len(cart_sku[0].intersection(cart_sku[1]))
				ints_view = len(view_sku[0].intersection(view_sku[1]))
				ints_purchase = len(purchase_sku[0].intersection(purchase_sku[1]))
				ints_purchase1_view2 = len(purchase_sku[0].intersection(view_sku[1]))
				ints_view1_purchase2 = len(view_sku[0].intersection(purchase_sku[1]))

				if (algo == Algorithms.ORIG):
					if (ints_cart == 0 or ints_purchase == 0):		#filterUnrelated
						continue
					val = wilson95(ints_purchase, len(purchase_sku[0]) + len(purchase_sku[1]) - ints_purchase)
				elif (algo == Algorithms.BYS):
					if (ints_purchase == 0):	#filterUnrelated
						continue
					val = wilson95(ints_purchase, ints_purchase1_view2 + ints_view1_purchase2)
				elif (algo == Algorithms.VTD):
					if (ints_cart == 0):		#filterUnrelated
						continue
					val = similar_filter_score(sku1, sku2) * ( 
								wilson95(ints_cart, len(cart_sku[0]) + len(cart_sku[1]) - ints_cart)
								+ 0.2 * wilson95(ints_purchase, len(purchase_sku[0]) + len(purchase_sku[1]) - ints_purchase))
				else:
					if (ints_view == 0):		#filterUnrelated
						continue
					val = similar_filter_score(sku1, sku2) * wilson95(ints_view, len(view_sku[0]) + len(view_sku[1]) - ints_view)
				
				if sku2 in sku_dst:
					res[sku1][sku2] = val
				if sku1 in sku_dst:
					res[sku2][sku1] = val
	res_f = {}
	for sku1 in sku_src:
		res_f[sku1] = {}

	for k, v in res.iteritems():
		if (k in sku_src and len(v) > 0):
			sorted_value = sorted(v.items(), key=itemgetter(1), reverse = True)
			t = len(v)
			if (t > size):
				t = size
			res_f[k] = sorted_value[0:t]

	return res_f

def wilson95(p, n):
	if (p <= 0 or n <= 0):
		return 0
	p = float(p)
	n = float(n)
	return 100 * (p + 1.9208 - 1.96 * sqrt(p - p * p / n + 0.9604)) /  (3.8416 + n)

def similar_filter_score(sku1, sku2):
	lev = levenshtein(sku1, sku2)
	if (lev < 3):
		return 0.10
	elif (lev == 3):
		return 1.00
	else:
		return 10.00	# magic number walking down the street

def levenshtein(s1, s2):
	if len(s1) < len(s2):
		return levenshtein(s2, s1)

	if len(s2) == 0:
		return len(s1)

	pre = range(len(s2) + 1)
	for i, c1 in enumerate(s1):
		cur = [i + 1]
		for j, c2 in enumerate(s2):
			cur.append(min(pre[j + 1] + 1, cur[j] + 1, pre[j] + (c1 != c2)))	# insert, delete, substitute
		pre = cur

	return pre[-1]

def print_output(country, output, list1, list2):
	if not os.path.exists(os.path.dirname(output)):
		os.makedirs(os.path.dirname(output))
	f = open(output, 'wb')
	list1.update(list2)
	for key, row in list1.iteritems():
		f.write(country + '\t' + key)
		for item in row:
			f.write( ('\t%.2f-' + item[0]) % item[1] )
		f.write('\n')
	f.close()

def main(algo, home, size, country):
	sku_src = set(line.strip() for line in open(home + '/Data/instock_skus_' + country + '.csv'))
	sku_dst = set(line.strip() for line in open(home + '/Data/valid_skus_' + country + '.csv'))
	sku_male = set(line.strip() for line in open(home + '/Data/sku_male_' + country + '.csv'))
	sku_female = set(line.strip() for line in open(home + '/Data/sku_female_' + country + '.csv'))

	purchase_map = file_to_map(open(home + '/Data/VTD_purchased_' + country + '.csv'))
	view_map = file_to_map(open(home + '/Data/VTD_view_' + country + '.csv'))
	cart_map = file_to_map(open(home + '/Data/VTD_cart_' + country + '.csv'))

	sku_dst_male = sku_male.intersection(sku_dst)
	sku_dst_female = sku_female.intersection(sku_dst)
	sku_src_male = sku_male.intersection(sku_src)
	sku_src_female = sku_female.intersection(sku_src)

	tmp_algo = Algorithms.ORIG

	if (options.algo == 'vtd'):
		tmp_algo = Algorithms.VTD
	elif (options.algo == 'bayes'):
		tmp_algo = Algorithms.BYS
	elif (options.algo == 'visenze'):
		tmp_algo = Algorithms.VSZ

	list_recommended_male = apply_jaccard(tmp_algo, size, sku_src_male, sku_dst_male, purchase_map, view_map, cart_map)
	list_recommended_female = apply_jaccard(tmp_algo, size, sku_src_female, sku_dst_female, purchase_map, view_map, cart_map)

	print_output(country, home + '/Result/' + algo + '/Raptor_' + country + '.csv', list_recommended_male, list_recommended_female)

if __name__ == "__main__":

	optparser = OptionParser()
	optparser.add_option('-p', '--homePath',
						dest='home',
						help='path to home folder',
						default='./Data/Test')
	optparser.add_option('-s', '--size',
						dest='size',
						help='specify number of relevant products, default = 3',
						default=3)
	optparser.add_option('-a', '--algorithm',
						dest='algo',
						help='algorithm being used, default = ORIG',
						default='original')
	optparser.add_option('-c', '--country',
						dest='country',
						help='country code, default = sg',
						default='sg')

	(options, args) = optparser.parse_args()

	print "Run PyRaptor with option: (" + options.algo, options.home, options.size, options.country + ")"

	main(options.algo, options.home, int(options.size), options.country)