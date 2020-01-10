import csv
import matplotlib.pyplot as plt

def get_xs_ys(source='punkty.csv'):
    xs = []
    ys = []
    with open(source, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for i in reader:
            yield i

for i in get_xs_ys():
    plt.scatter(i[0], i[1], s=2)
plt.xlim(0, 60)
plt.ylim(0,60)
plt.show()

