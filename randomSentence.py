# Returns random sentences to PiPy's main logic script

import random
import urllib2

sentencePoolOne = [line.rstrip('\n') for line in open('randomSentences.txt')]
sentencePoolTwo = [line.rstrip('\n') for line in urllib2.urlopen("http://scraper.reppardwalker.com/sentences.txt")]

def main():

    run = True
    
    while run:
        totalPost = [random.choice(sentencePoolOne), random.choice(sentencePoolTwo), random.choice(sentencePoolOne)]
        joinedPost = ' '.join(totalPost)
        charCount = len(joinedPost)
    
        if charCount <= 140:
            return joinedPost
            run = False


main()


