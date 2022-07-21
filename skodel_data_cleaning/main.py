import pandas as pd
from preprocess_sentences import Preprocess_Sentences

# prepare data
csv_url = 'skodel_data_original.csv'
skodel_df = pd.read_csv(csv_url, encoding='latin1')
skodel_df.fillna('', inplace=True)

# chain methods from PreprocessIndvWords class to clean data
piw = Preprocess_Sentences(skodel_df['third_question_response'])
column_9 = piw.without_line_break().remove_whitespace().remove_punctuation().remove_integers().remove_duplicates()
# target data cleaning
for i, _ in enumerate(column_9):
    if column_9[i] == 'no itâ\x80\x99ok':
        column_9[i] = 'no it is okay'
    if column_9[i] == 'like thunder rain because of the rain hitting the roof tiles and the thunder sound cause of the rumbling it gives sound good sleepð\x9f\x98\x81':
       column_9[i] = 'like thunder rain because of the rain hitting the roof tiles and the thunder sound cause of the rumbling it gives a good sleep sound'
    if column_9[i] == 'might to school tomorrow but my cold isnâ\x80\x99contagious just so anyone reading this now knows':
       column_9[i] = 'might go to school tomorrow but my cold is not contagious, just so anyone reading this now knows'
    if column_9[i] == 'donâ\x80\x99have covid yet also am feeling better now':
        column_9[i] = 'do not have covid yet, I am also feeling better now'
    if column_9[i] == 'my sister has big tummy ache and she keeps vomiting in other places so hope we can try and find way to make her betterð\x9f\x98':
        column_9[i] = 'my sister has big tummy ache and she keeps vomiting in other places so hope we can try and find way to make her better'
    if column_9[i] == 'my neckbrainarmsfingersand everything hurts but im feeling fine':
       column_9[i] = 'my neck, brain, arms, fingers and everything hurts but i am feeling fine'
