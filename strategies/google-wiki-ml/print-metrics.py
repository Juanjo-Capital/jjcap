import pandas as pd
from models import df
from models import fit_predict, get_metrics

print("Logistic regression ===================================================")
logreg_metrics = get_metrics(fit_predict(df, "LogReg"))
print(logreg_metrics)
print("")

print("XGBoost ===============================================================")
xgb_metrics = get_metrics(fit_predict(df, "XGB"))
print(xgb_metrics)
print("")

print("Random forest =========================================================")
rf_metrics = get_metrics(fit_predict(df, "RF"))
print(rf_metrics)
print("")

print("Decision trees ========================================================")
dt_metrics = get_metrics(fit_predict(df, "DT"))
print(dt_metrics)
print("")

print("KNN ===================================================================")
knn_metrics = get_metrics(fit_predict(df, "KNN"))
print(knn_metrics)
print("")

print("SVM ===================================================================")
svm_metrics = get_metrics(fit_predict(df, "SVM"))
print(svm_metrics)
print("")
