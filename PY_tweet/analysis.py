import pandas as pd

from PY_tweet.lists_file import *

class Analysis(object):
	"""docstring for analysis"""
	def __init__(self, labels_list, labels_name):
		self.labels_list = labels_list
		self.labels_name = labels_name

	def dump_labels_list(self):
		lst = loadJoblib('DATA_all_texts/only_4labels_label.joblib')

		for label in self.labels_list:
			labels = []
			for idx, inner_label in enumerate(lst):
				if label == inner_label:
					labels.append(idx)
			dumpJoblib(f'DATA_labels/labels_{label}.joblib', labels)


	def id_to_texts(self):
		labels = {}
		texts_dict = {}
		texts = loadJoblib('DATA_all_texts/only_4labels_textdata.joblib')

		for label in self.labels_list:
			labels[label] = loadJoblib(f'DATA_labels/labels_{label}.joblib')

		for key, label in labels.items():
			texts_dict[key] = []
			for idx, text in enumerate(texts):
				for lb in label:
					if idx == lb:
						texts_dict[key].append(text)

		for key, texts in texts_dict.items():
			dumpJoblib(f'DATA_labels/texts_{key}.joblib', texts)

	def how_many_func(self, func, string):
		texts_data = {}

		for label in self.labels_list:
			texts_data[label] = loadJoblib(f'DATA_labels/texts_{label}.joblib')

		print(f'This is count of {string}!!')
		print('-' * 30)

		cnt = 0

		for key, texts in texts_data.items():
			cnt_list, _ = func(texts)
			print(f'label:{self.labels_name[cnt]}({key})  全部で{len(texts)}個中{cnt_list}個    {(cnt_list / len(texts) * 100):.1f}%')
			cnt += 1

		print('-' * 30)
 













