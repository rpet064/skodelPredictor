import pandas as pd
import math

from sqlalchemy import column
from preprocess_indv_words import PreprocessIndvWords

# prepare data
csv_url = 'skodel_data.csv'
skodel_df = pd.read_csv(csv_url, encoding='latin1')
skodel_df.fillna('', inplace=True)

# chain methods from PreprocessIndvWords class to clean data
piw = PreprocessIndvWords(skodel_df['third_question_response'])
column_7 = piw.without_line_break().remove_whitespace().change_contractions().remove_punctuation(
).remove_integers().remove_stopwords().remove_duplicates().spelling_fixer().lemmatization()

# special case data cleaning
for i, _ in enumerate(column_7):
    if column_7[i] == 'sleep\x98\x81':
        column_7[i] = 'sleep'
    if column_7[i] == 'neckbrainarmsfingersand':
       column_7[i] = 'neck'
    if column_7[i] == 'better\x9820220515':
       column_7[i] = 'better'

column_7.extend(['brain', 'arms', 'fingers'])
