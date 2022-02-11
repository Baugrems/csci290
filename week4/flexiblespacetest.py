import unittest

from flexiblespaces import handlePartitions

class FlexibleSpaceTest(unittest.TestCase): # this is basically just a copy of the example for fizzbuzz, but applied to my flexible spaces solve
	def run_cases(self, cases):
		for case in cases:
			actual = handlePartitions(case[0], case[1])
			self.assertEqual(actual, case[2], "Expected " + case[2] + " but got " + actual)
	
	def test_flexspace(self): # kattis only gives two examples so I put them both here
		cases = [
			([1,4,8], 10, "1 2 3 4 6 7 8 9 10"), # I want partition, width, and expected
			([2,5], 6, "1 2 3 4 5 6"),
		]
		self.run_cases(cases)

if __name__ == '__main__':
    unittest.main()