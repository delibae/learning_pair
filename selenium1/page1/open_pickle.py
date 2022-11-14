import pickle
import pandas as pd


with open('fixed_data/time_dict.pickle', 'rb') as f:
    time_dict = pickle.load(f)


#
# # print(len(data))
# #
# # with open('fixed_data/error_list1.pickle', 'rb') as f:
# #     data2 = pickle.load(f)
#
# # print(len(data2))
#
# # print(data)
#
print(len([k for k, v in time_dict.items() if v == -1]))
#
# def create_ad_list(path):
#     ex = pd.read_excel(path)
#     ad_list = ex['도로명'].to_list()
#     return ad_list
#
# ad_list = create_ad_list('Book3.xlsx')
#
# i = ad_list.index('경기 이천시 부발읍 경충대로2092번길 39-33 신일해피트리빌 1단지 101동 상가 102호')
# j = ad_list.index('경기 이천시 부발읍 경충대로2092번길 39-33')
#
# time_dict[f'{i}-{j}'] = 1
#
# print(len([k for k, v in time_dict.items() if v == -1]))
#
# with open('fixed_data/time_dict.pickle', 'wb') as fw:
#     pickle.dump(time_dict, fw)



