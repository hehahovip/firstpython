import unittest
import sys
sys.path.append('readfiledata.py')
import readfiledata

class ReadFileDataTest(unittest.TestCase):
	def setUp(self):
		datadict = readfiledata.load_file()
		self.datadict = datadict

	def test_find_it1(self):
		datadict = readfiledata.load_file()
		target = readfiledata.find_it('5mi', '20:45', self.datadict)
		self.assertEqual('84.8', target)

	def test_find_it2(self):
		datadict = readfiledata.load_file()
		target = readfiledata.find_it('5mi', '20:45', self.datadict)
		self.assertNotEqual('84.1', target)

	def test_find_it3(self):
		datadict = readfiledata.load_file()
		target = readfiledata.find_it('5mi', '1:04:26', self.datadict)
		self.assertEqual('28.5', target)

	def test_find_it4(self):
		datadict = readfiledata.load_file()
		target = readfiledata.find_it('5mi', '1:03:20', self.datadict)
		self.assertEqual('28.5', target)

	def test_find_it5(self):
		datadict = readfiledata.load_file()
		target = readfiledata.find_it('5mi', '1:02:05', self.datadict)
		self.assertEqual('29.1', target)

if __name__ == '__main__':
    unittest.main()