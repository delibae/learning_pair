import pickle

addressList = ['경기 이천시 부발읍 경충대로 1918-18' , '경기 이천시 신둔면 석동로 3', '경기 이천시 설성면 설가로 219', '경기 이천시 부발읍 경충대로1722번길 54', '경기 이천시 장호원읍 대서리 산 63-1']
recent1 = addressList[0:3]
recent2 = addressList[1:4]
recent3 = addressList[1:]

print(addressList)
print(recent1)
print(recent2)
print(recent3)

# address_dict = {addressList[0]: 0, addressList[1]: 1, addressList[2]: 2, addressList[3]: 3, addressList[4]: 4}
address_dict = {}
for i in range(len(addressList)):
    address_dict[addressList[i]] = i

convert_address_dict = {v: k for k, v in address_dict.items()}

time_dict = {'0-1': 30, '0-2': 40, '0-3': 10, '0-4': 90, '1-2': 60, '1-3': 80, '1-4': 25, '2-3': 5, '2-4': 15,
             '3-4': 45}

print(address_dict)
print(time_dict)

# # with open('addressList.pickle', 'wb') as f:
# #     pickle.dump(addressList, f, pickle.HIGHEST_PROTOCOL)
#
# with open('../data/recent1.pickle', 'wb') as f:
#     pickle.dump(recent1, f, pickle.HIGHEST_PROTOCOL)
#
# with open('../data/recent2.pickle', 'wb') as f:
#     pickle.dump(recent2, f, pickle.HIGHEST_PROTOCOL)
#
# with open('../data/recent3.pickle', 'wb') as f:
#     pickle.dump(recent3, f, pickle.HIGHEST_PROTOCOL)
#
# with open('../data/time_dict.pickle', 'wb') as f:
#     pickle.dump(time_dict, f, pickle.HIGHEST_PROTOCOL)
#
# with open('../data/address_dict.pickle', 'wb') as f:
#     pickle.dump(address_dict, f, pickle.HIGHEST_PROTOCOL)
#
#
#
# with open('../data/convert_address_dict.pickle', 'wb') as f:
#     pickle.dump(convert_address_dict, f, pickle.HIGHEST_PROTOCOL)
#
# print(convert_address_dict)