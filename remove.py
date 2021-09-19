import re
import string
import emoji

from emoji_list import get_all_emoji

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
            while re.search(r'http', tweet) is not None:
                an = re.search(r'http', tweet)
                start = an.span()[0]
                tweet = str(tweet[:start])
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


if '__name__' == '__main__':
    pass




