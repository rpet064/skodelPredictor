import pandas as pd
import math
from contraction_dict import contraction_map as cd
import re
import nltk from nltk.corpus 
import stopwords 
nltk.download('stopwords') 

csv_url = 'skodel_data.csv'


# prepare data
skodel_df = pd.read_csv(csv_url, encoding='latin1')
skodel_df.fillna('', inplace=True)

# # prepare names, no duplicate, alphabetical
# list_of_names = skodel_df['name'].tolist()
# no_duplicate_list_of_names = list(set(list_of_names))
# column_1 = [ele.split()[0] for ele in no_duplicate_list_of_names]
# column_1 = sorted(column_1)

# # total checkins & total mood score
# total_checkins = skodel_df.groupby('name')['name'].value_counts()
# total_mood_score = skodel_df.groupby('name')['mood'].sum()
# # average mood score per check in
# avg_mood_list = (total_mood_score / total_checkins).tolist()
# column_4 = [round(avg, 2) for avg in avg_mood_list]
# column_2 = total_checkins.tolist()
# column_3 = total_mood_score.tolist()

# # average words per check in
# skodel_df['total_words'] = skodel_df['third_question_response'].str.count(' ') + 1
# # class average
# total_words_class = skodel_df['total_words'].sum()
# total_checkins_class = len(skodel_df)
# class_average_words = int(total_words_class / total_checkins_class)
# # per student
# total_words_student = skodel_df.groupby('name')['total_words'].sum()
# avg_words_check_in = (total_words_student / total_checkins ).tolist()
# column_5 = [math.ceil(avg) for avg in avg_words_check_in]

# # extract tags
# tags_list = skodel_df['tags'].tolist()
# column_6 = list(filter(None, tags_list))

# extract responses

# change input to lower case
response_list = [resp.lower()for resp in skodel_df['third_question_response']]
 # Replacing all the occurrences of \n,\\n,\t,\\ with space
without_line_breaks = [text.replace('\\n', ' ').replace('\n', ' ').replace('\t', ' ').replace('\\', ' ').replace(
     '. com', '.com').replace('\r', '').replace('_\x98_20220515 20:00:09605585+00:00', '') for text in response_list]
# remove white space, filter list and seperate list
without_white_space = [resp.strip() for resp in without_line_breaks if len(resp) > 11]
without_contractions = [i for item in without_white_space for i in item.split()]
# changing contractions (let's => let us)
for word in without_contractions:
     if word in cd:
        without_contractions = [item.replace(word, cd[word]) for item in without_contractions]
# remove numbers & punctuation
Formatted_Text = []
for word in without_contractions:
    Formatted_Text.append(re.sub(r"[^a-zA-Z0-9:$-,%.?!]+", ' ', word))

print(Formatted_Text)


# # whole class mean mood
# avg_mood_class = skodel_df['mood'].mean()
# column_8 = str(round(avg_mood_class, 2))
# column_8 = column_8.split(',')

# # create df-> excel
# student_summary_data_df = pd.DataFrame(list(zip(column_1, column_2, column_3, column_4, column_5)),
#              columns =['name', 'total_checkins', 'total_mood_score', 'mood_mean_score', 'avg_words_check_in'])

# df1 = pd.DataFrame(column_6, columns = ['tags'])
# df2 = pd.DataFrame(column_7, columns = ['responses'])
# df3 = pd.DataFrame(column_8, columns = ['whole_class_mean'])

# pd.concat([df1,df2, df3],axis=1).to_excel('class_summary_data.xlsx')

# # drop students who changed school
# student_summary_data_df = student_summary_data_df.drop(student_summary_data_df.index[10])
# student_summary_data_df = student_summary_data_df.drop(student_summary_data_df.index[10])
# student_summary_data_df.to_excel('student_summary_data.xlsx', index=False)
