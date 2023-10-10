import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
def init():
    print("초기화 용도")
    df = pd.read_csv("D:/핀테크_평일/django/bank_cleaning.csv")
    print( df )
    f = ['age' ,'duration', 'campaign', 'pdays', 'previous']
    label = 'y'
    X , y = df[f], df[label]
    X_train, X_test, y_train, y_test = \
                    train_test_split( X, y, test_size=0.3 )
    gbc = GradientBoostingClassifier()
    gbc.fit( X_train, y_train )
    print("train : ", gbc.score(X_train, y_train ))
    print("test : ", gbc.score(X_test, y_test ))

    return gbc
