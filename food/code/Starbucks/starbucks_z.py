import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

#創餐點資料夾
dn = 'Starbucks1'
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
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\Starbucks1\Sf" + str(i) + "_"  + ".csv"
                   , encoding="utf-8", index=False)

    except:
        print("應該是沒表格了吧")
        pass
    i += 1

#創飲料資料夾
dn = 'Starbucks2'
os.makedirs(dn)

#抓取所有Starbucks飲料營養資訊
i=1
for i in range(1,999):
    print("目前第幾頁?", i)
    try:
        r = urlopen('https://www.starbucks.com.tw/products/drinks/product.jspx?id='+str(i))
        rl = BeautifulSoup(r)
        df = pd.read_html("https://www.starbucks.com.tw/products/drinks/product.jspx?id="+str(i))
        j=0
        for j in range(0,4):
            print("目前第幾個表格?", j)
            try:
                df1 = df[j].T
                df1.columns = df1.iloc[j]
                df1.drop([j],inplace=True)
                df2 = df1.drop(['價格', '咖啡因含量'],axis=1)
                fn = rl.find("h1", class_="title_cn")
                df2['食物名'], df2['品牌'], df2['資料來源'], df2['更新時間'], df2['食用量'] = [fn.text, 'Starbucks',
                                                                                     'https://www.starbucks.com.tw/home/index.jspx',
                                                                                     '20190923', '一份']
                df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\Starbucks2\Starbucks" + str(i) + "_" + str(j + 1) + ".csv"
                           , encoding="utf-8", index=False)
            except ValueError:
                print("應該是沒表格了吧")
            j += 1
    except:
        print("應該是沒頁數了吧")
        pass
    i += 1

