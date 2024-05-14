import numpy as np
def calculate(list):
    if len(list) != 9:
        raise ValueError("Nine numbers in this list")

    values = {}
    matrix = np.array(list).reshape((3, 3))
    values['mean'] = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()]
    values['variance'] = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()]
    values['standard deviation'] = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()]
    values['max'] = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()]
    values['min'] = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()]
    values['sum'] = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    return values


