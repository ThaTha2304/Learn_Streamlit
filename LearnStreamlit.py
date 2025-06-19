"""
    Learn Streamlit, from docs.streamlit.io
"""

# 0. Import library
import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. Use Magic

# Teks kek gini langsung muncul, format mengikuti markdown (I guess?)
"""
    # My First App
    Here's our first attempt at using data to create a table
"""

## Add the data
df = pd.DataFrame({
    'first_column' : [1,2,3,4],
    'second_column' : [10,20,30,40] 
})

## Write the data
df

# 2. Write a data frame (using st.write())
## Display table using st.write()
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first_col': [1,2,3,4],
    'second_col' : [10,20,30,40]
}))
'''
    Tabel langsung keluar, tanpa harus dipanggil dulu si tabelnya
'''

## Contoh daataframe, digabung ama numpy
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)
'''Tabel langsung keluar, berisi 10 baris, 20 kolom angka random'''

## Format using Pandas Styler Object
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))
'''
    Baris dengan nilai tertinggi di tiap kolom akan berwarna kuning
'''

## Buat nampilin tabel statis
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))
)
st.table(dataframe)
'''
    Akan muncul tabel statis, tidak interaktif
'''

# 3. Draw Charts and Maps
## Generate random data using numpy
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

## Plot a map
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)

# 4. Widgets
## Slider, Button, Select Box
x = st.slider('x')
st.write(x, 'squared is', x*x)

y = st.button("Lalala")
st.write(y)

z = st.selectbox("Select Box", ("Ya", "Tidak"))
st.write("You Select: ", z)

## By Key
st.text_input("Your name", key="name")
st.session_state.name

## Use checkboxes
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a', 'b', 'c']
    )
    chart_data

## Use a selectbox for options
df = pd.DataFrame({
    'first_col' : [1,2,3,4],
    'second_col' : [10,20,30,40]
})

option = st.selectbox(
    "Which number do you like best?",
    df['second_col']
)
"You selected: ", option

# 5. Layout

## Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home Phone", "Mobile Phone")
)

## Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
## Put button on the left_column
left_column.button("Press me!")

with right_column:
    chosen = st.radio(
        "Sorting hat",
        ("a", "b", "c", "d")
    )
    st.write(f"You chose {chosen}!")

## Show Progress
'Starting a long computation..'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'... done'