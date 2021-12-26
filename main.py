import numpy as np
from matplotlib import pyplot as plt


def NormalD(x, _mean, _var):
    return np.exp(-0.5 * ((x-_mean)/np.sqrt(_var))**2)/(np.sqrt(2*np.pi*_var))


def CreateRandomVar(_n):
    return np.random.rand(1, _n)[0, :]


def MeanOfArray(_array):
    _sum = 0
    for i in _array:
        _sum += i
    return _sum / len(_array)


def VarOfArray(_array):
    sum = 0
    for i in _array:
        sum += i**2
    return (sum / len(_array)) - (MeanOfArray(_array)**2)


def DrawMeanGraph(_n):
    values = []
    vars = CreateRandomVar(_n)
    sum = 0
    for i in range(int(_n)):
        sum += vars[i]
        values.append(sum / (i+1))
    x = list(range(0, _n))
    plt.xlabel("N")
    plt.ylabel("Mean")
    plt.title("Mean of N Times Iterated Uniform Random Variable Graph.")
    plt.plot(x, values, label="Means")


def DrawGaussianGraphs(_n, _color):
    array = np.sort(CreateRandomVar(_n))
    mean = MeanOfArray(array)
    var = VarOfArray(array)
    values = []
    for i in array:
        values.append(NormalD(i, mean, var))

    plt.xlabel("N")
    plt.ylabel("Probability Density")
    plt.plot(array, values, label="Gaussian Distribution " + str(_n) + " Iteration", color=_color)


def DrawGaussianGraphWBar(_n, _color):
    array = np.sort(CreateRandomVar(_n))
    mean = MeanOfArray(array)
    var = VarOfArray(array)
    values = []
    for i in array:
        values.append(NormalD(i, mean, var))
    barInterval = np.arange(array[0], array[-1], (array[-1] - array[0]) / _n)
    plt.bar(barInterval, values, (array[-1] - array[0]) / _n, color="none", edgecolor="black")
    plt.title("N : " + str(_n))
    plt.xlabel("N")
    plt.ylabel("Probability Density")
    plt.plot(array, values, label="Gaussian Distribution " + str(_n) + " Iteration", color=_color)


n = []
colors = ["red", "blue", "green"]

print("[Choose]\n[1] Draw Mean Graph\n[2] Draw Gaussian Graphs On Same Plot\n[3] Draw Gaussain Graph With Bar Graph")
choice = input("Choice: ")

if choice == "1":
    print("[N] number of iteration.\n")
    n.append(input("N: "))
    DrawMeanGraph(int(n[0]))
elif choice == "2":
    print("[Number of Graph]\n[1]\n[2]\n[3]\n")
    graphCount = input("Number of Graph: ")

    print("[N] number of iterations.\n")
    for i in range(int(graphCount)):
        n.append(input("N" + str(i+1) + ": "))

    for i in range(int(graphCount)):
        DrawGaussianGraphs(int(n[i]), colors[i])
elif choice == "3":
    print("[N] number of iterations.\n")
    n.append(input("N: "))
    DrawGaussianGraphWBar(int(n[0]), colors[0])
else:
    quit()

plt.show()