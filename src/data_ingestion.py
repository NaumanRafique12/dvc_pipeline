import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

data_url = 'https://raw.githubusercontent.com/campusx-official/jupyter-masterclass/main/tweet_emotions.csv'
df = pd.read_csv(data_url)
df.drop(columns=['tweet_id'], inplace=True)
final_df = df[df['sentiment'].isin(['happiness', 'sadness'])]
final_df['sentiment'].replace({'happiness': 1, 'sadness': 0}, inplace=True)
 
data_path = os.path.join("data", 'data')
os.makedirs(data_path, exist_ok=True)
final_df.to_csv(os.path.join(data_path, "data.csv"), index=False)
 