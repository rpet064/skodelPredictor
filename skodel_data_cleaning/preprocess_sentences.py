from regex import F
from nlp_token_generation.contraction_dict import contraction_map as cd
import nltk
import ssl
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re
from autocorrect import Speller
from autocorrect import Speller 
from nltk.tokenize import word_tokenize

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

    def remove_punctuation(self):
        # remove punctuation
        self.without_punctuation = []
        for word in self.without_white_space:
            for letter in word:
                if letter in string.punctuation:
                    word = word.replace(letter,"")
            self.without_punctuation.append(word)
        return self

    def remove_integers(self):
        # remove integers
        self.without_integer = []
        for sentence in self.without_punctuation:
           self.without_integer.append(re.sub(r'\b(?:\d+|\w)\b\s*', '', sentence))
        return self

    def remove_duplicates(self):
        self.formatted_text = []
        self.combined_formatted = []
        self.final_formatted = []
        self.pattern_alpha = re.compile(r"([A-Za-z])\1{1,}", re.DOTALL)
        # Pattern matching for all the punctuations that can occur
        self.pattern_punct = re.compile(r'([.,/#!$%^&*?;:{}=_`~()+-])\1{1,}')
        # Limiting all the  repeatation to two characters.
        for sentence in self.without_integer:
            self.formatted_text.append(self.pattern_alpha.sub(r"\1\1", sentence))
        # Limiting punctuations in previously formatted string to only one.
        for sentence in self.formatted_text:
            self.combined_formatted.append(self.pattern_punct.sub(r'\1', sentence))
        for sentence in self.formatted_text:
            self.final_formatted.append(re.sub(' {2,}',' ', sentence))
        return self.final_formatted
