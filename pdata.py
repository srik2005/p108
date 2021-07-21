import random
import plotly.express as px
import plotly.figure_factory as ff
import csv
import pandas as pd


df = pd.read_csv('pdatacsv.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()],['Average Ratings Of Smartphones 2021'],show_hist = False)
fig.show()