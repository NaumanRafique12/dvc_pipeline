import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import yaml
test_size = yaml.safe_load(open("params.yaml","r"))['data_splitting']['test_size']
df = pd.read_csv("./data/data/data.csv")
train_data, test_data = train_test_split(df, test_size=test_size, random_state=42)
print(train_data)
data_path = os.path.join("data", 'raw')
os.makedirs(data_path, exist_ok=True)
train_data.to_csv(os.path.join(data_path, "train.csv"), index=False)
test_data.to_csv(os.path.join(data_path, "test.csv"), index=False)