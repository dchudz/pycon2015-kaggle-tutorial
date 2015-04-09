import pandas as pd 
from sklearn.metrics import log_loss
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

# def expand_with_bow_features(train, test, max_features = 100):
# 	title_vectorizer = CountVectorizer(max_features=max_features)
# 	title_vectorizer_fitted = title_vectorizer.fit(train["Title"])
# 	col_names = ["Title\n" + x for x in list(title_vectorizer.vocabulary_.keys())]
# 	title_bow_train = title_vectorizer_fitted.transform(train["Title"]).todense()
# 	title_bow_train_df = pd.DataFrame(title_bow_train, index=train.index, columns = col_names)
# 	title_bow_test  = title_vectorizer_fitted.transform(test["Title"]).todense()
# 	title_bow_test_df = pd.DataFrame(title_bow_test, index=test.index, columns = col_names)
# 	return train.join(title_bow_train_df), test.join(title_bow_test_df), list(title_bow_train_df.columns)

from sklearn.feature_extraction.text import CountVectorizer
def expand_with_bow_features(train, test, columns_to_expand, max_features = 200):
	new_columns = []
	for column in columns_to_expand:
		vectorizer = CountVectorizer(max_features=max_features)
		vectorizer_fitted = vectorizer.fit(train[column])
		col_names = [column + x for x in list(vectorizer_fitted.vocabulary_.keys())]
		train_matrix = vectorizer_fitted.transform(train[column]).todense()
		train = train.join(pd.DataFrame(train_matrix, index=train.index, columns = col_names))
		test_matrix  = vectorizer_fitted.transform(test[column]).todense()
		test = test.join(pd.DataFrame(test_matrix, index=test.index, columns = col_names))
		new_columns += col_names
	return train, test, new_columns

def load_feature_matrix(path):
	df = pd.read_csv(path)
	df["BodyMarkdownLength"] = df.BodyMarkdown.apply(len)
	df["BodyMarkdownLengthCapped"] = df.BodyMarkdownLength.clip_upper(5000)
	df["TitleLength"] = df.Title.apply(len)
	return df

def make_logistic_submission(train, test):
	lr = LogisticRegression()
	result = lr.fit(X=np.asarray(train[["BodyMarkdownLengthCapped"]]), y = np.asarray(train.OpenStatus).transpose())
	predictions = result.predict_proba(np.asarray(test[["BodyMarkdownLength"]]))[:,1]
	submission = pd.DataFrame({"id": test.PostId, "OpenStatus": predictions})
	return submission


def make_constant_submission(train, test):
    train.OpenStatus.mean()
    return pd.DataFrame({"id": test.PostId, "OpenStatus": train.OpenStatus.mean()})


import statsmodels.api as sm
def make_logistic_submission_statsmodels(train, test):
	logit = sm.Logit(exog = train.BodyMarkdownLengthCapped, endog = train.OpenStatus)
	result = logit.fit()
	predictions = result.predict(exog = test.BodyMarkdownLength)
	submission = pd.DataFrame({"id": test.PostId, "OpenStatus": predictions})
	return submission

def get_score(train, test, submission_creator):
	submission = submission_creator(train, test)
	return log_loss(test.OpenStatus.values, submission.OpenStatus.values)

def plot_counter(counter, max_items=10):
    data = [(k,counter[k]) for k in counter]
    data = sorted(data, key=lambda x: x[1], reverse=True)[:max_items]
    ax = plt.axes()
    ax.bar(range(len(data)), [x[1] for x in data])
    ax.set_xticks(np.array(range(len(data)))+0.4)
    labels = [x[0] for x in data]
    ax.set_xticklabels(labels);


def make_submitter(columns, model, train, test):
    result = model.fit(X=np.asarray(train[columns]), y = np.asarray(train.OpenStatus).transpose())
    predictions = result.predict_proba(np.asarray(test[columns]))[:,1]
    submission = pd.DataFrame({"id": test.PostId, "OpenStatus": predictions})
    return submission
