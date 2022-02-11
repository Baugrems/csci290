import unittest
from checkerboard import handleBoard

#unittest didn't get used live in Kattis. These are just running the values as a test, but not using the official unittest library..

# rows = ["WBBW", "WBWB", "BWWB", "BWBW"]
# rows2 = ["BWWB", "BWBB", "WBBW", "WBWW"]
# rows3 = ["BWBWWB", "WBWBWB", "WBBWBW", "BBWBWW", "BWWBBW", "WWBWBB"]
# rows4 = ["WWBBWB", "BBWWBW", "WBWBWB", "BWBWBW", "BWBBWW", "WBWWBB"]
# handleBoard(rows)
# handleBoard(rows2)
# handleBoard(rows3)
# handleBoard(rows4)

class CheckersTest(unittest.TestCase): # this is basically just a copy of the example for fizzbuzz, but applied to my checkerboard solve
	def run_cases(self, cases):
		for case in cases:
			actual = handleBoard(case[0])
			self.assertEqual(actual, case[1], "Expected " + str(case[1]) + " but got " + str(actual))
	
	def test_boards(self): # kattis examples
		cases = [
			(["WBBW", "WBWB", "BWWB", "BWBW"], 1), # I want a board... and then a result so... not much here
			(["BWWB", "BWBB", "WBBW", "WBWW"], 0),
            (["BWBWWB", "WBWBWB", "WBBWBW", "BBWBWW", "BWWBBW", "WWBWBB"], 0),
            (["WWBBWB", "BBWWBW", "WBWBWB", "BWBWBW", "BWBBWW", "WBWWBB"], 1),
		]
		self.run_cases(cases)

if __name__ == '__main__':
    unittest.main()