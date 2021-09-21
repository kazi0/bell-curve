import pandas as pd
import plotly.figure_factory as ff


df = pd.read_csv("data.csv")
data = df["Avg Rating"].tolist()

a = ff.create_distplot([data], ["Avg Rating for smartphones"], show_hist= True)
a.show()