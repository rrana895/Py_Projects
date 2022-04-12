import urllib.request
import pandas as pd

url = "https://en.wikipedia.org/wiki/Forbes%27_list_of_the_world%27s_highest-paid_athletes"

with urllib.request.urlopen(url) as i:
    html = i.read()
    
data = pd.read_html(html)[0]
print(data.head())

data.to_csv("athles.csv")