from bs4 import BeautifulSoup
import requests

import re

class Translate:
	def _init__(self):
		pass

	def entoja(self, tweets_list, source='en', target='ja'):

		translate_list = []

		for tweet in tweets_list:
			tweet = re.sub(r'[\\|/|:|?|.|"|<|>|\|]', ' ', tweet)
			tweet = tweet.replace(' ', '')
			tweet = tweet.replace('"', '')
			tweet = tweet.replace('\n', '\\n')
			tweet = tweet.replace('#', '')
			url = 'https://script.google.com/macros/s/AKfycbweJFfBqKUs5gGNnkV2xwTZtZPptI6ebEhcCU2_JvOmHwM2TCk/exec?text={}&source={}&target={}'.format(tweet, target, source)
			print(url)
			response = requests.get(url)
			response.encoding = response.apparent_encoding

			new_tweet = re.sub(r'[\\|/|:|?|.|"|<|>|\|]', ' ', response.text)
			new_tweet = new_tweet.replace(' ', '')
			new_tweet = new_tweet.replace('"', '')
			new_tweet = new_tweet.replace('\n', '\\n')
			new_tweet = new_tweet.replace('#', '')
			url = 'https://script.google.com/macros/s/AKfycbweJFfBqKUs5gGNnkV2xwTZtZPptI6ebEhcCU2_JvOmHwM2TCk/exec?text={}&source={}&target={}'.format(new_tweet, source, target)
			print(url)
			response = requests.get(url)
			response.encoding = response.apparent_encoding
			translate_list.append(response.text)

		return translate_list

		removed_list = []

		# for tweet in tweets_list:
		# 	tweet = tweet.replace('"', '')
		# 	tweet = '"' + tweet + '"'
		# 	while re.search(r'http[a-zA-Z:./0-9]*', tweet) is not None:
		# 		an = re.search(r'http[a-zA-Z:./0-9]*', tweet)
		# 		start = an.span()[0]
		# 		end = an.span()[1]
		# 		tweet = str(tweet[:start]) + '"' + str(tweet[start:end]) +  + str(tweet[end:])
		# 	removed_list.append(tweet)