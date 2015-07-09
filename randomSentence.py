# Returns random sentences to PiPy's main logic script

import random

sentencePool = [line.rstrip('\n') for line in open('randomSentences.txt')]

def main():

    run = True
    
    while run:
        totalPost = [random.choice(sentencePool), random.choice(sentencePool), random.choice(sentencePool)]
        joinedPost = ' '.join(totalPost)
        charCount = len(joinedPost)
    
        if charCount <= 140:
            return joinedPost
            run = False


main()


