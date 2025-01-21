import numpy as np
import streamlit as st
import pandas as pd

import plotly.graph_objects as go

# 座標データを保存するリスト
coordinates = []

# タイトルの表示
st.title("タッチ・クリックでスイング座標を入力")

# クリックした座標を取得するための関数
def get_click_coordinates(event):
    x = event['x']
    y = event['y']
    coordinates.append((x, y))  # 座標をリストに追加

# 座標がクリックされるたびに更新
st.markdown("### グラフをクリックして座標を入力してください")
graph = go.Figure()

# 最初のグラフ（空の散布図）
graph.add_trace(go.Scatter(x=[], y=[], mode='markers', marker=dict(color='blue', size=10)))

# ユーザーがクリックした座標を基にプロットを更新
if len(coordinates) > 0:
    x_data = [coord[0] for coord in coordinates]
    y_data = [coord[1] for coord in coordinates]
    
    graph.add_trace(go.Scatter(x=x_data, y=y_data, mode='markers', marker=dict(color='blue', size=10)))

# グラフをStreamlitに表示
st.plotly_chart(graph)

# 座標を表示する
if coordinates:
    st.write("現在の入力座標:")
    st.write(coordinates)