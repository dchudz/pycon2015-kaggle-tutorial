import pandas as pd
from dateutil.parser import parse
import json

def get_df_from_raw(path):
	with open('raw/train.json', 'r') as f:
		train_json = json.load(f)
	train_df = pd.DataFrame(train_json)
	train_df[["unix_timestamp_of_request", "unix_timestamp_of_request_utc"]] = train_df[["unix_timestamp_of_request", "unix_timestamp_of_request_utc"]].astype('datetime64[s]')
	return train_df