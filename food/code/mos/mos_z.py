import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import os

#創早餐資料夾
dn = 'Breakfast_detail'
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
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\Breakfast_detail\MOS_" +"breakfast_detail" + str(i) + ".csv", encoding="utf-8", index=False)
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

#創主餐資料夾
dn = 'set_detail'
os.makedirs(dn)

#抓取主餐食物資訊
for i in range(1,10):
    print('目前第幾個食物', i)
    try:
        r = urlopen('http://www.mos.com.tw/menu/set_detail.aspx?id=M00' + str(i))
        rl = BeautifulSoup(r)
        df = pd.read_html("http://www.mos.com.tw/menu/set_detail.aspx?id=M00"+ str(i), encoding="utf-8")
        df1 = df[0].T
        df1.columns = df1.iloc[0]
        df1.drop([0],inplace=True)
        fn = rl.find("span", id="mainContent_lblName")
        df1['食物名'],df1['品牌'], df1['資料來源'], df1['更新時間'],df1['食用量'] = [fn.text,'MOS BURGER', 'http://www.mos.com.tw/index.aspx', '20190101','一份']
        df2 = df1[['品牌','食物名','食用量', '熱量', '蛋白質','脂肪','飽和脂肪','反式脂肪' ,'鈉', '碳水化合物','資料來源','更新時間' ]]
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\set_detail\MOS_" + "set_detail" + str(i)  + ".csv", encoding="utf-8", index=False)
        print('表格出現了')
    except ValueError:
        pass
    i+=1

for (i) in range(10,100):
    print('目前第幾個食物', i)
    try:
        r = urlopen('http://www.mos.com.tw/menu/set_detail.aspx?id=M0'+ str(i))
        rl = BeautifulSoup(r)
        df = pd.read_html("http://www.mos.com.tw/menu/set_detail.aspx?id=M0" + str(i), encoding="utf-8")
        df1 = df[0].T
        df1.columns = df1.iloc[0]
        df1.drop([0], inplace=True)
        fn = rl.find("span", id="mainContent_lblName")
        df1['食物名'], df1['品牌'], df1['資料來源'], df1['更新時間'], df1['食用量'] = [fn.text, 'MOS BURGER',
                                                                       'http://www.mos.com.tw/index.aspx',
                                                                       '20190101', '一份']
        df2 = df1[['品牌', '食物名', '食用量', '熱量', '蛋白質', '脂肪','飽和脂肪', '反式脂肪', '鈉', '碳水化合物', '資料來源', '更新時間']]
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\set_detail\MOS_" + "set_detail" + str(i) + ".csv", encoding="utf-8", index=False)
        print('表格出現了')
    except :
        pass
    i += 1

time.sleep(5)
for i in range(100,1000):
    print('目前第幾個食物', i)
    try:
        r = urlopen('http://www.mos.com.tw/menu/set_detail.aspx?id=M' + str(i))
        rl = BeautifulSoup(r)
        df = pd.read_html("http://www.mos.com.tw/menu/set_detail.aspx?id=M"+ str(i), encoding="utf-8")
        df1 = df[0].T
        df1.columns = df1.iloc[0]
        df1.drop([0],inplace=True)
        fn = rl.find("span", id="mainContent_lblName")
        df2['食物名'],df2['品牌'], df2['資料來源'], df2['更新時間'],df2['食用量'] = [fn.text,'MOS BURGER', 'http://www.mos.com.tw/index.aspx', '20190101','一份']
        df3 = df2[['品牌','食物名','食用量', '熱量', '蛋白質','脂肪','飽和脂肪','反式脂肪' ,'鈉', '碳水化合物','資料來源','更新時間' ]]
        df3.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\set_detail\MOS_" + "set_detail" + str(i)  + ".csv", encoding="utf-8", index=False)
        print('表格出現了')
    except ValueError:
        pass
    i+=1

#創附餐資料夾
dn = 'Detail_1'
os.makedirs(dn)

#抓取富餐食物資訊
for i in range(1,10):
    print('目前第幾個食物', i)
    try:
        r = urlopen('http://www.mos.com.tw/menu/Detail.aspx?id=M00' + str(i))
        rl = BeautifulSoup(r)
        df = pd.read_html("http://www.mos.com.tw/menu/Detail.aspx?id=M00"+ str(i), encoding="utf-8")
        df1 = df[0].T
        df1.columns = df1.iloc[0]
        df1.drop([0],inplace=True)
        fn = rl.find("span", id="mainContent_lblName")
        df1['食物名'],df1['品牌'], df1['資料來源'], df1['更新時間'],df1['食用量'] = [fn.text,'MOS BURGER', 'http://www.mos.com.tw/index.aspx', '20190101','一份']
        df2 = df1[['品牌','食物名','食用量', '熱量', '蛋白質','脂肪','飽和脂肪','反式脂肪' ,'鈉', '碳水化合物','資料來源','更新時間' ]]
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\Detail_1\MOS_" + "Detail" + str(i)  + ".csv", encoding="utf-8", index=False)
        print('表格出現了')
    except ValueError:
        pass
    i+=1

for (i) in range(10,100):
    print('目前第幾個食物', i)
    try:
        r = urlopen('http://www.mos.com.tw/menu/Detail.aspx?id=M0'+ str(i))
        rl = BeautifulSoup(r)
        df = pd.read_html("http://www.mos.com.tw/menu/Detail.aspx?id=M0" + str(i), encoding="utf-8")
        df1 = df[0].T
        df1.columns = df1.iloc[0]
        df1.drop([0], inplace=True)
        fn = rl.find("span", id="mainContent_lblName")
        df1['食物名'], df1['品牌'], df1['資料來源'], df1['更新時間'], df1['食用量'] = [fn.text, 'MOS BURGER',
                                                                       'http://www.mos.com.tw/index.aspx',
                                                                       '20190101', '一份']
        df2 = df1[['品牌', '食物名', '食用量', '熱量', '蛋白質', '脂肪','飽和脂肪','反式脂肪' ,'鈉', '碳水化合物', '資料來源', '更新時間']]
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\Detail_1\MOS_" + "Detail"+ str(i) + ".csv", encoding="utf-8", index=False)
        print('表格出現了')
    except :
        pass
    i += 1

time.sleep(2)
for i in range(100,1000):
    print('目前第幾個食物', i)
    try:
        r = urlopen('http://www.mos.com.tw/menu/Detail.aspx?id=M' + str(i))
        rl = BeautifulSoup(r)
        df = pd.read_html("http://www.mos.com.tw/menu/Detail.aspx?id=M"+ str(i), encoding="utf-8")
        df1 = df[0].T
        df1.columns = df1.iloc[0]
        df1.drop([0],inplace=True)
        fn = rl.find("span", id="mainContent_lblName")
        df1['食物名'],df1['品牌'], df1['資料來源'], df1['更新時間'],df1['食用量'] = [fn.text,'MOS BURGER', 'http://www.mos.com.tw/index.aspx', '20190101','一份']
        df2 = df1[['品牌','食物名','食用量', '熱量', '蛋白質','脂肪','飽和脂肪','反式脂肪' ,'鈉', '碳水化合物','資料來源','更新時間' ]]
        df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\Detail_1\MOS_" + "Detail"+ str(i)  + ".csv", encoding="utf-8", index=False)
        print('表格出現了')
    except ValueError:
        pass
    i+=1

#先匯集成同一csv檔，方法如同subway

#讀取總csv檔
df = pd.read_csv('E:\Python 3.7\pyetl\Demodb0103/food\mos\mos_c.csv',encoding="big5")

#改欄位名
df= df.rename(columns={'品牌':'Brand', '食物名':'Name', '食用量':'Portions', '熱量':'Cal_kcal',
'蛋白質':'Protein_g', '脂肪':'Fat_g', '飽和脂肪':'SF_g','碳水化合物':'Cho_g','鈉':'Na_g','資料來源':'Resource', '更新時間':'UpdateTime', '反式脂肪':'TF_g'})
#合併欄位並新增
df['BraName'] = df['Brand']+"_"+df['Name']
#刪除資料的單位值
df["Na_g"]=df["Na_g"].str.replace('mg',' ')
df["Cal_kcal"]=df["Cal_kcal"].str.replace('Kcal',' ')
list1=['Protein_g','Fat_g','SF_g','TF_g', 'Cho_g']
for i in list1 :
    df[i]=df[i].str.replace('g',' ')
#單欄位值做除法，將mg轉成g(值先轉成數字)
#df['Na_g'] = df['Na_g'].map(lambda x: x / 1000)
#df['Na_g']= df.apply(lambda x: x['Na_g']/1000, axis=1)
df['Na_g'] = df['Na_g'].apply(pd.to_numeric)
df['Na_g'] = df['Na_g']/ 1000
#存成csv檔
df.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\mos\mos_e.csv" , encoding="big5", index=False)
