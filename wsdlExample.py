from zeep import Client
from zeep import helpers

import pandas as pd

import json

wsdl_url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?wsdl'

client = Client(wsdl_url)

response = client.service.CountryIntPhoneCode(sCountryISOCode= 'TR')

#json_response = helpers.serialize_object(response)
json_response = json.dumps(response)

#df = pd.DataFrame(json_response)

#print(response)


datas = {'Column1': [1, 2, 'A'], 'Column2': [4, 5, 6]}

df = pd.DataFrame(datas)

#for key, value in enumerate(datas):
for key, value in datas.items():
    print(f"Key: {key}, Value: {value}")


#Veri tabanına ekleme işlemi yaparken ayrıca nonen kontrolü yapmamıza gerek yok. Veri otomatik olarak veri tabanına null olarak atanıyor.


#connection = cx_Oracle.connect("kullanici_adı/parola@veritabani_adresi")

#cursor = connection.cursor()

sql = "INSERT INTO table_name (sutun1, sutun2, sutun3) VALUES(:1, :2, :3)"
#veri = (deger1, deger2, deger3)
#cursor.execute(sql, veri)

#connection.commit()#işlemi kaydet
#connection.close()#bağlantıyı kes

print(sql)