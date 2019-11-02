import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import os

#創早餐資料夾
dn = 'Breakfast_detail_1'
os.makedirs(dn)

#抓取早餐食物資訊
for i in range(1,10):
    print('目前第幾個食物', i)
    try:
        #讀網頁
        r = urlopen('http://www.mos.com.tw/menu/breakfast_detail.aspx?id=M00' + str(i))
        rl = BeautifulSoup(r)
        #讀表格
        df = pd.read_html("http://www.mos.com.tw/menu/breakfast_detail.aspx?id=M00"+ str(i), encoding="utf-8")
        #行列轉置
        df1 = df[0].T
        #讓第一列當欄位名
        df1.columns = df1.iloc[0]
        #刪除第一列
        df1.drop([0],inplace=True)
        #搜尋食物名
        fn = rl.find("span", id="mainContent_lblName")
        #新增欄位
        df1['食物名'],df1['品牌'], df1['資料來源'], df1['更新時間'],df1['食用量'] = [fn.text,'MOS BURGER', 'http://www.mos.com.tw/index.aspx', '20190101','一份']
        #排序欄位
        df2 = df1[['品牌','食物名','食用量', '熱量', '蛋白質','脂肪','飽和脂肪','反式脂肪' ,'鈉', '碳水化合物','資料來源','更新時間' ]]
        #存成csv檔
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\Breakfast_detail\MOS_" +"breakfast_detail"+ str(i)  + ".csv", encoding="utf-8", index=False)
        print('表格出現了')
    except ValueError:
        pass
    i+=1

for (i) in range(10,100):
    print('目前第幾個食物', i)
    try:
        r = urlopen('http://www.mos.com.tw/menu/breakfast_detail.aspx?id=M0'+ str(i))
        rl = BeautifulSoup(r)
        df = pd.read_html("http://www.mos.com.tw/menu/breakfast_detail.aspx?id=M0" + str(i), encoding="utf-8")
        df1 = df[0].T
        df1.columns = df1.iloc[0]
        df1.drop([0], inplace=True)
        fn = rl.find("span", id="mainContent_lblName")
        df1['食物名'], df1['品牌'], df1['資料來源'], df1['更新時間'], df1['食用量'] = [fn.text, 'MOS BURGER',
                                                                       'http://www.mos.com.tw/index.aspx',
                                                                       '20190101', '一份']
        df2 = df1[['品牌', '食物名', '食用量', '熱量', '蛋白質', '脂肪','飽和脂肪', '反式脂肪', '鈉', '碳水化合物', '資料來源', '更新時間']]
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\Breakfast_detail_1\MOS_" +"breakfast_detail" + str(i) + ".csv", encoding="utf-8", index=False)
        print('表格出現了')
    except :
        pass
    i += 1

time.sleep(2)
for i in range(100,1000):
    print('目前第幾個食物', i)
    try:
        r = urlopen('http://www.mos.com.tw/menu/breakfast_detail.aspx?id=M' + str(i))
        rl = BeautifulSoup(r)
        df = pd.read_html("http://www.mos.com.tw/menu/breakfast_detail.aspx?id=M"+ str(i), encoding="utf-8")
        df1 = df[0].T
        df1.columns = df1.iloc[0]
        df1.drop([0],inplace=True)
        fn = rl.find("span", id="mainContent_lblName")
        df1['食物名'],df1['品牌'], df1['資料來源'], df1['更新時間'],df1['食用量'] = [fn.text,'MOS BURGER', 'http://www.mos.com.tw/index.aspx', '20190101','一份']
        df2 = df1[['品牌','食物名','食用量', '熱量', '蛋白質','脂肪','飽和脂肪','反式脂肪' ,'鈉', '碳水化合物','資料來源','更新時間' ]]
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\Breakfast_detail\MOS_" +"breakfast_detail" + str(i)  + ".csv", encoding="utf-8", index=False)
        print('表格出現了')
    except ValueError:
        pass
    i+=1







