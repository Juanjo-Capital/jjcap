import pandas as pd
from numpy import loadtxt
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
from sklearn.linear_model import LogisticRegression
from xgboost import plot_importance
from xgboost import plot_tree
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import confusion_matrix, classification_report

def fit_predict(df, m):
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

    if m == "LogReg":
        model = LogisticRegression(random_state = 0)
    elif m == "XGB":
        model = XGBClassifier()
    elif m == "RF":
        model = RandomForestClassifier(n_estimators=200)
    elif m == "DT":    
        model = DecisionTreeClassifier(criterion="entropy", max_depth=20)
    elif m == "KNN":
        model = KNeighborsClassifier(n_neighbors=200)
    elif m == "SVM":
        model = SVC(C=1.0,gamma=0.00001)
    
    model.fit(X_train, Y_train)
    
    Y_test_pred = pd.Series(model.predict(X_test)).astype(int)
    Y_train_pred = pd.Series(model.predict(X_train)).astype(int)
    
    # Calibrated classifier
    model_c = CalibratedClassifierCV(model, method='sigmoid', cv="prefit")
    model_c.fit(X_train, Y_train)
    Y_test_pred_prob = pd.Series(model_c.predict_proba(X_test)[:, 1])
    Y_train_pred_prob = model_c.predict_proba(X_train)[:, 1]
    
    return [Y_test_pred, Y_test_pred_prob, Y_test, Y_train_pred, Y_train_pred_prob, Y_train]

# Test set metrics
def get_metrics(results):
    test = results[2]
    test_pred = results[0]
    train = results[5]
    train_pred = results[3]
    
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    labels = ["Accuracy", "Precision", "Recall", "F1 Score"]
    test_scores = [accuracy_score(test, test_pred), precision_score(test, test_pred), recall_score(test, test_pred), f1_score(test, test_pred)]
    train_scores = [accuracy_score(train, train_pred), precision_score(train, train_pred), recall_score(train, train_pred), f1_score(train, train_pred)]
    
    metrics = pd.DataFrame()
    metrics["Index"] = labels
    metrics["Test Score"] = test_scores
    metrics["Train Score"] = train_scores
    metrics = metrics.set_index("Index")
    return metrics
