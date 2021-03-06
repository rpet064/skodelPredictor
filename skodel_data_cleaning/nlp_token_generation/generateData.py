import pandas as pd
import math
from preprocess_indv_words import PreprocessIndvWords

# prepare data
csv_url = 'skodel_data.csv'
skodel_df = pd.read_csv(csv_url, encoding='latin1')
skodel_df.fillna('', inplace=True)

# prepare names, no duplicate, alphabetical
list_of_names = skodel_df['name'].tolist()
no_duplicate_list_of_names = list(set(list_of_names))
column_1 = [ele.split()[0] for ele in no_duplicate_list_of_names]
column_1 = sorted(column_1)

# total checkins & total mood score
total_checkins = skodel_df.groupby('name')['name'].value_counts()
total_mood_score = skodel_df.groupby('name')['mood'].sum()
# average mood score per check in
avg_mood_list = (total_mood_score / total_checkins).tolist()
column_4 = [round(avg, 2) for avg in avg_mood_list]
column_2 = total_checkins.tolist()
column_3 = total_mood_score.tolist()

# average words per check in
skodel_df['total_words'] = skodel_df['third_question_response'].str.count(' ') + 1
# class average
total_words_class = skodel_df['total_words'].sum()
total_checkins_class = len(skodel_df)
class_average_words = int(total_words_class / total_checkins_class)
# per student
total_words_student = skodel_df.groupby('name')['total_words'].sum()
avg_words_check_in = (total_words_student / total_checkins ).tolist()
column_5 = [math.ceil(avg) for avg in avg_words_check_in]

# extract tags
tags_list = skodel_df['tags'].tolist()
column_6 = list(filter(None, tags_list))

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

# whole class mean mood
avg_mood_class = skodel_df['mood'].mean()
column_8 = str(round(avg_mood_class, 2))
column_8 = column_8.split(',')

# create df-> excel
student_summary_data_df = pd.DataFrame(list(zip(column_1, column_2, column_3, column_4, column_5)),
             columns =['name', 'total_checkins', 'total_mood_score', 'mood_mean_score', 'avg_words_check_in'])

df1 = pd.DataFrame(column_6, columns = ['tags'])
df2 = pd.DataFrame(column_7, columns = ['responses'])
df3 = pd.DataFrame(column_8, columns = ['whole_class_mean'])

pd.concat([df1,df2, df3],axis=1).to_excel('class_summary_data.xlsx')

# drop students who changed school
student_summary_data_df = student_summary_data_df.drop(student_summary_data_df.index[10])
student_summary_data_df = student_summary_data_df.drop(student_summary_data_df.index[10])
student_summary_data_df.to_excel('student_summary_data.xlsx', index=False)
