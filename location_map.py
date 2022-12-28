import folium
import pandas as pd
import numpy as np
from sklearn import cluster


data = pd.read_csv('NPA_TMA1-2.csv',encoding='utf-8')

class Accident:
	def __init__(self, lng, lat, age, addr):
		self.lng = lng
		self.lat = lat
		self.age = age
		self.addr = addr


lngs = data['經度'].values
lats = data['緯度'].values
ages = data['當事者事故發生時年齡'].values
cities = data['發生地點'].values

# accidents = []
# for i in data.loc[:].values:
# 	print(i)
	

locations = np.vstack([lats, lngs]).T


kmeans_res = cluster.KMeans(n_clusters = 4).fit(locations)
print(kmeans_res.labels_)

COLOR = ["red",
"darkred",
"lightred",
"orange",
"beige",
"green",
"darkgreen",
"lightgreen",
"blue",
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

fmap = folium.Map(location=[23.6864,120.4114], zoom_start=10)
for lat, lng, label, city in zip(lats,lngs,kmeans_res.labels_,cities):
	if not '高雄' in city: continue
	fmap.add_child(folium.Marker(location=[lat,lng], icon = folium.Icon(color=COLOR[label])))

fmap.save('map.html')

