import pickle
with open('time_dict.pickle','rb') as f:
    time_dict = pickle.load(f)

import pandas as pd
def create_ad_list(path):
    ex = pd.read_excel(path)
    ad_list = ex['도로명'].to_list()
    return ad_list

addressList = create_ad_list('Book3.xlsx')

recent1 = addressList[0:3]
recent2 = addressList[1:4]
recent3 = addressList[1:]



# address_dict = {addressList[0]: 0, addressList[1]: 1, addressList[2]: 2, addressList[3]: 3, addressList[4]: 4}
address_dict = {}
for i in range(len(addressList)):
    address_dict[addressList[i]] = i

convert_address_dict = {v: k for k, v in address_dict.items()}

# time_dict = {'0-1': 30, '0-2': 40, '0-3': 10, '0-4': 90, '1-2': 60, '1-3': 80, '1-4': 25, '2-3': 5, '2-4': 15,
#              '3-4': 45}


print(addressList)
print(recent1)
print(recent2)
print(recent3)

print(address_dict)
print(time_dict)
print(convert_address_dict)

# with open('addressList.pickle', 'wb') as f:
#     pickle.dump(addressList, f, pickle.HIGHEST_PROTOCOL)

with open('../data/recent1.pickle', 'wb') as f:
    pickle.dump(recent1, f, pickle.HIGHEST_PROTOCOL)

with open('../data/recent2.pickle', 'wb') as f:
    pickle.dump(recent2, f, pickle.HIGHEST_PROTOCOL)

with open('../data/recent3.pickle', 'wb') as f:
    pickle.dump(recent3, f, pickle.HIGHEST_PROTOCOL)

with open('../data/time_dict.pickle', 'wb') as f:
    pickle.dump(time_dict, f, pickle.HIGHEST_PROTOCOL)

with open('../data/address_dict.pickle', 'wb') as f:
    pickle.dump(address_dict, f, pickle.HIGHEST_PROTOCOL)



with open('../data/convert_address_dict.pickle', 'wb') as f:
    pickle.dump(convert_address_dict, f, pickle.HIGHEST_PROTOCOL)

