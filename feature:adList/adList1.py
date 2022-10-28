import pandas as pd
import re

id = []
es2 = []
es4 = []

df = pd.read_excel("/Users/songsumin/Dev/tutorial/learning_pair/addressList/Book1.xlsx", sheet_name = "Sheet1")

for row in range(131):
    es1 = df.iloc[row, 0]
    es2 = re.sub(r"\([^)]*\)",'', es1)
    es3 = es2.split('→')
    es4 = es4 + es3
    es4 = list(set(es4))

for i in range(len(es4)):
    id.append(f'{i}')
    
excel_data1 = {'주소' : es4}
print(excel_data1)  

df1 = pd.DataFrame(excel_data1,index = id, columns = ['주소'])
excel_writer = pd.ExcelWriter('/Users/songsumin/Dev/tutorial/learning_pair/addressList/Book2.xlsx', engine='openpyxl')
df1.to_excel(excel_writer, index=True, sheet_name='주소 리스트')
excel_writer.save()