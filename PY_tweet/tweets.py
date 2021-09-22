import os 

import pandas as pd

from PY_tweet.lists_file import dumpJoblib, loadJoblib

class MakeTweet:
	def __init__(self):
		self.texts_data = [] 
		self.real_data = {}
		self.unique_data = {}

	def make_all(self):
		self.make_all_tweets_list()
		self.make_real_unique_tweets_list()
		self.ignore_few_data()

	def make_all_tweets_list(self):
		texts_file = sorted(os.listdir('DATA_a_part_of_texts'))

		for file_name in texts_file:
			text_data = loadJoblib('DATA_a_part_of_texts/' + file_name)
			self.texts_data += text_data

		dumpJoblib('DATA_all_texts/all_textdata.joblib', self.texts_data)

		return None

	def make_real_unique_tweets_list(self):
		self.texts_data = loadJoblib('DATA_all_texts/all_textdata.joblib')

		for idx, tweet in enumerate(self.texts_data):
			if tweet is not None:
				self.real_data[idx]=tweet

		for idx, tweet in self.real_data.items():
			if tweet not in self.unique_data.values():
				self.unique_data[idx] = tweet

		df = pd.read_csv('DATA_csv/covid19.csv')
		key = list(self.unique_data.keys())
		labels = list(df.iloc[key]['assessment_option_id'])

		dumpJoblib('DATA_all_texts/real_textdata.joblib', self.real_data)
		dumpJoblib('DATA_all_texts/unique_textdata.joblib', self.unique_data)
		dumpJoblib('DATA_all_texts/unique_label_file.joblib', labels)

		return None

	def ignore_few_data(self):

		df = pd.read_csv('DATA_csv/covid19.csv')

		new_label = []
		new_text = []

		for key in list(self.unique_data.keys()):
			ass = df.iloc[key]['assessment_option_id']
			txt = self.unique_data[key]
			if ass != 66 and ass !=68:
				new_label.append(ass)
				new_text.append(txt)

		dumpJoblib('DATA_all_texts/only_4labels_label.joblib', new_label)
		dumpJoblib('DATA_all_texts/only_4labels_textdata.joblib', new_text)



class GetTweet:
	def __init__(self):
		self.texts_data = loadJoblib('DATA_all_texts/all_textdata.joblib')
		self.real_data = loadJoblib('DATA_all_texts/real_textdata.joblib')
		self.unique_data = loadJoblib('DATA_all_texts/unique_textdata.joblib')

		self.tweet_id_list = None
		self.assessment_list = None

	def get_all_tweets_list(self):
		df = pd.read_csv('DATA_csv/covid19.csv')
		self.tweet_id_list = list(df['tweet_id'])
		self.assessment_list = list(df['assessment_option_id']) 
		self.assessment_list_after = loadJoblib('DATA_all_texts/only_4labels_label.joblib')

		print(f'全データの件数:{len(self.texts_data)}')
		print(f'現存するデータの数：{len(self.real_data)}')
		print(f'重複を取り除いた件数：{len(self.unique_data)}')

		print('-' * 40)

		print('加工前')

		print('63: 　　　　一般事実　 {}個'.format(self.assessment_list.count(63)))
		print('64: 　　　　個人事実 　{}個'.format(self.assessment_list.count(64)))
		print('65: 　　　意見・感想 　{}個'.format(self.assessment_list.count(65)))
		print('66: 　　　　判定困難 　{}個'.format(self.assessment_list.count(66)))
		print('67: 　　　　関係なし 　{}個'.format(self.assessment_list.count(67)))
		print('68: 事実だが判定困難 　{}個'.format(self.assessment_list.count(68)))

		print('-' * 40)

		print('加工 \n(1)現存するデータのみにする\n(2) 重複データは除く\n(3)ラベル66,68は外す')

		print('-' * 40)

		print('加工後')

		print('63: 　　　　一般事実　 {}個'.format(self.assessment_list_after.count(63)))
		print('64: 　　　　個人事実 　{}個'.format(self.assessment_list_after.count(64)))
		print('65: 　　　意見・感想 　{}個'.format(self.assessment_list_after.count(65)))
		print('66: 　　　　判定困難 　{}個'.format(self.assessment_list_after.count(66)))
		print('67: 　　　　関係なし 　{}個'.format(self.assessment_list_after.count(67)))
		print('68: 事実だが判定困難 　{}個'.format(self.assessment_list_after.count(68)))


		return (self.tweet_id_list, self.assessment_list)

	def get_length(self):
		tweets_list = list(self.unique_data.values())

		max_length = 0

		for tweet in tweets_list:
		    if max_length < len(tweet):
		        max_length = len(tweet)
		        
		print(f'\nツイートの最長の長さは{max_length}です')

		return None


if '__name__' == '__main__':
	pass

