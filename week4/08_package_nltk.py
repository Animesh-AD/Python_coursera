import nltk
text = 'I am here for learning. I am currently doing everything'
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
print(word_tokenize(text))
print(nltk.tokenize.sent_tokenize(text))
stopwords = stopwords.words('english')
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append((i))
print(new_text)

'''
The first function used is word_tokenize(). This takes this text and produces the first part of the output in which 
the words are ‘tokenized’ or simply separated by a whitespace. The same can be done with the split() function in the string,
 but the use of the package is far more efficient when it comes to larger blocks of code.

The second function sent_tokenize() takes this block of text and tokenizes by ‘sentences’.

For the third output, I first split the code and remove what is called ‘stopwords’. Stopwords are words in
 the English language that can be considered redundant and adding little value while you are undertaking natural 
 language processing. These include words such as ‘a’, ‘the’, ‘him’. First I'll create a list of these stopwords 
 and then remove them using a for loop to form a new list called new_text. You will notice the difference by comparing
  the first and the final output of the code.'''