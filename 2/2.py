import pandas as pd
import numpy as np
from sklearn.metrics import log_loss

def load_feature_matrix(path):
	df = pd.read_csv(path)
	df["TitleLength"] = df.Title.apply(len)
	return df

def get_score(train, test, model, columns):
    model.fit(X=np.asarray(train[columns]), y = np.asarray(train.OpenStatus).transpose())
    predictions = model.predict_proba(np.asarray(test[columns]))[:,1]
    return log_loss(test.OpenStatus.values, predictions)
