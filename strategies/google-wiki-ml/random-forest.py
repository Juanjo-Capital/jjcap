import pandas as pd
from models import df
from models import fit_predict, get_metrics

thresh = 0.3
model = "RF"

results = fit_predict(df, model)
train = results[5]
train_pred_prob = results[4]
train_pred = (train_pred_prob >= thresh).astype(int)
test = results[2]
test_pred_prob = results[1]
test_pred = (test_pred_prob >= thresh).astype(int)

from sklearn.metrics import accuracy_score, precision_score
from sklearn.metrics import recall_score, f1_score

test_scores = [accuracy_score(test, test_pred),
               precision_score(test, test_pred),
               recall_score(test, test_pred),
               f1_score(test, test_pred)]

train_scores = [accuracy_score(train, train_pred),
                precision_score(train, train_pred),
                recall_score(train, train_pred),
                f1_score(train, train_pred)]

print("Test:", test_scores)
print("Train:", train_scores)
