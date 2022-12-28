# -*- coding: UTF-8 -*-
import pandas as pd

# 資料前處理
df = pd.read_csv('NPA_TMA1-2.csv',encoding='utf-8')
party_filter = df['當事者順位'] == 1
data = df[party_filter]
road_filter = data['道路類別-第1當事者-名稱'] != '國道'
data = data[road_filter]

data = data.drop(['發生年度','發生月份','發生日期','發生時間','事故類別名稱','處理單位名稱警局層','經度','緯度'],axis=1)
data.to_csv('traffic_accident_dataA1_v0.csv',index=False)





if __name__ == '__main__':
	pass