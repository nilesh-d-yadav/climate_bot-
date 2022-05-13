
def datas():
    import matplotlib as mpl
    import numpy as np
    import matplotlib.pyplot as plt

    data = np.genfromtxt('global_data.csv', delimiter=',', dtype=None, skip_header=5, names=('date', 'value', 'anomaly'))
    plt.title("Global Land and Ocean Temperature Anomalies, June")
    plt.xlabel('year')
    plt.ylabel('degrees F +/- from average')
    plt.bar(data['date'], data['value'], color="blue")
    plt.show()