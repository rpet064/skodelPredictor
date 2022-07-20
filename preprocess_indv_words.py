from contraction_dict import contraction_map as cd
import nltk
import ssl
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

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
    
    def lowercase(self):
        # all lowercase
        self.response_list = [resp.lower()for resp in self.data]
        # Replacing all the occurrences of \n,\\n,\t,\\ (and other edge cases) with space
        self.without_line_breaks = [text.replace('\\n', ' ').replace('\n', ' ').replace('\t', ' ').replace(
            '\\', ' ').replace('. com', '.com').replace('\r', '').replace(
            '_\\x98_20220515 20:00:09605585+00:00', '').replace('\x9820220515', '') for text in self.response_list]
        self.remove_whitespace(self.without_line_breaks)

    def remove_whitespace(self, without_line_breaks):
        # remove white space, filter list and seperate list
        self.without_white_space = [resp.strip() for resp in without_line_breaks if len(resp) > 11]
        self.change_contractions(self.without_white_space)

    def change_contractions(self, without_white_space):
        # changing contractions (let's => let us)
        self.without_contractions = [i for item in without_white_space for i in item.split()]
        for word in self.without_contractions:
            if word in cd:
                self.without_contractions = [item.replace(word, cd[word]) for item in self.without_contractions]
        self.remove_punctuation(self.without_contractions)

    def remove_punctuation(self, without_contractions):
        # remove punctuation
        self.without_punctuation = []
        for word in without_contractions:
            for letter in word:
                if letter in string.punctuation:
                    word = word.replace(letter,"")
            self.without_punctuation.append(word)
        self.remove_integers(self.without_punctuation)

    def remove_integers(self, without_punctuation):
        # remove integers
        self.without_integer = [item for item in without_punctuation if not item.isdigit()]
        return self.without_integer
        # to clean        '2nd' => second       duplication     u => you      empty strings    stop words


        # # remove stopwords
        # stoplist = stopwords.words('english')
        # stoplist = set(stoplist)
        # remove_stop_words = [word for word in formatted_Text if word not in stoplist ]
        # words_string = ' '.join(remove_stop_words)

        # print(words_string)