# Feature importances for random forest

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from models import df

model = RandomForestClassifier(n_estimators=200)
X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

# Split the dataset into the training set and test set
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = seed)
    
# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

model.fit(X_train, Y_train)

try:
    feat_labels = X
    importances = model.feature_importances_
    feature_importance = pd.DataFrame(
        {"Feature Name": feat_labels.columns,
         "Importance": importances[np.argsort(importances)[::-1]]})
except AttributeError:
    feature_importance = pd.DataFrame()

print(feature_importance)
