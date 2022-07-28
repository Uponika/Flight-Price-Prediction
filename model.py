import pandas as pd
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
# import matplotlib.pyplot as plt
# import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def loadData(file):
    data = pd.read_excel(file)
    return data

def preProcessing(data, columns, unwantedCols):
    data[columns] = data[columns].apply(label_encoder.fit_transform)
    data = data.drop(unwantedCols, axis=1)
    data['Duration'] = data['Duration'].str.replace('h', '*60').str.replace('m', '*1').str.replace(' ', '+').apply(
        eval)
    return data

def splitData(data):
    x = data.drop(['Price'], axis = 1)
    y = data['Price']
    x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)
    return (x_train, x_test, y_train, y_test)


def modelTrain(data, x_train, y_train):
    # create regressor object
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    regressor.fit(x_train, y_train)
    return regressor

