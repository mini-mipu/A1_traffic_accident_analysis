import pandas as pd

def single_column_analysis():
	data = pd.read_csv('traffic_accident_dataA1_v0.csv',encoding='utf-8')
	DATA_NUM = len(data)

	wf = open('single_column_analysis_result.txt','w',encoding='utf-8')
	for key in data.keys():
		category_names = list(set(data[key].values))
		category_results = []
		for name in category_names:
			cls_num = data[key].values.tolist().count(name)
			print(key,name,cls_num)
			proportion = round(cls_num/DATA_NUM,2)*100
			category_results.append([name,cls_num,proportion])

			
		category_results.sort(key = lambda s: s[1],reverse=True)
		for res in category_results:
			wf.write(f'{key}  {res[0]}  {res[1]}  {res[2]}%\n')
			

	wf.close()


def specific_column_analysis():
	data = pd.read_csv('traffic_accident_dataA1_v0.csv',encoding='utf-8')
	sp_filter = (data['事故類型及型態大類別名稱'] == '車與車')&(data['事故類型及型態子類別名稱'] == '其他')
	data = data[sp_filter]
	DATA_NUM = len(data)

	wf = open('car_car_othertype_analysis_result.txt','w',encoding='utf-8')
	for key in data.keys():
		category_names = list(set(data[key].values))
		category_results = []
		for name in category_names:
			cls_num = data[key].values.tolist().count(name)
			print(key,name,cls_num)
			proportion = round(cls_num/DATA_NUM*100,2)
			category_results.append([name,cls_num,proportion])

			
		category_results.sort(key = lambda s: s[1],reverse=True)
		for res in category_results:
			wf.write(f'{key}  {res[0]}  {res[1]}  {res[2]}%\n')
			

	wf.close()


if __name__ == '__main__':
	specific_column_analysis()