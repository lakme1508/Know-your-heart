import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse.lil import lil_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class logisticR():
    def __init__(self,df):
        self.df = df
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        self.accuracy = None


    def model(self):       
        lr = LogisticRegression()
        lr.fit(self.x_train,self.y_train) 
        return lr
    
    def pre_processing(self):
        a = pd.get_dummies(self.df['cp'], prefix = "cp")
        b = pd.get_dummies(self.df['thal'], prefix = "thal")
        c = pd.get_dummies(self.df['slope'], prefix = "slope")
        frames = [self.df, a, b, c]
        self.df = pd.concat(frames, axis = 1)
        self.df = self.df.drop(columns = ['cp', 'thal', 'slope'])
        y = self.df.target.values
        x_data = self.df.drop(["target"],axis = 1)
        x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data)).values
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3,random_state=109)
        return x_train, y_train, x_test, y_test
    
    def predict(self):
        self.x_train, self.y_train, self.x_test, self.y_test = self.pre_processing()
        lr = self.model()
        self.accuracy = lr.score(self.x_test,self.y_test)*100
        return "Accuracy {:.2f}%".format(self.accuracy)
