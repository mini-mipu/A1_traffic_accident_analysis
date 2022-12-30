import os
import pandas as pd
from functools import reduce

#merge A1, A2. accidents that only happened in Sanmin, Kaohsiung 
def merge_table(data:list):
	new_data = reduce(lambda x,y: x.merge(y,how='outer'), data)
	return new_data

A2_files = os.listdir('A2_data')[:]
tables = []
for a in A2_files:
	tables.append(pd.read_csv(f'A2_data/{a}', sep=',', encoding='utf-8'))
tables.append(pd.read_csv('NPA_TMA1-2.csv', sep=',', encoding='utf-8'))
a1a2_accidents_data = merge_table(tables)
a1a2_accidents_data = a1a2_accidents_data.loc[a1a2_accidents_data['發生地點'].str.contains('高雄市三民區')]
a1a2_accidents_data = a1a2_accidents_data.loc[a1a2_accidents_data['當事者順位']==1]
a1a2_accidents_data.to_csv('kaohsiung_a1a2_accidents_data.csv', index=False, encoding='utf-8')