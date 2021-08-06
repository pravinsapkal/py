import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def marks_prediction(marks):
    path = "./student_info.csv"
    df = pd.read_csv(path)

    df2 = df.fillna(df.mean())

    X = df2.drop("student_marks", axis = "columns")
    y = df2.drop("study_hours", axis = "columns")

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=51 )

    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()

    lr.fit(X_train , y_train)

    return lr.predict([[marks]])