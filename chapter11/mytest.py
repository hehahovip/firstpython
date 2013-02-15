import sys
sys.path.append('readfiledata.py')
import readfiledata

datadict = readfiledata.load_file()
print(readfiledata.find_it('5mi', '20:45', datadict))