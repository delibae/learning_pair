import pickle

a = ['0_29','30_59','60_99','100_129','130_159','160_189','190_219','220_249','250_last']
path = './final_data/100_200/time_dict_'
path_1 = './final_data/100_200/error_list_'
time_dict = {}
for i in a:
    t_path = path + i + '.pickle'
    with open(t_path,'rb') as f:
        t = pickle.load(f)
    time_dict.update(t)

error_list_to = []

for i in a:
    e_path = path_1 + i + '.pickle'
    with open(e_path,'rb') as f:
        e = pickle.load(f)
    error_list_to.extend(e)

print(len(time_dict))
print(len(error_list_to))

