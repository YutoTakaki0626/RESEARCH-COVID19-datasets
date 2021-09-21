import os 

import pandas as pd

from lists_file import dumpJoblib, loadJoblib

class MakeTweet:
	def __init__(self):
		self.texts_data = []
		self.real_data = {}
		self.unique_data = {}

	def make_all_tweets_list(self):
		texts_file = sorted(os.listdir('texts_data'))

		for file_name in texts_file:
			text_data = loadJoblib('texts_data/' + file_name)
			self.texts_data += text_data

		dumpJoblib('all_textdata.joblib', self.texts_data)

		return None

	def make_real_unique_tweets_list(self):
		self.texts_data = loadJoblib('all_textdata.joblib')

		for idx, tweet in enumerate(self.texts_data):
		    if tweet is not None:
		        self.real_data[idx]=tweet

		for idx, tweet in self.real_data.items():
			if tweet not in self.unique_data.values():
				self.unique_data[idx] = tweet

		dumpJoblib('real_textdata.joblib', self.real_data)
		dumpJoblib('unique_textdata.joblib', self.unique_data)

		return None


class GetTweet:
	def __init__(self):
		self.texts_data = loadJoblib('all_textdata.joblib')
		self.real_data = loadJoblib('real_textdata.joblib')
		self.unique_data = loadJoblib('unique_textdata.joblib')

		self.tweet_id_list = None
		self.assessment_list = None

	def get_all_tweets_list(self):
		df = pd.read_csv('covid19.csv')
		self.tweet_id_list = list(df['tweet_id'])
		self.assessment_list = list(df['assessment_option_id']) 

		print(f'全データの件数:{len(self.texts_data)}')
		print(f'現存するデータの数：{len(self.real_data)}')
		print(f'重複を取り除いた件数：{len(self.unique_data)}')

		print('-' * 40)

		print('63: 　　　　一般事実　 {}個'.format(self.assessment_list.count(63)))
		print('64: 　　　　個人事実 　{}個'.format(self.assessment_list.count(64)))
		print('65: 　　　意見・感想 　{}個'.format(self.assessment_list.count(65)))
		print('66: 　　　　判定困難 　{}個'.format(self.assessment_list.count(66)))
		print('67: 　　　　関係なし 　{}個'.format(self.assessment_list.count(67)))
		print('68: 事実だが判定困難 　{}個'.format(self.assessment_list.count(68)))

		return (self.tweet_id_list, self.assessment_list)


if '__name__' == '__main__':
	pass

