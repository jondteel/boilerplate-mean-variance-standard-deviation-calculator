import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        myArr = np.array([list[0:3], list[3:6], list[6:9]])

        calculations = { }

        calculations['mean'] = [np.mean(myArr, axis=0).tolist(), np.mean(myArr, axis=1).tolist(), float(np.mean(myArr))]
        calculations['variance'] = [np.var(myArr, axis=0).tolist(), np.var(myArr, axis=1).tolist(), float(np.var(myArr))]
        calculations['standard deviation'] = [np.std(myArr, axis=0).tolist(), np.std(myArr, axis=1).tolist(), float(np.std(myArr))]
        calculations['max'] = [np.max(myArr, axis=0).tolist(), np.max(myArr, axis=1).tolist(), float(np.max(myArr))]
        calculations['min'] = [np.min(myArr, axis=0).tolist(), np.min(myArr, axis=1).tolist(), float(np.min(myArr))]
        calculations['sum'] = [np.sum(myArr, axis=0).tolist(), np.sum(myArr, axis=1).tolist(), float(np.sum(myArr))]

    return calculations