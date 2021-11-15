import requests
import json
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

csv_url = (
    "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
)
data = pd.read_csv(csv_url, sep=";")


train, test = train_test_split(data)

train_x = train.drop(["quality"], axis=1)

test_x = test.drop(["quality"], axis=1)
train_y = train[["quality"]]
test_y = test[["quality"]]

print(test_x.iloc[:2])
print(len(test_x.iloc[:2]))
print(type(test_x.iloc[:2]))

data_json = test_x.iloc[:2].to_json(orient="records")
print(data_json)

headers = {'Content-Type': 'application/json; format=pandas-records'}
request_uri = 'http://127.0.0.1:5000/invocations'

if __name__ == '__main__':
    try:
        response = requests.post(request_uri, data=data_json, headers=headers)
        print(response.content)
        print('done!!!')
    except Exception as ex:
        raise (ex)