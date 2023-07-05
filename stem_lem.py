import nltk
#import tokenization
from nltk import sent_tokenize, word_tokenize
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# stemming - trying to shorten a word with simple regex rules
# lemmatization - finding the root of the word using regex
# stemmer : porter stemmer lemmatizer : wordnet lemmatizer
from nltk.stem import PorterStemmer

# necessary corpus for candidate8
from nltk.corpus import webtext
candidate8 = webtext.raw('singles.txt').split('\n')[8]

# stopwords
from nltk.corpus import stopwords
stopwords = stopwords.words('english')

# punctuation
from string import punctuation
stop_and_punct = set(stopwords).union(set(punctuation))

porter = PorterStemmer()  # brackets included coz it's a class
for nord in ['walking', 'walks', 'walked']:
    print(porter.stem(nord))

# wnl.lemmatizer() assumes word is a noun if no pos tag in the input. pos - parts of speech
# need to find pos tag - whether word is noun, verb, adj, adv
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

wnl = WordNetLemmatizer()


# for word in ['ate', 'eating']:
#    print(wnl.lemmatize(word))

# penn treebank PTB is a dataset(corpus of english) 4.8 mill annotated words. Annotations includes POS, syntactic and semantic skeletons
# PTB tagset for pos : https://www.sketchengine.eu/penn-treebank-tagset/
def penn2morphy(penntag):
    # converts penn treebank tags to wordnet
    # careful with the indentation. IT ALWAYS MEANS SOMETHING!!!!
    morphy_tag = {'NN': 'n', 'JJ': 'a',
                  'VB': 'v', 'RB': 'r'}
    try:
        return morphy_tag[penntag[:2]]
    except:
        return 'n'  # if no mapping found, assume is noun


# `pos_tag` takes the tokenized sentence as input, i.e. list of string,
# and returns a tuple of (word, tg), i.e. list of tuples of strings
# we need to get the tag from the 2nd element .

statement = 'He is walking to school'
walking_tagged = pos_tag(word_tokenize(statement))
print(walking_tagged)


# print([wnl.lemmatize(word.lower(), pos=penn2morphy(tag)) for word, tag in walking_tagged])

# lemmatization function
def lemmatize_sent(text):
    return [wnl.lemmatize(word.lower(), pos=penn2morphy(tag))
            for word, tag in pos_tag(word_tokenize(text))]

print(lemmatize_sent(statement))

# note word.isdigit() contains numbers, can be used for filtering and comparison
print(candidate8)
print('Lemmatized and removed stopwords:')
print([word for word in lemmatize_sent(candidate8)
      if word not in stop_and_punct
       and not word.isdigit()])

# note difference between type, token, lemma and word family
