import pandas as pd
from preprocess_sentences import Preprocess_Sentences

# prepare data
csv_url = 'skodel_data_original.csv'
skodel_df = pd.read_csv(csv_url, encoding='latin1')
skodel_df.fillna('', inplace=True)

# chain methods from PreprocessIndvWords class to clean data
piw = Preprocess_Sentences(skodel_df['third_question_response'])
column_9 = piw.without_line_break().remove_whitespace().change_contractions()
print(column_9)
# column_7 = piw.without_line_break().remove_whitespace().change_contractions().remove_punctuation(
# ).remove_integers().remove_stopwords().remove_duplicates().spelling_fixer().lemmatization()

