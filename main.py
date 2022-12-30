#-*- coding: UTF-8 -*-
import folium
import pandas as pd
import numpy as np
from sklearn import cluster

COLOR = ["red",
"green",
"blue",
"darkred",
"lightred",
"orange",
"beige",
"darkgreen",
"lightgreen",
"darkblue",
"cadetblue",
"lightblue",
"purple",
"darkpurple",
"pink",
"white",
"gray",
"lightgray",
"black"]

data = pd.read_csv('kaohsiung_a1a2_accidents_data.csv',encoding='utf-8')

class Accident:
	def __init__(self, lng, lat, age, addr, rt, cau, car, acc_type, cat=None):
		self.lng = lng
		self.lat = lat
		self.age = age
		self.addr = addr
		self.rt = rt
		self.cau = cau
		self.car = car
		self.acc_type = acc_type
		self.cat = cat


#使用欄位：(1)道路型態子類別名稱 (2)肇因研判子類別名稱-主要 (3)當事者區分-類別-大類別名稱-車種 (4)事故類別名稱
road_type = data['道路型態大類別名稱'].values
cause_main = data['肇因研判子類別名稱-主要'].values
car_type = data['當事者區分-類別-大類別名稱-車種'].values
accident_type = data['事故類別名稱'].values

lngs = data['經度'].values
lats = data['緯度'].values
ages = data['當事者事故發生時年齡'].values
cities = data['發生地點'].values

def data_process(d):
	_data = d.copy()
	cat = list(set(_data))
	print(cat)
	for i in range(len(_data)):
		_data[i] = cat.index(_data[i])
	print(_data)
	return _data

def age_process(ages):
	for i in range(len(ages)):
		if ages[i]<30:
			ages[i] = 0
		elif ages[i]<60:
			ages[i] = 1
		else:
			ages[i] = 2

	return ages

def normalization(d):
	_range = np.max(d)-np.min(d)
	return (d-np.min(d))/_range

road_type_data = data_process(road_type)
cause_main_data = data_process(cause_main)
car_type_data = data_process(car_type)
accident_type_data = data_process(accident_type)

road_type_data = normalization(road_type_data)
cause_main_data = normalization(cause_main_data)
car_type_data = normalization(car_type_data)

ages = age_process(ages)
print(ages)
print(f'29歲以下：{ages.tolist().count(0)}')
print(f'30~59歲：{ages.tolist().count(1)}')
print(f'60歲以上：{ages.tolist().count(2)}')

accidents = []
for _rt, _cau, _car, _acc, _lng, _lat, _age, _city in zip(road_type, cause_main, car_type, accident_type, lngs, lats, ages, cities):
	accidents.append(Accident(_lng, _lat, _age, _city, _rt, _cau, _car, _acc))

# locations = np.vstack([lats, lngs, ages]).T
# _ages = np.expand_dims(ages, axis=1)


input_data = np.vstack([road_type_data, car_type_data, accident_type_data]).T
kmeans_res = cluster.KMeans(n_clusters = 4, random_state=0).fit(input_data)
# # kmeans_res = cluster.DBSCAN(eps=0.3, min_samples=14).fit(locarions)

for accident, category in zip(accidents, kmeans_res.labels_):
	accident.cat = category
	
age0_accidents = list(filter(lambda x: x.age==0, accidents))
age1_accidents = list(filter(lambda x: x.age==1, accidents))
age2_accidents = list(filter(lambda x: x.age==2, accidents))

def print_cluster(_accidents:list, age_type):
	cats = list(map(lambda x: x.cat, _accidents))
	names = sorted(list(set(cats)))
	for i in names:
		if age_type == 0:
			print(f'29以下，群{i}：{cats.count(i)}')
		elif age_type == 1:
			print(f'30~59，群{i}：{cats.count(i)}')
		elif age_type == 2:
			print(f'60以上，群{i}：{cats.count(i)}')
		else:
			print('ERROR:A')

print_cluster(age0_accidents, 0)
print_cluster(age1_accidents, 1)
print_cluster(age2_accidents, 2)

for i in accidents:
	if i.cat==3:
		print(f'道路型態：{i.rt}  車種：{i.car}  事故類型：{i.acc_type}  群：{i.cat}')

result = pd.DataFrame({'年齡層':list(map(lambda x: x.age, accidents)), '道路型態':list(map(lambda x: x.rt, accidents)), '車種':list(map(lambda x: x.car, accidents)), '事故型態':list(map(lambda x: x.acc_type, accidents)), '群':list(map(lambda x: x.cat, accidents))})
result.to_csv('result.csv', encoding='utf-8')
fmap0 = folium.Map(location=[22.65264,120.3275], zoom_start=14)
fmap1 = folium.Map(location=[22.65264,120.3275], zoom_start=14)
fmap2 = folium.Map(location=[22.65264,120.3275], zoom_start=14)
fmap_all = folium.Map(location=[22.65264,120.3275], zoom_start=14)
for lat, lng, age, label in zip(lats,lngs,ages,kmeans_res.labels_):
	if age == 0:
		fmap0.add_child(folium.Marker(location=[lat,lng], icon = folium.Icon(color=COLOR[label+4])))
	elif age == 1:
		fmap1.add_child(folium.Marker(location=[lat,lng], icon = folium.Icon(color=COLOR[label+4])))
	else:
		fmap2.add_child(folium.Marker(location=[lat,lng], icon = folium.Icon(color=COLOR[label+4])))
	fmap_all.add_child(folium.Marker(location=[lat,lng], icon = folium.Icon(color=COLOR[label+4])))


fmap_all.save('map_all.html')
fmap0.save('map0.html')
fmap1.save('map1.html')
fmap2.save('map2.html')


