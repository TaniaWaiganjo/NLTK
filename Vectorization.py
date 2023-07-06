from nltk import word_tokenize
from string import punctuation
from nltk.corpus import stopwords

stopwords = stopwords.words('english')
stop_and_punct = set(stopwords).union(set(punctuation))

from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

wnl = WordNetLemmatizer()


def penn2morphy(penntag):
    # converts penn treebank tags to wordnet
    # careful with the indentation. IT ALWAYS MEANS SOMETHING!!!!
    morphy_tag = {'NN': 'n', 'JJ': 'a',
                  'VB': 'v', 'RB': 'r'}
    try:
        return morphy_tag[penntag[:2]]
    except:
        return 'n'  # if no mapping found,


def lemmatize_sent(text):

    return [wnl.lemmatize(word.lower(), pos=penn2morphy(tag))
                  for word, tag in pos_tag(word_tokenize(text))]



# preprocess being removing stopwords, punctuation , word tokenization, and lemmatization
def preprocess_text(text):
     return [word for word in text
            if word not in stop_and_punct
            and not word.isdigit()]


# vector is an array of numbers
# Vector Space Model- conceptualizing language as numbers
# Bag-of-words = counting each sentence as a vector of numbers, each number representing the count of a word in the corpus
# collections.Counter to get bag of words
from collections import Counter

sent1 = 'The quick brown fox jumps over the lazy brown dog'
sent2 = "Mr brown jumps over the lazy fox"

# processed_sent1 = preprocess_text(sent1)
# processed_sent2 = preprocess_text(sent2)
process1_1 = lemmatize_sent(sent1)
process2_1 = lemmatize_sent(sent2)

process1_2 = preprocess_text(process1_1)
process2_2 = preprocess_text(process2_1)

print(process1_2)
print(process2_2)

# Bag of words count the words
print('word counts:')
print(Counter(process1_2))
print(Counter(process2_2))

# Vectorization
# https://www.kaggle.com/code/alvations/basic-nlp-with-nltk?scriptVersionId=1831367&cellId=63

# USING SCIKIT-LEARN
from io import StringIO # convert any string to work like a file
from sklearn.feature_extraction.text import CountVectorizer