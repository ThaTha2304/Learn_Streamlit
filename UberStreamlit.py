# Create an App
# https://docs.streamlit.io/get-started/tutorials/create-an-app

# Exploring a public Uber dataset for pickups and drop-offs in NYC

# 0. Import Library
import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber pickups in NYC")

# 1. Import Data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
        'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows = nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading Data...')
# Load 10.000 rows of data into the dataframe
data = load_data(10000)
# Notify the reader that the data was succesfully loaded
data_load_state.text('Done!')
# Write the data
st.subheader('Raw Data')
st.write(data)

# 2. Draw a histogram
st.subheader("Number of pickups by hour")

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# 3. Plot data on a map
# Map all time
# st.subheader("Map of all pickups")
# st.map(data)

# Map on certain hour
hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

# 4. Filter results with a slider
# min: 0h, max: 23h, default: 17h
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

# 5. Use a button to toggle data
if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(data)