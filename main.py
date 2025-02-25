import pandas as pd
import streamlit as st
import plotly.express as px
import dotenv

file_path = dotenv.get_key('.env', 'FILE_PATH')

df = pd.read_csv(file_path)

title = st.title('Index of Happiness')
x_axis_name = st.selectbox('Select data for X-axis', ['gdp', 'life_expectancy', 'generosity', 'happiness'])
y_axis_name = st.selectbox('Select data for Y-axis', ['gdp', 'life_expectancy', 'generosity', 'happiness'])


def format_column_names(col_name):
    name = col_name.replace("_", " ").title()
    return name


st.subheader(f"{format_column_names(x_axis_name)} and {format_column_names(y_axis_name)}")

cell_value_for_x = df[x_axis_name]
cell_value_for_y = df[y_axis_name]

figure = px.scatter(x=cell_value_for_x, y=cell_value_for_y, labels={'x': x_axis_name, 'y': y_axis_name},
                    hover_name=df['country'])

st.plotly_chart(figure)
