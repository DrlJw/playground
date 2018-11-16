import tushare as ts
import numpy as np

# 1
df = ts.get_hist_data('600036', start = '2018-01-01', end = '2018-06-30')
df.drop(df.iloc[:, 5:], axis = 1, inplace = True)   # 删除第5列及后面的列
df.sort_index(inplace = True)   # 按date列进行排序
# 2
min_day = df.sort_values('volume').iloc[0,]
min_volume = min_day.volume
min_volume_date = min_day.name
print("the min volume of {} is at {}".format(min_volume, min_volume_date))
max_day = df.sort_values('volume').iloc[-1,]
max_volume = max_day.volume
max_volume_date = max_day.name
print("the max volume of {} is at {}".format(max_volume, max_volume_date))
# 3
print(df[df.volume >= 1000000])
# 4
print(len(df[df.close > df.open]))
# 5
print(df.open.diff())
print(np.sign(np.diff(df.open)))
# 6
lst = []
for item in df.index:
    lst.append(item[5:7])
df['month'] = lst
print(df.groupby('month').close.apply(np.mean))