# Returns random sentences to PiPy's main logic script

import random
import urllib2


# Pull 50 random lines from scraped sentence file - store as lines in list
sentencePool = random.sample(list(line.rstrip('\n') for line in open('randomSentences.txt')), 50)

def main():

    run = True
    
    while run:
        totalPost = [random.choice(sentencePool),
                     random.choice(sentencePool),
                     random.choice(sentencePool)]
        
        joinedPost = ' '.join(totalPost)
        charCount = len(joinedPost)
    
        if charCount <= 140:
            return joinedPost
            run = False


main()


