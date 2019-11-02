import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup


list1=['set_detail','breakfast_detail']
for i in list1:
    for j in range(10,100):
        print('目前第幾個食物', j)
        try:
            r = urlopen('http://www.mos.com.tw/menu/'+i+'.aspx?id=M0'+ str(j))
            rl = BeautifulSoup(r)
            df = pd.read_html("http://www.mos.com.tw/menu/set_detail.aspx?id=M0" + str(j), encoding="utf-8")
            df1 = df[0].T
            df1.columns = df1.iloc[0]
            df1.drop([0], inplace=True)
            df2 = df1.drop(['飽和脂肪', '反式脂肪', '鈉'], axis=1)
            fn = rl.find("span", id="mainContent_lblName")
            df2['食物名'], df2['品牌'], df2['資料來源'], df2['更新時間'], df2['食用量'] = [fn.text, 'MOS BURGER',
                                                                           'http://www.mos.com.tw/index.aspx',
                                                                           '20190101', '一份']
            df3 = df2[['品牌', '食物名', '食用量', '熱量', '蛋白質', '脂肪', '碳水化合物', '資料來源', '更新時間']]
            df3.to_csv("MOS_" + i + '_' + str(j) + ".csv", encoding="utf-8", index=False)
            print('表格出現了')
        except :
            pass
        j += 1







