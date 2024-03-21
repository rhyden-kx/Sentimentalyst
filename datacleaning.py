import pandas as pd
import emoji
import string



pd.set_option('display.max_columns', None)
# Specify the file path
file_path = 'dataset/steam_dataset_trunc.csv'

# Read the CSV file
data = pd.read_csv(file_path)

def clean_data(df):
  pd.options.mode.copy_on_write = True
  
  # Remove rows with empty review_text
  df = df[df['review_text'].notnull()]

  # Remove emoji rows
  df['review_text'] = df['review_text'].apply(lambda x: emoji.replace_emoji(x,''))
  
  # Remove punctuation
  df['review_text'] = df['review_text'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
  # Replace non-ASCII characters with empty character
  df['review_text'] = df['review_text'].apply(lambda x: ''.join([i if ord(i) < 128 else '' for i in x]))
  
  # Remove rows with empty review_text
  df = df[df['review_text']!='']

  return df

clean_data(data)