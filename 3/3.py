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

def expand_with_bow_features(train, test, column, max_features = 200):
	vectorizer = CountVectorizer(max_features=max_features)
	train_matrix = vectorizer.fit_transform(train[column]).todense()
	col_names = [column + x for x in list(vectorizer.vocabulary_.keys())]
	train = train.join(pd.DataFrame(train_matrix, index=train.index, columns = col_names))
	test_matrix  = vectorizer.transform(test[column]).todense()
	test = test.join(pd.DataFrame(test_matrix, index=test.index, columns = col_names))
	return train, test, col_names
