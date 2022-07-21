from data_preprocessing.contraction_dict import contraction_map as cd
import nltk
import ssl
from nltk.corpus import stopwords
import string
import re
from autocorrect import Speller
from autocorrect import Speller 

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
        return self
    
    def spelling_fixer(self):
        self.spell = Speller(lang='en') 
        self.corrected_text = self.spell(self.final_formatted)
        return self
    
    def lemmatization(self):
        self.w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
        self.lemmatizer = nltk.stem.WordNetLemmatizer()
        self.lemma = [self.lemmatizer.lemmatize(w,'v') for w in self.w_tokenizer.tokenize(self.corrected_text)]
        return self.lemma
        