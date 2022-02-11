import unittest
from nineknights import handleKnights

# this isn't really using unittest but its what I used live in Kattis when I wasn't sure how to unit test better...
# board1 = ["...k.","...k.","k.k.k", ".k.k.", "k.k.k"]
# board2 = [".....","...k.","k.k.k", ".k.k.", "k.k.k"]
# board3 = [".....","...k.","k.k.k", ".k.k.", "k...k"]
# handleKnights(board1)
# handleKnights(board2)
# handleKnights(board3)

class NineKnightsTest(unittest.TestCase): # this is basically just a copy of the example for fizzbuzz, but applied to my nine knights solve
	def run_cases(self, cases):
		for case in cases:
			actual = handleKnights(case[0])
			self.assertEqual(actual, case[1], "Expected " + case[1] + " but got " + actual)
	
	def test_knights(self): # kattis examples
		cases = [
			(["...k.","...k.","k.k.k", ".k.k.", "k.k.k"], "invalid"), # I want a board... and then a result so... not much here
			([".....","...k.","k.k.k", ".k.k.", "k.k.k"], "valid"),
            ([".....","...k.","k.k.k", ".k.k.", "k...k"], "invalid"),
		]
		self.run_cases(cases)

if __name__ == '__main__':
    unittest.main()