#!/usr/bin/env
# -*- coding: utf-8 -*-
"""
Run unit tests

See:
	http://pyunit.sourceforge.net/pyunit.html
"""
import unittest
import os
from gimpFormats import *
from smartimage.imgTools import *


__HERE__=os.path.abspath(__file__).rsplit(os.sep,1)[0]+os.sep
class Test(unittest.TestCase):
	"""
	Run unit test
	"""

	def setUp(self):
		self.dut=GimpDocument()
		
	def tearDown(self):
		pass
		
	def testImage(self):
		self.dut.load(__HERE__+'one_layer_with_transparency.xcf')
		self.dut.save(__HERE__+'actualOutput.png')
		same=compareImage(self.dut.layers[0].image,__HERE__+'desiredOutput.png')
		assert same

		
def testSuite():
	"""
	Combine unit tests into an entire suite
	"""
	testSuite = unittest.TestSuite()
	testSuite.addTest(Test("testImage"))
	return testSuite
		
		
if __name__ == '__main__':
	"""
	Run all the test suites in the standard way.
	"""
	unittest.main()