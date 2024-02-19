import coinmarketcap as CMC 
from CMC_Key import Key

O_CMC = CMC.CMC_Client(Key)

data  = O_CMC.listings_latest(start = 1, limit = 2)

print(data)

for i in data:
    print(i['id'])

