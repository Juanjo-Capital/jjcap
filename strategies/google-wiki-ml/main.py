import pandas as pd
from models import fit_predict, get_metrics

# Import raw data set
df0 = pd.read_excel("aapl.xlsx").iloc[2:, :].reset_index(drop = True)

# Remove the first 14 rows and the last row (we don't have future data in the present)
df0 = df0.iloc[14:-1, :].reset_index(drop = True)
df0["Wiki Move"] = df0["Wiki Move"].astype(int)
df0["Goog ROC"] = df0["Goog ROC"].astype(float)

# Select columns from data set
df = df0[["Open", "Close", "High", "Low", "RS", "Wiki Traffic- 1 Day Lag", "Wiki 5day disparity", "Wiki Move", "Wiki MA3 Move", "Wiki MA5 Move", "Wiki EMA5 Move", "Goog RS", "Goog MA3", "Goog MA5", "Goog EMA5 Move", "Goog 3day Disparity Move", "Goog ROC Move", "Goog RSI Move", "Wiki 3day Disparity", "Price RSI Move", "Google_Move", "Target"]]

features = ["Wiki Traffic- 1 Day Lag", "Wiki 5day disparity", "Wiki Move", "Wiki MA3 Move", "Wiki MA5 Move", "Wiki EMA5 Move", "Goog MA3", "Target"]

df = df[features]

print("Logistic regression ===================================================")
logreg_metrics = get_metrics(fit_predict(df, "LogReg"))
print(logreg_metrics)
print("")
logreg_pred = pd.concat([fit_predict(df, "LogReg")[0], fit_predict(df, "LogReg")[1]], axis = 1)
logreg_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(logreg_pred.head())
print("")

print("XGBoost ===============================================================")
xgb_metrics = get_metrics(fit_predict(df, "XGB"))
print(xgb_metrics)
print("")
xgb_pred = pd.concat([fit_predict(df, "XGB")[0], fit_predict(df, "XGB")[1]], axis = 1)
xgb_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(xgb_pred.head())
print("")

print("Random forest =========================================================")
rf_metrics = get_metrics(fit_predict(df, "RF"))
print(rf_metrics)
print("")
rf_pred = pd.concat([fit_predict(df, "RF")[0], fit_predict(df, "RF")[1]], axis = 1)
rf_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(rf_pred.head())
print("")

print("Decision trees ========================================================")
dt_metrics = get_metrics(fit_predict(df, "DT"))
print(dt_metrics)
print("")
dt_pred = pd.concat([fit_predict(df, "DT")[0], fit_predict(df, "DT")[1]], axis = 1)
dt_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(dt_pred.head())
print("")

print("KNN ===================================================================")
knn_metrics = get_metrics(fit_predict(df, "KNN"))
print(knn_metrics)
print("")
knn_pred = pd.concat([fit_predict(df, "KNN")[0], fit_predict(df, "KNN")[1]], axis = 1)
knn_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(knn_pred.head())
print("")

print("SVM ===================================================================")
svm_metrics = get_metrics(fit_predict(df, "SVM"))
print(svm_metrics)
print("")
svm_pred = pd.concat([fit_predict(df, "SVM")[0], fit_predict(df, "SVM")[1]], axis = 1)
svm_pred.columns = ["Predicted Binary Value", "Predicted Probability"]
print(svm_pred.head())
