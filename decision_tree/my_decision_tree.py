import pandas as pd
from operator import itemgetter


MAX_LEAF_NUM = 3

def top_category_filter(data,cols,pos,catgs):
	top_catg = []
	for i in catgs:
		top_catg.append((i, len(data.loc[data[cols[pos]] == i][cols[pos]])))

	top_catg = sorted(top_catg,key=itemgetter(1),reverse=True)
	top_catg = [x[0] for x in top_catg]
	if len(top_catg)>MAX_LEAF_NUM: top_catg = top_catg[:MAX_LEAF_NUM]
	return top_catg


def dt(data,cols,pos):
	catgs = list(set(data[cols[pos]].values))
	top_catgs = top_category_filter(data,cols,pos,catgs) #取前幾名的葉子
	tree = {}
	if pos != len(cols)-1:
		for i in top_catgs:
			tree[i] = (len(data.loc[data[cols[pos]] == i][cols[pos]]), dt(data.loc[data[cols[pos]] == i],cols,pos+1))
	else:
		for i in top_catgs:
			tree[i] = (len(data.loc[data[cols[pos]] == i][cols[pos]]))
	return tree



if __name__  == "__main__":
	b = pd.read_csv('traffic_accident_dataA1_v0.csv',encoding='utf-8')
	car_type_filter = b['事故類型及型態大類別名稱'] == '車與車'
	b = b.loc[car_type_filter]
	col_filter = ['事故類型及型態大類別名稱','事故類型及型態子類別名稱','事故位置子類別名稱']
	b = b.loc[:,col_filter]
	b = b.reset_index(drop=True)

	result = dt(b,col_filter,0)
	print(result)