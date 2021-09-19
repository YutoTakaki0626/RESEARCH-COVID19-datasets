import time

class Id2Tweets:
	def _init__(self, epoch_cnt, limit_number, current_number, final_number):
		self.epoch_cnt = epoch_cnt
		self.limit_number = limit_number
		self.current_number = current_number
		self.final_number = final_number
		self.end_number = None

	def transform(self):
		try:
		    while True:
		        inner_cnt = 0
		        self.epoch_cnt += 1
		        tweets_list = []
		        self.end_number = self.current_number + self.limit_number - 1

		        print(f'{self.epoch_cnt}回目の実行です ', end='')

		        if self.end_number > self.final_number:
		            self.end_number = self.final_number

		        for tweet_id in tweet_id_list[self.current_number:(self.end_number+1)]:
		            try:
		                inner_cnt += 1
		                if inner_cnt == 450:
		                    print('　順調に進んでいます')
		                tweet = api.get_status(tweet_id).text
		                tweets_list.append(tweet)
		            except:
		                tweets_list.append(None)


		        dumpJoblib(f'texts_list_{str(self.current_number)}_{str(self.end_number)}.joblib', tweets_list)    
		        print(f'{str(self.current_number)}から{str(self.end_number)}のjoblibファイルを作成しました!!\n')

		        if self.end_number == self.final_number:
		        	break

		        self.current_number = self.end_number + 1

		        time.sleep(60*15)
	        
	except:
	    print('エラーが発生しました!! 対処してください!! ')


if '__name__' == '__main__':
	pass