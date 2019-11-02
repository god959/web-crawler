import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

#創餐點資料夾
dn = 'Starbucks2'
os.makedirs(dn)

#抓取所有Starbucks餐點營養資訊
for i in range(1,999):
    print("目前第幾個表格?", i)
    try:
        #讀網頁
        r = urlopen('https://www.starbucks.com.tw/products/food/product.jspx?id='+str(i))
        rl = BeautifulSoup(r)
        #讀表格
        df = pd.read_html("https://www.starbucks.com.tw/products/food/product.jspx?id="+str(i))
        #行列轉置
        df1 = df[0].T
        # 讓第一列當欄位名
        df1.columns = df1.iloc[0]
        # 刪除第一列
        df1.drop([0],inplace=True)
        # 刪除第一列
        df2 = df1.drop('價格',axis=1)
        # 搜尋食物名
        fn = rl.find("h1", class_="title_cn")
        # 新增欄位
        df2['食物名'], df2['品牌'], df2['資料來源'], df2['更新時間'], df2['食用量'] = [fn.text, 'Starbucks',
                                                                             'https://www.starbucks.com.tw/home/index.jspx',
                                                                             '20190923', '一份']
        # 存成csv檔
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\Starbucks2\Sf" + str(i) + "_"  + ".csv"
                   , encoding="utf-8", index=False)

    except:
        print("應該是沒表格了吧")
        pass
    i += 1

