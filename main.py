import pandas as pd
import json

url = r"" # enter json file url here
f=open(url)
data=json.load(f)
f.close
df=pd.read_json(data)
print(df)
path=r"" # enter path of where you want your csv file saved here
df.to_csv(path, index=False)