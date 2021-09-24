import re
import string
import emoji

from PY_preprocessing.emoji_list import get_all_emoji

class Remove:
	def __init__(self):
		self.all_emojis = get_all_emoji()

	def new_line_marks(self, tweets_list):
		'''
		the process of removing new line marks ('\n')
		'''
		new_list = []

		for st in tweets_list:
			while re.search(r'\n', st):
				an = re.search(r'\n', st)
				start = an.span()[0]
				end = an.span()[1]
				st = str(st[:start]) + str(st[end:])
			new_list.append(st)
			
		return new_list

	def all_blanks(self, tweets_list):
		'''
		the process of removing all blanks
		'''
		new_list = []

		for st in tweets_list:
			while re.search(r'\u3000', st):
				an = re.search(r'\u3000', st)
				start = an.span()[0]
				end = an.span()[1]
				st = str(st[:start]) + str(st[end:])
			new_list.append(st)
			
		return new_list

	def usermention(self, tweets_list):
		'''
		the process of removing USER MENTION ('@XXXX')
		'''
		removed_list = []

		for tweet in tweets_list:
			while re.search(r'@[0-9a-zA-Z_]{4,14}', tweet) is not None:
				an = re.search(r'@[0-9a-zA-Z_]{4,14}', tweet)
				start = an.span()[0]
				end = an.span()[1]
				tweet = str(tweet[:start]) + str(tweet[end:])
			removed_list.append(tweet)

		return removed_list


	def url(self, tweets_list):
		'''
		the process of removing URL ('httpXXXX')
		'''
		removed_list = []

		for tweet in tweets_list:
			while re.search(r'http[a-zA-Z:./0-9]*', tweet) is not None:
				an = re.search(r'http[a-zA-Z:./0-9]*', tweet)
				start = an.span()[0]
				end = an.span()[1]
				tweet = str(tweet[:start]) + str(tweet[end:])
			removed_list.append(tweet)

		return removed_list


	def hashtag(self, tweets_list):
		'''
		the process of removing only hashtag
		example) #happy -> happy
		'''
		removed_list = []
		removed_cnt = 0

		for tweet in tweets_list:
			if re.search(r'#', tweet) is not None:
				removed_cnt += 1
			while re.search(r'#', tweet) is not None:
				an = re.search(r'#', tweet)
				start = an.span()[0]
				end = an.span()[1]
				tweet = str(tweet[:start]) + str(tweet[end:])
			removed_list.append(tweet)
		return removed_list

	def hashtag_a_series_of_words(self, tweets_list):
		'''
		the process of removing a series of hashtag
		example) '#happy' -> ''
		'''

		removed_list = []

		for tweet in tweets_list:
			while re.search(r'#[0-9a-zA-Z_]+\s', tweet) is not None:
				an = re.search(r'#[0-9a-zA-Z_]+\s', tweet)
				start = an.span()[0]
				end = an.span()[1]
				tweet = str(tweet[:start]) + str(tweet[end:])
			removed_list.append(tweet)

		return removed_list

	def emojis(self, tweets_list):
		'''
		the process of removing emoji
		'''
		removed_list = []

		for tweet in tweets_list:
			tmp = []
			for idx, string in enumerate(tweet):
				if string in self.all_emojis:
					tmp.append(idx)
			new_tweet = ''
			tmp_in = 0
			for i in tmp:
				new_tweet = str(new_tweet) + str(tweet[tmp_in:i])
				tmp_in = i+1
			new_tweet = str(new_tweet) + str(tweet[tmp_in:])
			removed_list.append(new_tweet)

		return removed_list

	def covid19(self, tweets_list):
		'''
		count the number of of tweets contained conid-19 ('httpXXX')
		'''
		
		removed_list = []

		for tweet in tweets_list:



			while re.search(r'covid19|covid-19|covid', tweet.lower()) is not None:
				a = re.search(r'covid19|covid-19|covid', tweet.lower())
				start = a.span()[0]
				end = a.span()[1]
				tweet = str(tweet[:start]) + 'コロナ' + str(tweet[end:])

			while re.search(r'corona', tweet.lower()) is not None:
				b = re.search(r'corona', tweet.lower())
				start = b.span()[0]
				end = b.span()[1]
				tweet = str(tweet[:start]) + 'コロナ' + str(tweet[end:])

			while re.search(r'who', tweet.lower()) is not None:
				c = re.search(r'who', tweet.lower())
				start = c.span()[0]
				end = c.span()[1]
				tweet = str(tweet[:start]) + '世界保健機関' + str(tweet[end:])

			while re.search(r'pcr', tweet.lower()) is not None:
				d = re.search(r'pcr', tweet.lower())
				start = d.span()[0]
				end = d.span()[1]
				if tweet[end:end+2] != '検査':
					tweet = str(tweet[:start]) + '検査' + str(tweet[end:])
				else:
					tweet = str(tweet[:start]) + str(tweet[end:])

			while re.search(r'virus', tweet.lower()) is not None: 
				e = re.search(r'virus', tweet.lower())
				start = e.span()[0]
				end = e.span()[1]
				tweet = str(tweet[:start]) + 'ウイルス' + str(tweet[end:])

			removed_list.append(tweet)

		return removed_list

	def www(self, tweets_list):
		'''
		count the number of of tweets contained 'w' 
		It uses when laughing in Japan

		'''

		
		not_w_list = list(string.ascii_lowercase)
		not_w_list.remove('w')

		removed_list = []
		new_removed_list = []
		
		for tweet in tweets_list:
			text = []
			contexts = tweet.strip()
			for context in contexts:
				if len(context) != 1:
					if context[-1]=='w' and context[-2] not in not_w_list:
						text.append(context[:-1] + '笑')
					else:
						text.append(context)
				else:
					text.append(context)
			text = ''.join(text)
			removed_list.append(text)

		for tweet in removed_list:
			while re.search(r'[^abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ:./0-9]ww+', tweet) is not None: 
			    e = re.search(r'[^abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ:./0-9]ww+', tweet)
			    start = e.span()[0]
			    end = e.span()[1]
			    tweet = str(tweet[:start]) + ('笑' * (end-start)) + str(tweet[end:])
			new_removed_list.append(tweet)


		return new_removed_list


if '__name__' == '__main__':
	pass




