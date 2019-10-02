import numpy as np

def outlier(dataset):

    q1 ,q3 = np.percentile(dataset , [25,75])


    interquantile_range = q3-q1


    lower_bond = q1-(1.5*interquantile_range)
    upper_bond = q3+(1.5*interquantile_range)

    print(lower_bond)
    print(upper_bond)

    #lower_bond is 9.0 and upper bound is 17.0 , so anything outside of 9.0 and 17.0 is an outlier




if __name__ == '__main__':
    dataset = [10,12,12,14,12,11,14,13,15,10,10,100,12,14,14,15,13,13,14,125,15,10,11,14,12,14,15]

    sorted_dataset = sorted(dataset)

    outlier(sorted_dataset)
