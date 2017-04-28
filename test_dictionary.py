
from canarydictionary import canarydictionary

def test_dictionary():
	dictionary = canarydictionary()
	millo = dictionary['millo']
	assert millo == 'maiz'
	papa = dictionary['papa']
	assert papa == 'patata'
	baifo = dictionary['baifo']
	assert baifo == 'cabra'

def test_nodictionary():
	dictionary = canarydictionary()
	noword = dictionary['noword']
	assert noword == None