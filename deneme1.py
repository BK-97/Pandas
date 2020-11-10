import pandas as pd
from pandas import DataFrame

data = pd.read_json(r'result.json')
df = DataFrame(data,
               columns=['phone_name','phone_adress', 'comment_author', 'phone_price',
                        'comment_detail','comment_date', 'comment_point'])
# df = df.drop(columns="phone_adress")
# -------------------------
count = df['comment_detail'].str.split().str.len()
~(count == 1)
dropped = df[~(count <= 5)].copy()
cf = dropped[~dropped.comment_detail.str.contains("kargo|Kargo|KARGO")]
# tf = cf[~cf.phone_name.str.contains("iPhone 11 Pro Max")]
cf = cf[cf.comment_point != 0]
# tf = tf[tf.comment_point != 0]
# kf = tf[tf['phone_name'].str.contains("iPhone 11 Pro")]
kf = cf[cf['phone_name'].str.contains("iPhone")]
# kf.index = pd.Index(list(range(10)), name='phone_name')
print(kf)
kf.to_json(r'C:\Users\Burak\PycharmProjects\pandas\msd.json', orient='table')

# phone_name','comment_point','comment_detail','comment_author','comment_date','phone_adress
# booleans =[]
# for length in df.yor
# df.info()
# df[df['yor'].str.contains("telefon",na=False)]
# df.__contains__("telefon")
# abc = notlar.str.contains(pat='telefon')
# df['yor'].astype(str)
# df = df[df.yor != "Note"]
# cf = df[df['yor'].str.contains("telefon|Samsung")]
# df=df.drop(columns="yor")
# notlar.product_name = notlar.product_name.str.upper()
# print(notlar.product_name.str.contains('Samsung'.upper))
# df = pd.DataFrame(notlar, columns='product_name')
# notlar.columns = 'product_name'
