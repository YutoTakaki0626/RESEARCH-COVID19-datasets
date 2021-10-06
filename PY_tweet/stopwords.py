from bs4 import BeautifulSoup
import requests 

from PY_tweet.lists_file import *


def make_stop_words():
	slothlib_path = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
	response = requests.get(slothlib_path)
	response.encoding = response.apparent_encoding
	text = str(response.text)
	stopword_list = text.split('\r\n')
	stopword_list = list(filter(None, stopword_list))
	dumpJoblib('DATA_labels/stopword_list.joblib', stopword_list)

	return stopword_list