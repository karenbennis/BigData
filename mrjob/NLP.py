import nltk
from nltk import word_tokenize
text = word_tokenize("Nicole saw the woman with binoculars")
output = nltk.pos_tag(text)
print(output)