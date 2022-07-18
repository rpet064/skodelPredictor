import pandas as pd

csv_url = 'skodel_data.csv'

# prepare data
skodel_df = pd.read_csv(csv_url, encoding='latin1')
skodel_df.fillna('', inplace= True)

# # whole class mean mood
# column_8 = skodel_df['mood'].mean()

# # prepare names, no duplicate, alphabetical
# list_of_names = skodel_df['name'].tolist()
# no_duplicate_list_of_names = list(set(list_of_names))
# column_1 = [ele.split()[0] for ele in no_duplicate_list_of_names]
# column_1 = sorted(column_1)

# # total checkins & total mood score
# total_checkins = skodel_df.groupby('name')['name'].value_counts()
# total_mood_score = skodel_df.groupby('name')['mood'].sum()
# # average mood score per check in
# column_4 = (total_mood_score / total_checkins ).tolist()
# column_2 = total_checkins.tolist()
# column_3 = total_mood_score.tolist()

# average words per check in
skodel_df['total_words'] = skodel_df['third_question_response'].str.count(' ') + 1
# class average
total_words_class = skodel_df['total_words'].sum()
total_checkins_class = len(skodel_df)
class_average_words = int(total_words_class / total_checkins_class)
# per student
total_words_student = skodel_df.groupby('name')['total_words'].sum()
column_5 = (total_words_student / total_checkins ).tolist()

# # extract tags
# tags_list = skodel_df['tags'].tolist()
# column_6 = list(filter(None, tags_list))

# # extract responses
# response_list = skodel_df['third_question_response'].tolist()
# response_list = [resp.replace('\r', '').replace('.', '').replace('-', '').replace('?', '').replace('_\x98_20220515 20:00:09605585+00:00', '') for resp in response_list]
# norm_response_list = list(filter(None, response_list))
# column_7 = " ".join(norm_response_list).split()
# column_7.remove('&s').remove('1')

# # create df-> excel
# student_summary_data_df = pd.DataFrame(list(zip(column_1, column_2, column_3, column_4, column_5)),
#              columns =['name', 'total_checkins', 'total_mood_score', 'mood_mean_score'])

# class_summary_data_df = pd.DataFrame(list(zip(column_5, column_6, column_7, column_8)),
#              columns =['tags', 'responses', 'total_class_mean'])

# student_summary_data_df.to_excel('student_summary_data.xlsx')
# class_summary_data_df.to_excel('class_summary_data.xlsx')

