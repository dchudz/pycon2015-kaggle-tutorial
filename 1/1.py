import pandas as pd

def load_feature_matrix(path):
	df = pd.read_csv(path)
	df["TitleLength"] = df.Title.apply(len)
	return df
