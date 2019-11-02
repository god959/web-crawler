#用pandas讀取網頁所有表格
import pandas as pd
import os

#創資料夾
dn = 'subway2'
os.makedirs(dn)

#抓取所有網頁
i = 1
while True:
    print("目前第幾頁?", i)
    try:
        df = pd.read_html("http://www.twsubway.com.tw/tw/subway_nutrition-tw_0"+str(i)+".html", encoding="utf-8")

        #抓取每一個網頁的所有表格
        j=0
        while True:
            print("目前第幾個表格?", j)
            try:
                #針對每個表格做修改
                df2 = df[j].drop('重量(g)', axis=1)
                df2.columns = ['食物名', '熱量', '脂肪', '碳水化合物', '蛋白質']
                df2['品牌'], df2['資料來源'], df2['更新時間'],df2['食用量'] = ['Subway'
                    , 'http://www.twsubway.com.tw/GoWeb2/include/', '20190101','一份']
                df3 = df2[['品牌','食物名','食用量', '熱量', '蛋白質','脂肪', '碳水化合物','資料來源','更新時間' ]]
                df3.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\subway2\subway" + str(i) + "_" + str(j+1) + ".csv"
                           , encoding="utf-8", index=False)
            except:
                print("應該是沒表格了吧")
                break
            j = j + 1
    except:
        print("應該是到底了吧")
        break
    i = i+1