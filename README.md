# PiPyThePoet - Twitter Bot - @PiPyThePoet
#
# Fun little project for the RPi written in Python. By setting up a basic cron job on my Raspberry Pi, PiPy's script will be
# run at the top of every hour, which results in PiPy selecting a random pool of sentences (stored within a txt file). 
# If the random selection doesn't exceed Twitter's char cap of 140 characters, the selected sentences will be tweeted.
# If the random selection exceeds char limit, script loops until requirements met and tweet is sent.
