import numpy as np
import pandas as pd
import folium
import warnings

warnings.filterwarnings(action='ignore')
from folium.features import CustomIcon

오름 = pd.read_csv('o.csv', encoding='cp949')

m = folium.Map(
    location = [33.3684955195788, 126.52918183373025],
    zoom_start = 10
)

tooltip = 'Click!!'

주차장유 = folium.FeatureGroup(name='주차장유').add_to(m)
주차장무 = folium.FeatureGroup(name='주차장무').add_to(m)


for i in range(오름.shape[0]):
    if 오름.iloc[i]["주차장"] == 'Y':
        folium.Marker(
            [오름.iloc[i]['위도'], 오름.iloc[i]['경도']],
            popup = f'<div style="width:100px"><strong>{오름.iloc[i]["오름명"]}</strong><br>\
            주차장 : {오름.iloc[i]["주차장"]}<br>\
            화장실 : {오름.iloc[i]["화장실"]}<br>',
            tooltip = tooltip
        ).add_to(주차장유)
    else:
        folium.Marker(
            [오름.iloc[i]['위도'], 오름.iloc[i]['경도']],
            popup = f'<div style="width:100px"><strong>{오름.iloc[i]["오름명"]}</strong><br>\
            주차장 : {오름.iloc[i]["주차장"]}<br>\
            화장실 : {오름.iloc[i]["화장실"]}<br>',
            tooltip = tooltip
        ).add_to(주차장무)

folium.LayerControl(collapsed=False).add_to(m)
m