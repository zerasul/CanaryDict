
from canarydictionary import canarydictionary

def test_dictionary():
	dictionary = canarydictionary()
	millo = dictionary.searchword('millo')
	assert millo == 'maiz'
	papa = dictionary.searchword('papa')
	assert papa == 'patata'
	baifo = dictionary.searchword('baifo')
	assert baifo == 'cabra'
	godo = dictionary.searchword('godo')
	assert godo == 'miguel'

def test_nodictionary():
	dictionary = canarydictionary()
	noword = dictionary.searchword('noword')
	assert noword == None