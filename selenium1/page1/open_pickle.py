import pickle

with open('100_300_data/time_dict.pickle_160_189', 'rb') as f:
    data = pickle.load(f)

print(len(data))

with open('100_300_error/error_list.pickle_160_189', 'rb') as f:
    data2 = pickle.load(f)

print(len(data2))

print(data)