import csv
import random
import string
import os

def file_to_map(filecontent):
	rows = list(filecontent)
	res = {}
	for row in rows:
		parse_data = string.split(row)
		res[parse_data[0]] = parse_data[1:]
	return res

def to_list_file(l, output):
	if not os.path.exists(os.path.dirname(output)):
		os.makedirs(os.path.dirname(output))
	f = open(output, 'wb')

	for row in l:
		f.write(row)
		f.write('\n')
	f.close()

def to_map_file(m, output):
	if not os.path.exists(os.path.dirname(output)):
		os.makedirs(os.path.dirname(output))
	f = open(output, 'wb')

	for key, row in m.iteritems():
		f.write(key + '\t')
		f.write(row[0])
		for i in range(1, len(row)):
			f.write(' ' + row[i])
		f.write('\n')
	f.close()

def process(sample_size, sku_src, sku_dst, sku_male, sku_female, purchase_map, view_map, cart_map):
	sku_src_s = random.sample(sku_src, sample_size)

	sku_dst_s = sku_dst.intersection(sku_src_s)
	sku_male_s = sku_male.intersection(sku_src_s)
	sku_female_s = sku_female.intersection(sku_src_s)
	purchase_map_s = {k:v for (k,v) in purchase_map.iteritems() if k in sku_src_s}
	view_map_s = {k:v for (k,v) in view_map.iteritems() if k in sku_src_s}
	cart_map_s = {k:v for (k,v) in cart_map.iteritems() if k in sku_src_s}

	to_list_file(sku_src_s, "../lab/%i/Data/instock_skus_sg.csv" % sample_size)
	to_list_file(sku_dst_s, "../lab/%i/Data/valid_skus_sg.csv" % sample_size)
	to_list_file(sku_male_s, "../lab/%i/Data/sku_male_sg.csv" % sample_size)
	to_list_file(sku_female_s, "../lab/%i/Data/sku_female_sg.csv" % sample_size)
	to_map_file(purchase_map_s, "../lab/%i/Data/VTD_purchased_sg.csv" % sample_size)
	to_map_file(view_map_s, "../lab/%i/Data/VTD_view_sg.csv" % sample_size)
	to_map_file(cart_map_s, "../lab/%i/Data/VTD_cart_sg.csv" % sample_size)


def main():
	sku_src = set(line.strip() for line in open('../lab/instock_skus_sg.csv'))
	sku_dst = set(line.strip() for line in open('../lab/valid_skus_sg.csv'))
	sku_male = set(string.split(line)[0] for line in open('../lab/sku_male_sg.csv'))
	sku_female = set(string.split(line)[0] for line in open('../lab/sku_female_sg.csv'))

	purchase_map = file_to_map(open('../lab/VTD_purchased_sg.csv'))
	view_map = file_to_map(open('../lab/VTD_view_sg.csv'))
	cart_map = file_to_map(open('../lab/VTD_cart_sg.csv'))

	for sample_size in [10, 50, 100, 500, 1000, 5000, 10000]:
		process(sample_size, sku_src, sku_dst, sku_male, sku_female, purchase_map, view_map, cart_map)

if __name__ == "__main__":
	main()