import numpy as np



def detect_out_lier(dataset):
    outlier = []

    third_standard_deviation = 3

    mean = np.mean(dataset)
    standard_deviation = np.std(dataset)


    for i in dataset:
        z_score = (i-mean)/standard_deviation


        if np.abs(z_score) > third_standard_deviation:
            outlier.append(i)
    return outlier


if __name__ == '__main__':
    dataset = [10,12,12,14,12,11,14,13,15,10,10,100,12,14,14,15,13,13,14,125,15,10,11,14,12,14,15]

    outliers = detect_out_lier(dataset)
    print(outliers)