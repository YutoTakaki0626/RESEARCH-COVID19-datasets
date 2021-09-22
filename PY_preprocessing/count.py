import re
import string
import emoji

from emoji_list import get_all_emoji

class Count:
    def __init__(self):
        self.all_emojis = get_all_emoji()

    def user_mention(self, tweets_list):
        '''
        count the number of of tweets contained USER MENTION ('@XXXX')
        '''

        user_mention_list = []

        for tweet in tweets_list:
            if tweet[0] == '@':
                user_mention_list.append(tweet)

            if re.search(r'@[0-9a-zA-Z_]+\s', tweet) is not None:
                user_mention_list.append(tweet)

            if re.search(r'@[0-9a-zA-Z_]{4,}', tweet) is not None:
                user_mention_list.append(tweet)

        user_mention_list = list(set(user_mention_list))
        user_mention_cnt = len(user_mention_list)
                
        return user_mention_cnt, user_mention_list


    def url(self, tweets_list):
        '''
        count the number of of tweets contained URL ('httpXXX')

        '''

        url_cnt = 0
        url_list = []

        for tweet in tweets_list:
            if re.search(r'http', tweet) is not None:
                url_cnt += 1
                url_list.append(tweet)
                
        return url_cnt, url_list

    def hashtag(self, tweets_list):
        '''
        count the number of tweets contained Hash Tag  ('#XXXX')
        '''

        hashtag_cnt = 0
        hashtag_list = []

        for tweet in tweets_list:
            if re.search(r'#', tweet) is not None:
                hashtag_cnt += 1
                hashtag_list.append(tweet)
                
        return hashtag_cnt, hashtag_list

    def www(self, tweets_list):
        '''
        count the number of of tweets contained 'w' 
        It uses when laughing in Japan

        '''
        
        w_list = []
        
        for tweet in tweets_list:
            contexts = tweet.strip()
            for context in contexts:
                if context[-1]=='w':
                    w_list.append(tweet)
                    break
            
        for tweet in tweets_list:
            if re.search(r'ww+', tweet) is not None:
                if tweet[-1] != 'w':
                    w_list.append(tweet)

        w_list = list(set(w_list))
        w_cnt = len(w_list)

        return w_cnt, w_list

    def not_single(self, tweets_list):
        '''
        count the tweets contained alphabet over 2 letters
        '''

        not_single_list = []

        for tweet in tweets_list:
            if re.search(r'[a-zA-Z][a-zA-Z]+', tweet) is not None:
                not_single_list.append(tweet)
        not_single_cnt = len(not_single_list)
                
        return not_single_cnt, not_single_list

    def mixed_tweet(self, tweets_list):
        '''
        count the tweets contained English and Japanese
        '''

        lower_list = list(string.ascii_lowercase)
        upper_list = list(string.ascii_uppercase)
        alphabet_list = lower_list + upper_list

        contained_cnt = 0
        contained_list = []

        for tweet in tweets_list:
            for alphabet in alphabet_list:
                if re.search(r'{}'.format(alphabet), tweet) is not None:
                        contained_cnt += 1
                        contained_list.append(tweet)
                        break

        return contained_cnt, contained_list


    def emojis(self, tweets_list):
        '''
        count the tweets contained Eemoji
        '''
        emojis_list = []
        for tweet in tweets_list:
            for string in tweet:
                if string in self.all_emojis:
                    emojis_list.append(tweet)
                    break

        emojis_cnt = len(emojis_list)

        return emojis_cnt, emojis_list

    def covid19(self, tweets_list):
        '''
        count the number of of tweets contained conid-19 ('httpXXX')
        '''
        
        covid_cnt = 0
        covid_list = []

        for tweet in tweets_list:
            if re.search(r'[cC][oO][vV][iI][dD]', tweet) is not None or \
                re.search(r'[cC][oO][rR][oO][nN][aA]', tweet) is not None or \
                re.search(r'[wW][hH][oO]', tweet) is not None or \
                re.search(r'[pP][cC][rR]', tweet) is not None or \
                re.search(r'[vV][iI][rR][uU][sS]', tweet) is not None: 
                covid_cnt += 1
                covid_list.append(tweet)
                
        return covid_cnt, covid_list
