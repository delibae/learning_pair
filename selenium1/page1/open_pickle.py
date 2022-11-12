import pickle

with open('past_data/100_300_data/time_dict.pickle_100_129', 'rb') as f:
    data = pickle.load(f)

print(len(data))

with open('past_data/100_300_error/error_list.pickle_100_129', 'rb') as f:
    data2 = pickle.load(f)

print(data2)

print(data)