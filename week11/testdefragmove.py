import unittest
from defragmove import defragMove

class defragMoveTest(unittest.TestCase):
	def run_cases(self, cases):
		for case in cases:
			actual = defragMove(case[0], "TD") # TD as in "Test Datacenter"
			self.assertEqual(actual, case[1], actual)
	
	def test_defrag_cases(self): # test case setup
		cases = [
            (
                ["001FF4", "000A14", "001054"],
                ["T0100D", "T0000D", "T0101D"]
             ), # example testcase
            (
                ["000FF0", "001FF0", "002FF0", "00CFF0", "00cEF0"],
                ["T0000D", "T0100D", "T0200D", "T0C00D", "T0C01D"]
             ) # testing various k values
		]
		self.run_cases(cases)

if __name__ == '__main__':
    unittest.main()