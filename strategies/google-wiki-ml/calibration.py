import pandas as pd
from models import df
from models import fit_predict, get_metrics

rows = 20

"""
print("Logistic regression ===================================================")
logreg_pred = pd.concat([fit_predict(df, "LogReg")[0], fit_predict(df, "LogReg")[1]], axis = 1)
logreg_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(logreg_pred.head(50))
print("")

logreg_pred_class = pd.DataFrame()
logreg_pred_class["Predicted Binary Value"] = logreg_pred["Predicted Binary Value"]
logreg_pred_class["Predicted Probability"] = logreg_pred["Predicted Probability"] > 0.7

print(logreg_pred_class.head(50))

print("XGBoost ===============================================================")
xgb_pred = pd.concat([fit_predict(df, "XGB")[0], fit_predict(df, "XGB")[1]], axis = 1)
xgb_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(xgb_pred.head(rows))
print("")
"""

print("Random forest =========================================================")
rf_pred = pd.concat([fit_predict(df, "RF")[0], fit_predict(df, "RF")[1]], axis = 1)
rf_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(rf_pred.head(rows))
print("")

rf_pred_class = pd.DataFrame()
rf_pred_class["Predicted Binary Value"] = rf_pred["Predicted Binary Value"]
rf_pred_class["Predicted Probability"] = (rf_pred["Predicted Probability"] > 0.1).astype(int)

train = fit_predict(df, "RF")[5]
train_pred = fit_predict(df, "RF")[3]
test = fit_predict(df, "RF")[2]
test_pred = rf_pred_class["Predicted Probability"]

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print(rf_pred_class.head(50))
print([accuracy_score(test, test_pred), precision_score(test, test_pred), recall_score(test, test_pred), f1_score(test, test_pred)])
print([accuracy_score(train, train_pred), precision_score(train, train_pred), recall_score(train, train_pred), f1_score(train, train_pred)])
"""
print("Decision trees ========================================================")
dt_pred = pd.concat([fit_predict(df, "DT")[0], fit_predict(df, "DT")[1]], axis = 1)
dt_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(dt_pred.head(rows))
print("")

print("KNN ===================================================================")
knn_pred = pd.concat([fit_predict(df, "KNN")[0], fit_predict(df, "KNN")[1]], axis = 1)
knn_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(knn_pred.head(rows))
print("")

print("SVM ===================================================================")
svm_pred = pd.concat([fit_predict(df, "SVM")[0], fit_predict(df, "SVM")[1]], axis = 1)
svm_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(svm_pred.head(rows))
"""
