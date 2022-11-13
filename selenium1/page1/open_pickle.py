import pickle

with open('final_data/100_200/time_dict_160_189.pickle', 'rb') as f:
    data = pickle.load(f)

print(len(data))

with open('final_data/100_200/error_list_160_189.pickle', 'rb') as f:
    data2 = pickle.load(f)

print(len(data2))

print(data)

print(len([k for k, v in data.items() if v == -1]))

