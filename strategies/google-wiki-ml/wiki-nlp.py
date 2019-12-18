import wikipedia
from nltk.tokenize import RegexpTokenizer

# Tokenize by word, remove punctuation
text_str = wikipedia.page("Apple Inc.").content
tokenizer = RegexpTokenizer(r'\w+')
text0 = tokenizer.tokenize(text_str)
print("# of words in original text:", len(text0))

# Remove stopwords
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

text = []
for word in text0:
    if word not in stop_words:
        text.append(word)

print("# of words after stopword removal:", len(text))

print(text_str)
