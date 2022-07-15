import pandas as pd

csv_url = 'skodel_data.csv'

# prepare data
skodel_df = pd.read_csv(csv_url, encoding='latin1')
skodel_df.fillna('', inplace= True)

# whole class data
total_class_mean = skodel_df['mood'].mean()

# prepare names, no duplicate, alphabetical
list_of_names = skodel_df['name'].tolist()
no_duplicate_list_of_names = list(set(list_of_names))
column_1 = [ele.split()[0] for ele in no_duplicate_list_of_names]
column_1 = sorted(column_1)

# prepare other columns
total_checkins = skodel_df['name'].value_counts()
total_mood_score = skodel_df.groupby('name')['mood'].sum()
column_4 = (total_mood_score / total_checkins ).tolist()
column_2 = total_checkins.tolist()
column_3 = total_mood_score.tolist()

# create df-> excel
skodel_summary_data_df = pd.DataFrame(list(zip(column_1, column_2, column_3, column_4)),
             columns =['name', 'total_checkins', 'total_mood_score', 'mood_mean_score'])

skodel_summary_data_df.to_excel('skodel_summary_data.xlsx' )

