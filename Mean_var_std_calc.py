import numpy as np

def calculate(list):
  if len(list) == 9:
    calculations = {}
    array = np.array([list]).reshape(3,3)

    calculations['mean'] = [(array.mean(axis = 0).tolist()), (array.mean(axis = 1).tolist()), (array.mean())]
    calculations['variance'] = [(array.var(axis = 0).tolist()), (array.var(axis = 1).tolist()), (array.var())]
    calculations['standard deviation'] = [(array.std(axis = 0).tolist()), (array.std(axis = 1).tolist()), (array.std())]
    calculations['max'] = [(array.max(axis = 0).tolist()), (array.max(axis = 1).tolist()), (array.max())]
    calculations['min'] = [(array.min(axis = 0).tolist()), (array.min(axis = 1).tolist()), (array.min())]
    calculations['sum'] = [(array.sum(axis = 0).tolist()), (array.sum(axis = 1).tolist()), (array.sum())]

    return calculations

  raise ValueError("List must contain nine numbers.")
list = [0,1,2,3,4,5,6,7,8]
calculate(list)
