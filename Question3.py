import pandas as pd
import sqlite3


conn = sqlite3.connect('itdaadb.db')
df = pd.read_sql_query("SELECT * FROM heart_patient", conn)

"""Checking for NULL values"""
NAs = pd.concat([df.isnull().sum()], axis=1, keys=["Heart"])
NAs[NAs.sum(axis=1) > 0]
print(NAs)

"""Checking for duplicate values"""
print("\nDuplicate values\n",df.loc[df.duplicated()])

"""Cleaning duplicate values"""
df.drop_duplicates(keep='first',inplace=True)
print("\nDuplicate values are gone\n",df.loc[df.duplicated()], "\n")




from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

"""3.2"""

X = df.drop(columns = 'target', axis = 1)
Y = df['target']

from sklearn.preprocessing import MinMaxScaler

Scaler = MinMaxScaler()

df = Scaler.fit_transform(df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']])




X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2, stratify=Y)


models = {
    "Random Forest": RandomForestClassifier(),
    "SVM": svm.SVC(kernel='linear'),
    "Gradient Boosting": GradientBoostingClassifier()
}



for name, model in models.items():
    model.fit(X_train, Y_train)
    predictions = model.predict(X_test)
    print(f"{name} Accuracy: {accuracy_score(Y_test, predictions)*100:.2f}%")
    
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train,Y_train)

trainedModel = 'Trained_model.sav'
pickle.dump(classifier, open(trainedModel, 'wb'))
print("Model Saved")

