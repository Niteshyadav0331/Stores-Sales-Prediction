import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report
import pickle

# reading cleaned data
df=pd.read_csv('cleaned_data.csv')

# splitting the x and y labels
features = ['Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_MRP',
       'Outlet_Location_Type', 'Item_Outlet_Sales', 'Outlet_Age',
       'Item_Visibility_bins', 'Grocery Store', 'Supermarket Type1',
       'Supermarket Type2', 'Supermarket Type3']
X = df[features]
y = df['Rate']

# splitting Data into train and test.
X_train, X_valid, y_train, y_valid = train_test_split(X, y,test_size=20, random_state=42)

# Checking shape.
print (X_train.shape, y_train.shape)
print (X_valid.shape, y_valid.shape)


# making Model.
model=RandomForestClassifier()
model.fit(X_train,y_train)
# accuracy of RandomForest Model
y_predxgb = model.predict(X_valid)
report2 = classification_report(y_valid, y_predxgb)
print(report2)
print("Accuracy of the RandomForest Model is:",accuracy_score(y_valid,y_predxgb)*100,"%")

# dumping model
filename='Finalmodel.sav'
pickle.dump(model,open(filename,'wb'))