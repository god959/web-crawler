#用pandas讀取網頁所有表格
import pandas as pd
import os

#創資料夾
dn = 'subway2'
os.makedirs(dn)

#抓取所有subway食物營養資訊
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
                #取欄位名
                df[j].columns = ['食物名','重量', '熱量', '脂肪', '碳水化合物', '蛋白質']
                #新增欄位
                df[j]['品牌'], df[j]['資料來源'], df[j]['更新時間'],df[j]['食用量'] = ['Subway'
                    , 'http://www.twsubway.com.tw/GoWeb2/include/', '20190101','一份']
                #欄位排序
                df2 = df[j][['品牌','食物名','食用量','重量', '熱量', '蛋白質','脂肪', '碳水化合物','資料來源','更新時間' ]]
                #存成csv檔
                df2.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\subway2\subway" + str(i) + "_" + str(j+1) + ".csv"
                           , encoding="utf-8", index=False)
            except:
                print("應該是沒表格了吧")
                break
            j = j + 1
    except:
        print("應該是到底了吧")
        break
    i = i+1

#整合subway的csv檔
# 獲取當前路徑
cwd = os.getcwd()

# 要拼接的資料夾及其完整路徑，注意不要包含中文
## 待讀取批量csv的資料夾名稱
Folder_Path =  'subway2'
## 待儲存的合併後的csv的資料夾名稱
SaveFile_Path =  'subway2'
## 待儲存的合併後的csv名稱
SaveFile_Name = 'subway_z.csv'

# 修改當前工作目錄
os.chdir(Folder_Path)

# 將該資料夾下的所有檔名存入一個列表
file_list = os.listdir()

# 迴圈遍歷列表中各個CSV檔名，並追加到合併後的檔案
for i in range(0,16):
   df = pd.read_csv( file_list[i] )
   df.to_csv(cwd + '\\' + SaveFile_Path + '\\' + SaveFile_Name,encoding="utf_8",index=False, header=False, mode='a+')

#subway資料清洗
#讀取csv檔
df = pd.read_csv('E:\Python 3.7\pyetl\Demodb0103/food\subway2\subway_z',encoding="big5")
#重新命名欄位
df.rename(columns={'品牌': 'Brand', '食物名': 'Name', '食用量': 'Portions', '熱量': 'Cal_kcal',
                   '蛋白質': 'Protein_g', '脂肪': 'Fat_g', '碳水化合物': 'Cho_g','重量':'Intake_g',
                   '資料來源': 'Resource', '更新時間': 'UpdateTime'})
#合併欄位並新增
df['BraName'] = df['Brand']+"_"+df['Name']
#刪除資料的單位值,df["Fat_g"]=df["Fat_g"].str.replace('g',' ')
df['Cal_kcal'] = df['Cal_kcal'].map(lambda x: x.rstrip('Kcal'))
df['Na_g'] = df['Na_g'].map(lambda x: x.rstrip('mg'))
list1=['Protein_g','Fat_g','SF_g','TC_g', 'Na_g',]
for i in list1 :
    df= df[i] = df[i].map(lambda x: x.rstrip('g'))

#data['result'] = data['result'].map(lambda x: x.lstrip('+-')前.rstrip('aAbBcC'))後
df.to_csv("E:\Python 3.7\pyetl\Demodb0103/food\mos\mos_z1.csv" , encoding="utf-8", index=False)
