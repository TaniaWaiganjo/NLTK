# Don't name your file nltk... messes with the import
# corpus is data packaged as raw text files

import nltk
#nltk.download('brown')
# above imports the package brown
from nltk.corpus import brown

worieds = brown.words() # returns list of words
print(worieds)

print(len(brown.words())) # number of words in the corpus

# return list of strings sents like sentences
print(brown.sents())

# fileids can access a specific file
whack = brown.sents(fileids='ca01')
print(whack)

whacky = brown.sents(fileids='ca33')
print(whacky)

# can find the number of files using len
print(len(brown.fileids()))

# printing the first 100 file ids
print(brown.fileids()[:100])

# accessing raw files using .raw
print(brown.raw('cb01'))
print(brown.raw('cb01').strip()[:1000])






