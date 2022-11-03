import requests
import pandas as pd

res = requests.get('https://clock.eng-astra.com.tw/clock-system.php')
df = pd.read_html(res.text)

print(df)
