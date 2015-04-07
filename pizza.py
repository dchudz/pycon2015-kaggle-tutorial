import pandas as pd
from dateutil.parser import parse
import json

def get_df_from_raw(path):
	with open(path, 'r') as f:
		data_json = json.load(f)
	df = pd.DataFrame(data_json)
	df[["unix_timestamp_of_request", "unix_timestamp_of_request_utc"]] = df[["unix_timestamp_of_request", "unix_timestamp_of_request_utc"]].astype('datetime64[s]')
	return df