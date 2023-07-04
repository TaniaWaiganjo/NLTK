# https://www.kaggle.com/code/alvations/basic-nlp-with-nltk
# sentence tokenization is the process of splitting up strings to sentences
# word tokenization is splitting of sentences to words
import nltk
# downlad punkt
# run download once
# nltk.download('webtext')
from nltk.corpus import webtext

print(webtext.fileids())

# enumerate function in py keeps count of iterations by adding a counter
# enumerate(iterable, start), default start is 0, but you can specifiy it
# https://www.geeksforgeeks.org/enumerate-in-python/
for i, line in enumerate(webtext.raw('singles.txt').split('\n')):
    if i > 15:
        break
    print(str(i) + ':\t' + line)

# https://www.tutorialspoint.com/python3/string_split.htm#:~:text=The%20split()%20method%20returns,number%20of%20splits%20to%20num.
# split() returns list of all words in the string using str as the separator. splits on all whitespace if left unspecified
print(webtext.raw('singles.txt').split('\n'))

# how long can i be?
print(len(webtext.fileids()))

# for cryig out loud, its \n \n \n \n otherwise throws off your code

# Looking at one specific string
candidate8 = webtext.raw('singles.txt').split('\n')[8]
print(candidate8)

# Sentence tokenization
# splits strings into sentences
from nltk import sent_tokenize, word_tokenize
# nltk.download('punkt')
# punkt is a statistical model works for most well-formed text but not noisy
# transforms string to sentences
print(sent_tokenize(candidate8))

for sent in sent_tokenize(candidate8):
     print(word_tokenize(sent))
# difference between above and below is above each sentence is its own string then words are tokenized while below the entire paragraph is one sting
print(word_tokenize(candidate8))

# Lowecase
word_tokenize(candidate8)
for sent in sent_tokenize(candidate8):
    print([word.lower() for word in word_tokenize(sent)])

# STOPWORDS
# non-content words that primarily has only grammatical function
#nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
# can also use as a set as set checking is faster = set(stopwords.words('english')
print(stop_words)
print(len(stop_words))

# remove stopwords to get the content
candidate8_tokenized_lowered = list(map(str.lower, word_tokenize(candidate8)))
print(candidate8_tokenized_lowered)

print([word for word in candidate8_tokenized_lowered if word not in stop_words])

# remove punctuation using string.punctuation
from string import punctuation
print('from string. punctuation:', type(punctuation), punctuation)

# the punctuation signs are a string so change into a set
# can create a set with both punct and stop and use the set to filter out
stop_and_punct = set(stop_words).union(set(punctuation))
print(stop_and_punct)

print([word for word in candidate8_tokenized_lowered if word not in stop_and_punct])

# stronger stopword list such as stopwords_json
stop_json = set(stopwords_json['en'])