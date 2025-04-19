import pandas as pd

personal_list = {'ad' : ['Eylül', 'Suna', 'Banu','Melih','Özan', 'Özgur'],
                 'yas': [28,23,24,27,29,30],
                 'maas':[6000,8000,4000,1500,5000,9000]}

#print(type(personal_list))
df=pd.DataFrame(personal_list) #DataFrame gives us the data sequentially. Just like the tables on the database
print(df)

#We can also receive data in CSV format with DataFrame. For this, we can open a CSV file and read it with the read_csv() method.
#The method head() used for pulling whatever element you want from table .
#With method columns you can get the name of colons
#The method describe() is used for statistical ratios and informations like min, max and count of the elements in tables.
#Using this method dtypes() gives us the type of the any colons
#tail() method is the opposite of head() method : it returns data starting from the end.
#shape(colon, row) it logically works by rows and colons.
#sum() ,it returns sum of the all colons sequentially even strings
