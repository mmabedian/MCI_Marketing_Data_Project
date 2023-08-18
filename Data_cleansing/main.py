import pandas as pd

prototype_final = pd.read_csv('prototype_final.csv')
TDataDF = pd.read_csv('mainData.csv', dtype={'0MAT_SALES': str})
MHDtaDF = pd.read_csv('MHfinal.csv', encoding='unicode_escape', dtype={'PROD_HIER': str, 'MAT_SALES': str})
DBData = pd.DataFrame()
#
TDataDF = TDataDF[TDataDF['0DOC_NUMBER'] != '']
#
TDataDF = TDataDF[TDataDF['0DOC_CURRCY'] == 'IRR']
#
for key in prototype_final.keys():
    if prototype_final[key][3] == 'Y':
        DBData[prototype_final[key.strip()][0]] = TDataDF[key.strip()]
#
# DBData['subtot'] = DBData['subtot5'] + DBData['subtot6']
#
subMHDF = MHDtaDF[['SALESORG', 'MAT_SALES', 'PROD_HIER']]
new_dict = {}
for i in range(len(subMHDF)):
    new_dict[(subMHDF['SALESORG'][i], subMHDF['MAT_SALES'][i])] = str(subMHDF['PROD_HIER'][i])
DBData['hierarchys'] = DBData.apply(lambda row: new_dict[(row['company_code'], row['mat_sales'])], axis=1)
#
DBData['creation_date'] = pd.to_datetime(DBData['creation_date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
DBData['price_date'] = pd.to_datetime(DBData['price_date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
DBData['cal_date'] = pd.to_datetime(DBData['cal_date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
#
DBData = DBData.dropna(subset=['doc_No'])
#
DBData.to_csv('DBData.csv', index=False)
