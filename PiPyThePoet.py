# PiPyThePoet - Twitter Bot

from twython import Twython, TwythonError
import time
import randomSentence

KEYS = [line.rstrip('\n') for line in open('keys.txt')]

# PiPy's twitter keys/authentication tokens
APP_KEY = KEYS[0]
APP_SECRET = KEYS[1]
OAUTH_TOKEN = KEYS[2]
OAUTH_TOKEN_SECRET = KEYS[3]

twitter_api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Sets post content -> return value of randomSentence.py
status = randomSentence.main()

# Post content - Twitter
twitter_api.update_status(status=status)
