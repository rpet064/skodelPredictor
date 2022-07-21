from nlp_token_generation.contraction_dict import contraction_map as cd
import nltk
import ssl
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re
from autocorrect import Speller
from autocorrect import Speller 

class Preprocess_Sentences:

    def __init__(self, data):

        # disabling ssl check
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        # nltk library downloads
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        self.data = data
        self.response_list = [resp.lower()for resp in self.data]
    
    def without_line_break(self):
        # all lowercase
        # Replacing all the occurrences of \n,\\n,\t,\\ (and other edge cases) with space
        self.without_line_breaks = [text.replace('\\n', ' ').replace('\n', ' ').replace('\t', ' ').replace(
            '\\', ' ').replace('. com', '.com').replace('\r', '') for text in self.response_list]
        return self

    def remove_whitespace(self):
        # remove white space, filter list and seperate list
        self.without_white_space = [resp.strip() for resp in self.without_line_breaks if len(resp) > 11]
        return self

    def change_contractions(self):
        # changing contractions (let's => let us)
        for word in self.without_white_space:
            if word in cd:
                self.without_contractions = [item.replace(word, cd[word]) for item in self.without_white_space]
        return self.without_contractions
