#用pandas讀取網頁所有表格
import pandas as pd
import os

#創資料夾
dn = 'subway4'
os.makedirs(dn)

#抓取所有subway食物營養資訊

for i in range(0,8):
    print("目前第幾個表格?", i)
    #抓取網頁的所有表格
    df = pd.read_html("http://www.twsubway.com.tw/GoWeb2/include/meals-nutrition.html", encoding="utf-8")
    #新增欄位
    df[i]['品牌'], df[i]['資料來源'], df[i]['更新時間'],df[i]['食用量'] = ['Subway'
        , 'http://www.twsubway.com.tw/GoWeb2/include/', '20190101','一份']
    df = df[i].rename(columns={'品牌': 'Brand', '食用量': 'Portions', '卡路里Calories(Kcal)': 'Cal_kcal',
                       '蛋白質Protein(g)': 'Protein_g', '總脂肪Total Fat(g)': 'Fat_g', '碳水化合物Carbohydrate(g)': 'Cho_g'
        , '重量Serving Size(g)': 'Intake_g','資料來源': 'Resource', '更新時間': 'UpdateTime'
        , '糖Sugars(g)': 'Sugar_g', '飽和脂肪Saturated Fat(g)': 'SF_g', '反式脂肪Trans Fat(g)': 'TF_g'})
    #存成csv檔
    df.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\subway4\subway" + str(i) + ".csv"
               , encoding="utf-8", index=False)
    i+=1
