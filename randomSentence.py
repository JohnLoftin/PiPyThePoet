import random

sentencePool = [line.rstrip('\n') for line in open('randomSentences.txt')]

def main():

    run = True
    while run:
        totalPost = [random.choice(sentencePool), random.choice(sentencePool), random.choice(sentencePool)]
        charCount = len(totalPost)
    
        if charCount <= 140:
            return ' '.join(totalPost)
            run = False


main()


