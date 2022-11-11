import pickle

with open('past_data/time_dict.pickle', 'rb') as f:
    data = pickle.load(f)

print(data)

with open('error_list.pickle', 'rb') as f:
    data2 = pickle.load(f)

print(data2)
