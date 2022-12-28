import pandas as pd
import os



class DecisionTree(object):
	def __init__(self,data):
		self.__data = pd.DataFrame(data)
		self.__categorys= self.__get_category()
		
		
	def __get_category(self):
		_data = self.__data.copy()
		categorys = {}
		for i in _data.keys():
			category_name = list(set(_data[i].values))
			if type(category_name[0]) != str:continue
			categorys[i] = category_name
			# print(category_name,len(category_name))
		return categorys
		

	def data_to_code(self,data):
		for i in data.keys():
			class_name = list(set(data[i].values))
			if type(class_name[0]) != str:continue

			for j in range(len(data[i].values)):
				data.loc[j,i] = class_name.index(data[i][j])
	
		return data






if __name__ == '__main__':
	
	b = [1,2,3]
	b = pd.read_csv('traffic_accident_dataA1_v0.csv',encoding='utf-8')
	car_type_filter = b['事故類型及型態大類別名稱'] == '車與車'
	b = b.loc[car_type_filter]
	col_filter = ['事故類型及型態大類別名稱','事故位置子類別名稱','事故類型及型態子類別名稱']
	b = b.loc[:,col_filter]
	b = b.reset_index(drop=True)
	a = DecisionTree(b)
	a.specific_column_analysis(col_filter)
	
	