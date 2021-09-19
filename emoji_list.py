import emoji

def get_all_emoji():
	'''
	get all emoji list
	'''
	all_emojis = []
	emojis = emoji.UNICODE_EMOJI.values()
	emojis = list(emojis)
	for num in range(len(emojis)):
	    element_emojis=list(emojis[num].keys())
	    all_emojis += element_emojis

	return all_emojis