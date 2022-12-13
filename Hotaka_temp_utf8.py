import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
 
#CSVファイルをANSI形式で読み込む
# data = pd.read_csv('Hotaka_temp_201801_202201_utf8.csv',encoding = 'ANSI',skiprows=[0])
data = pd.read_csv('Hotaka_temp_utf8.csv',skiprows=[0])
print(data)

# グラフに出力
data.plot()
plt.title('2018年～2022年2月の穂高の気温')
plt.xlabel('日付(日)')
plt.ylabel('気温(℃)')

# グラフをpngに保存
plt.savefig("hotaka_temp_utf801.png")

plt.show()