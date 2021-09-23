import Cell
import pickle
'''
with open("TabelsDict","rb") as f:
    while True:
        try:
            d=pickle.load(f)
        except EOFError:
            break
'''
def give_me_list_of_grid_dict():
    with open("TabelsDict", "rb") as f:
        while True:
            try:
                d = pickle.load(f)
            except EOFError:
                break
    return d


