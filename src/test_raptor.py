import raptor
import unittest

class JacardTest(unittest.TestCase):
	"""This test case (JacardTest) is used to test apply_jaccard function, obviously"""

	
	def testNoValid(self):
		algo = raptor.Algorithms.ORIG
		size = 3

		sku_src = {'sku0', 'sku1', 'sku2', 'sku3', 'sku4', 'sku5', 'sku6', 'sku7', 'sku8', 'sku9'}
		sku_dst = {}

		purchase_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
						'sku2': set(['cust2']), 'sku3': set(['cust1', 'cust2']),
						'sku4': set(['cust4', 'cust5', 'cust3']), 'sku5': set(['cust1']),
						'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
						'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		view_map = {'sku0': set(['cust1', 'cust2', 'cust3', 'cust4']), 'sku1': set(['cust1', 'cust2', 'cust3', 'cust4', 'cust5']),
					'sku2': set(['cust2', 'cust4', 'cust5']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1', 'cust2', 'cust3']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4', 'cust5']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2', 'cust4'])}

		cart_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
					'sku2': set(['cust2', 'cust4']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		res = raptor.apply_jaccard(algo, size, sku_src, sku_dst, purchase_map, view_map, cart_map)

		self.assertEqual(len(res), 10)

		for item in res.values():
			self.assertLessEqual(len(item), 0)

	def testNormalOrig1(self):
		algo = raptor.Algorithms.ORIG
		size = 3

		sku_src = {'sku0', 'sku1', 'sku2', 'sku3', 'sku4'}
		sku_dst = {'sku1', 'sku2', 'sku3', 'sku4'}

		purchase_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
						'sku2': set(['cust2']), 'sku3': set(['cust1', 'cust2']),
						'sku4': set(['cust4', 'cust5', 'cust3']), 'sku5': set(['cust1']),
						'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
						'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		view_map = {'sku0': set(['cust1', 'cust2', 'cust3', 'cust4']), 'sku1': set(['cust1', 'cust2', 'cust3', 'cust4', 'cust5']),
					'sku2': set(['cust2', 'cust4', 'cust5']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1', 'cust2', 'cust3']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4', 'cust5']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2', 'cust4'])}

		cart_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
					'sku2': set(['cust2', 'cust4']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		res = raptor.apply_jaccard(algo, size, sku_src, sku_dst, purchase_map, view_map, cart_map)

		self.assertEqual(len(res), 5)

		for item in res.values():
			self.assertLessEqual(len(item), size)

		self.assertIn('sku1', res)
		t = dict(res['sku1'])
		self.assertIn('sku3', t)
		self.assertAlmostEqual(t['sku3'], 20.77, 2)

		self.assertIn('sku3', res)
		t = dict(res['sku3'])
		self.assertIn('sku2', t)
		self.assertAlmostEqual(t['sku2'], 9.45, 2)

		self.assertIn('sku4', res)
		t = dict(res['sku4'])
		self.assertIn('sku1', t)
		self.assertAlmostEqual(t['sku1'], 3.62, 2)

	def testNormalOrig2(self):
		algo = raptor.Algorithms.ORIG
		size = 3

		sku_src = {'sku5', 'sku6', 'sku7', 'sku8', 'sku9'}
		sku_dst = {'sku5', 'sku6', 'sku7', 'sku8'}

		purchase_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
						'sku2': set(['cust2']), 'sku3': set(['cust1', 'cust2']),
						'sku4': set(['cust4', 'cust5', 'cust3']), 'sku5': set(['cust1']),
						'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
						'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		view_map = {'sku0': set(['cust1', 'cust2', 'cust3', 'cust4']), 'sku1': set(['cust1', 'cust2', 'cust3', 'cust4', 'cust5']),
					'sku2': set(['cust2', 'cust4', 'cust5']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1', 'cust2', 'cust3']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4', 'cust5']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2', 'cust4'])}

		cart_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
					'sku2': set(['cust2', 'cust4']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		res = raptor.apply_jaccard(algo, size, sku_src, sku_dst, purchase_map, view_map, cart_map)

		self.assertEqual(len(res), 5)

		for item in res.values():
			self.assertLessEqual(len(item), size)

		self.assertIn('sku6', res)
		self.assertEqual(len(res['sku6']), 0)

		self.assertIn('sku9', res)
		self.assertEqual(len(res['sku9']), 0)

		self.assertIn('sku5', res)
		t = dict(res['sku5'])
		self.assertIn('sku8', t);
		self.assertAlmostEqual(t['sku8'], 9.45, 2)

		self.assertIn('sku7', res)
		t = dict(res['sku7'])
		self.assertIn('sku8', t);
		self.assertAlmostEqual(t['sku8'], 9.45, 2)

		self.assertIn('sku8', res)
		t = dict(res['sku8'])
		self.assertIn('sku7', t);
		self.assertAlmostEqual(t['sku7'], 9.45, 2)

	def testNormalBayes(self):
		algo = raptor.Algorithms.BYS
		size = 3

		sku_src = {'sku0', 'sku1', 'sku2', 'sku3', 'sku4'}
		sku_dst = {'sku1', 'sku2', 'sku3', 'sku4'}

		purchase_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
						'sku2': set(['cust2']), 'sku3': set(['cust1', 'cust2']),
						'sku4': set(['cust4', 'cust5', 'cust3']), 'sku5': set(['cust1']),
						'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
						'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		view_map = {'sku0': set(['cust1', 'cust2', 'cust3', 'cust4']), 'sku1': set(['cust1', 'cust2', 'cust3', 'cust4', 'cust5']),
					'sku2': set(['cust2', 'cust4', 'cust5']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1', 'cust2', 'cust3']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4', 'cust5']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2', 'cust4'])}

		cart_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
					'sku2': set(['cust2', 'cust4']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		res = raptor.apply_jaccard(algo, size, sku_src, sku_dst, purchase_map, view_map, cart_map)

		self.assertEqual(len(res), 5)

		for item in res.values():
			self.assertLessEqual(len(item), size)

		self.assertIn('sku1', res)
		t = dict(res['sku1'])
		self.assertIn('sku2', t);
		self.assertAlmostEqual(t['sku2'], 9.45, 2)

		self.assertIn('sku3', res)
		t = dict(res['sku3'])
		self.assertIn('sku1', t);
		self.assertAlmostEqual(t['sku1'], 15.00, 2)

		self.assertIn('sku4', res)
		t = dict(res['sku4'])
		self.assertIn('sku1', t);
		self.assertAlmostEqual(t['sku1'], 3.62, 2)

	def testNormalVTD(self):
		algo = raptor.Algorithms.VTD
		size = 3

		sku_src = {'sku0', 'sku1', 'sku2', 'sku3', 'sku4'}
		sku_dst = {'sku1', 'sku2', 'sku3', 'sku4'}

		purchase_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
						'sku2': set(['cust2']), 'sku3': set(['cust1', 'cust2']),
						'sku4': set(['cust4', 'cust5', 'cust3']), 'sku5': set(['cust1']),
						'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
						'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		view_map = {'sku0': set(['cust1', 'cust2', 'cust3', 'cust4']), 'sku1': set(['cust1', 'cust2', 'cust3', 'cust4', 'cust5']),
					'sku2': set(['cust2', 'cust4', 'cust5']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1', 'cust2', 'cust3']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4', 'cust5']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2', 'cust4'])}

		cart_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
					'sku2': set(['cust2', 'cust4']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		res = raptor.apply_jaccard(algo, size, sku_src, sku_dst, purchase_map, view_map, cart_map)

		self.assertEqual(len(res), 5)

		for item in res.values():
			self.assertLessEqual(len(item), size)

		self.assertIn('sku1', res)
		t = dict(res['sku1'])
		self.assertIn('sku4', t);
		self.assertAlmostEqual(t['sku4'], 1.25, 2)

		self.assertIn('sku3', res)
		t = dict(res['sku3'])
		self.assertIn('sku1', t);
		self.assertAlmostEqual(t['sku1'], 2.49, 2)

		self.assertIn('sku4', res)
		t = dict(res['sku4'])
		self.assertIn('sku3', t);
		self.assertAlmostEqual(t['sku3'], 0.36, 2)

	def testSize0(self):
		algo = raptor.Algorithms.ORIG
		size = 0

		sku_src = {'sku0', 'sku1', 'sku2', 'sku3', 'sku4', 'sku5', 'sku6', 'sku7', 'sku8', 'sku9'}
		sku_dst = {'sku1', 'sku2', 'sku3', 'sku4', 'sku5', 'sku6', 'sku7', 'sku8'}

		purchase_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
						'sku2': set(['cust2']), 'sku3': set(['cust1', 'cust2']),
						'sku4': set(['cust4', 'cust5', 'cust3']), 'sku5': set(['cust1']),
						'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
						'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		view_map = {'sku0': set(['cust1', 'cust2', 'cust3', 'cust4']), 'sku1': set(['cust1', 'cust2', 'cust3', 'cust4', 'cust5']),
					'sku2': set(['cust2', 'cust4', 'cust5']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1', 'cust2', 'cust3']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4', 'cust5']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2', 'cust4'])}

		cart_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
					'sku2': set(['cust2', 'cust4']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		res = raptor.apply_jaccard(algo, size, sku_src, sku_dst, purchase_map, view_map, cart_map)

		self.assertEqual(len(res), 0)

	def testSizeNeg(self):
		algo = raptor.Algorithms.ORIG
		size = -3

		sku_src = {'sku0', 'sku1', 'sku2', 'sku3', 'sku4', 'sku5', 'sku6', 'sku7', 'sku8', 'sku9'}
		sku_dst = {'sku1', 'sku2', 'sku3', 'sku4', 'sku5', 'sku6', 'sku7', 'sku8'}

		purchase_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
						'sku2': set(['cust2']), 'sku3': set(['cust1', 'cust2']),
						'sku4': set(['cust4', 'cust5', 'cust3']), 'sku5': set(['cust1']),
						'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
						'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		view_map = {'sku0': set(['cust1', 'cust2', 'cust3', 'cust4']), 'sku1': set(['cust1', 'cust2', 'cust3', 'cust4', 'cust5']),
					'sku2': set(['cust2', 'cust4', 'cust5']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1', 'cust2', 'cust3']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4', 'cust5']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2', 'cust4'])}

		cart_map = {'sku0': set(['cust1', 'cust2']), 'sku1': set(['cust1', 'cust2', 'cust3']),
					'sku2': set(['cust2', 'cust4']), 'sku3': set(['cust1', 'cust2']),
					'sku4': set(['cust4', 'cust5', 'cust1', 'cust3']), 'sku5': set(['cust1']),
					'sku6': set(['cust5', 'cust3']), 'sku7': set(['cust4']),
					'sku8': set(['cust1', 'cust4']), 'sku9': set(['cust2'])}

		res = raptor.apply_jaccard(algo, size, sku_src, sku_dst, purchase_map, view_map, cart_map)

		self.assertEqual(len(res), 0)

	def testBrandNew(self):
		algo = raptor.Algorithms.ORIG
		size = 3
		sku_src = {'sku0', 'sku1', 'sku2', 'sku3', 'sku4', 'sku5', 'sku6', 'sku7', 'sku8', 'sku9'}
		sku_dst = {'sku1', 'sku2', 'sku3', 'sku4', 'sku5', 'sku6', 'sku7', 'sku8'}
		purchase_map = {}
		view_map = {}
		cart_map = {}
		res = raptor.apply_jaccard(algo, size, sku_src, sku_dst, purchase_map, view_map, cart_map)

		self.assertEqual(len(res), 10)
		
		for item in res.values():
			self.assertLessEqual(len(item), 0)

	def testNull(self):
		algo = raptor.Algorithms.ORIG
		size = 3
		sku_src = {}
		sku_dst = {}
		purchase_map = {}
		view_map = {}
		cart_map = {}
		res = raptor.apply_jaccard(algo, size, sku_src, sku_dst, purchase_map, view_map, cart_map)

		self.assertEqual(len(res), 0)

class LevenshteinTest(unittest.TestCase):
	"""This test case (LevenshteinTest) is used to test levenshtein function, obviously"""
	def testNormal(self):
		self.assertEqual(raptor.levenshtein('a', 'b'), 1)
		self.assertEqual(raptor.levenshtein('kitten', 'sitten'), 1)		# very famous example
		self.assertEqual(raptor.levenshtein('sitten', 'sittin'), 1)		# very famous example
		self.assertEqual(raptor.levenshtein('sitten', 'sitting'), 2)	# very famous example

	# test with empty string input
	def testEmpty(self):
		self.assertEqual(raptor.levenshtein('a', ''), 1)
		self.assertEqual(raptor.levenshtein('', 'sitten'), 6)
		self.assertEqual(raptor.levenshtein('sitten', ''), 6)
		self.assertEqual(raptor.levenshtein('', ''), 0)

	# test two string identifically equal
	def testEqual(self):
		self.assertEqual(raptor.levenshtein('abcxyz', 'abcxyz'), 0)

class WilsonTest(unittest.TestCase):
	"""This test case (WilsonTest) is used to test wilson score function, obviously"""
	def testNormal(self):
		self.assertAlmostEqual(raptor.wilson95(1, 3), 6.149031527616, 4)
		self.assertAlmostEqual(raptor.wilson95(2, 6), 9.676933255922, 4)
		self.assertAlmostEqual(raptor.wilson95(2, 7), 8.221716570902, 4)
		self.assertAlmostEqual(raptor.wilson95(100, 300), 28.239256, 4)
		self.assertAlmostEqual(raptor.wilson95(20, 40), 35.19928, 4)

	# test with zero input
	def test0(self):
		self.assertAlmostEqual(raptor.wilson95(1, 1), 20.654329147389294, 4)
		self.assertAlmostEqual(raptor.wilson95(2, 2), 34.23719528896193, 4)
		self.assertAlmostEqual(raptor.wilson95(0, 1), 0, 4)
		self.assertAlmostEqual(raptor.wilson95(0, 0), 0, 4)		# invalid input

	# test with negative (invalid) input
	def testNeg(self):
		self.assertAlmostEqual(raptor.wilson95(-1, -2), 0, 4) 	# invalid input
		self.assertAlmostEqual(raptor.wilson95(-1, 2), 0, 4) 	# invalid input


if __name__ == '__main__':
	unittest.main()