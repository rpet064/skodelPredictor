from contraction_dict import contraction_map as cd
import nltk
import ssl
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re

class PreprocessIndvWords:

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
        self.data = data
        self.response_list = [resp.lower()for resp in self.data]
    
    def without_line_break(self):
        # all lowercase
        # Replacing all the occurrences of \n,\\n,\t,\\ (and other edge cases) with space
        self.without_line_breaks = [text.replace('\\n', ' ').replace('\n', ' ').replace('\t', ' ').replace(
            '\\', ' ').replace('. com', '.com').replace('\r', '').replace(
            '_\\x98_20220515 20:00:09605585+00:00', '').replace('better\x9820220515', 'better').replace('\x98\x81', '') for text in self.response_list]
        return self

    def remove_whitespace(self):
        # remove white space, filter list and seperate list
        self.without_white_space = [resp.strip() for resp in self.without_line_breaks if len(resp) > 11]
        return self

    def change_contractions(self):
        # changing contractions (let's => let us)
        self.without_contractions = [i for item in self.without_white_space for i in item.split()]
        for word in self.without_contractions:
            if word in cd:
                self.without_contractions = [item.replace(word, cd[word]) for item in self.without_contractions]
        return self

    def remove_punctuation(self):
        # remove punctuation
        self.without_punctuation = []
        for word in self.without_contractions:
            for letter in word:
                if letter in string.punctuation:
                    word = word.replace(letter,"")
            self.without_punctuation.append(word)
        return self

    def remove_integers(self):
        # remove integers
        self.without_integer = [item for item in self.without_punctuation if not item.isdigit()]
        return self

    def remove_stopwords(self):
        # remove stopwords
        self.stoplist = stopwords.words('english')
        self.stoplist = set(self.stoplist)
        self.remove_stop_words = [word for word in self.without_integer if word not in self.stoplist ]
        self.words_string = ' '.join(self.remove_stop_words)
        return self
        
    def remove_duplicates(self):
        self.pattern_alpha = re.compile(r"([A-Za-z])\1{1,}", re.DOTALL)
        # Limiting all the  repeatation to two characters.
        self.formatted_text = self.pattern_alpha.sub(r"\1\1", self.words_string) 
        # Pattern matching for all the punctuations that can occur
        self.pattern_punct = re.compile(r'([.,/#!$%^&*?;:{}=_`~()+-])\1{1,}')
        # Limiting punctuations in previously formatted string to only one.
        self.combined_formatted = self.pattern_punct.sub(r'\1', self.formatted_text)
        self.final_formatted = re.sub(' {2,}',' ', self.combined_formatted)
        return self.final_formatted