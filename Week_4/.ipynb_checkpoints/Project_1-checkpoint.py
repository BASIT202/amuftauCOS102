import pandas as pd

girls = {'Name': ['Evelyn','Jessica','Somto','Edith','Liza','Madonna','Waju','Tola','Aisha','Latifa'], 
         'Age':['17','16','17','18','16','18','17','20','19','17'],
         'Height':['5.5','6.0','5.4','5.9','5.8','5.5','6.1','6.0','5.7','5.5'],
         'Scores':['80','85','70','60','76','66','87','95','60','49']}

boys = {'Name':['Chimedu','Laim','Wissa','Gbenga','Abiola','Kola','Kunle','George','Thomas','Wesley'],
        'Age':['19','16','18','17','20','19','16','18','17','19'],
        'Height':['5.7','5.9','5.8','6.1','5.9','5.5','6.1','5.4','5.8','5.7'],
        'Scores':['74','87','75','68','65','78','87','98','54','60']}

girls_table = pd.DataFrame(girls)
print('Data for girls')
print(girls_table)

boys_table = pd.DataFrame(boys)
print('Data for boys')
print(boys_table)
