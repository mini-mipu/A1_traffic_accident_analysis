import pandas as pd


df = pd.read_csv('traffic_accident_data_v1.csv',encoding='utf-8')
for i in df.keys().values:
	for inx,_ in enumerate(df[i]):
		df.loc[inx,i] = i+'_'+str(df.loc[inx,i])

df.to_csv('traffic_accident_data_v1.1.csv',index=False,encoding='utf-8')
print(df.head())