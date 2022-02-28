#visualisasi hasil ConvexHull
import matplotlib.pyplot as plt
from myConvexHull import ConvexHull

import numpy as np
import pandas as pd
from sklearn import datasets

def menu():
    print("====== Pilih Data ======")
    print("1. Iris Sepal")
    print("2. Iris Petal")
    print("3. Wine")
    print("4. Breast Cancer")

menu()
opt = int(input("Pilihan anda >> "))
colors = ['b','g','r', 'c', 'm', 'y', 'k']

if opt == 1:
    data = datasets.load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    print(df.shape)
    print("Feature: ", data.feature_names)
    print("Target: ", data.target_names)
    df.head()

    plt.figure(figsize = (10, 6))
    plt.title('Sepal Width vs Sepal Length')
    plt.xlabel(data.feature_names[0])
    plt.ylabel(data.feature_names[1])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[0,1]].values

        hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi
    # ConvexHull Divide & Conquer

        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        for simplex in hull:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i % len(colors)])

    plt.legend()
    plt.savefig("./out/iris_sepal.png")
    plt.show()

elif opt == 2:
    data = datasets.load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    print(df.shape)
    print("Feature: ", data.feature_names)
    print("Target: ", data.target_names)
    df.head()

    plt.figure(figsize = (10, 6))
    plt.title('Petal Width vs Petal Length')
    plt.xlabel(data.feature_names[2])
    plt.ylabel(data.feature_names[3])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[2,3]].values

        hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi
    # ConvexHull Divide & Conquer

        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        for simplex in hull:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i % len(colors)])

    plt.legend()
    plt.savefig("./out/iris_petal.png")
    plt.show()
    
elif opt == 3:
    data = datasets.load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    print(df.shape)
    print("Feature: ", data.feature_names)
    print("Target: ", data.target_names)
    df.head()

    plt.figure(figsize = (10, 6))
    plt.title('Alcohol vs Malic Acid')
    plt.xlabel(data.feature_names[0])
    plt.ylabel(data.feature_names[1])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[0,1]].values

        hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi
    # ConvexHull Divide & Conquer

        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        for simplex in hull:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i % len(colors)])

    plt.legend()
    plt.savefig("./out/wine.png")
    plt.show()

elif opt == 4:
    data = datasets.load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    print(df.shape)
    print("Feature: ", data.feature_names)
    print("Target: ", data.target_names)
    df.head()

    plt.figure(figsize = (10, 6))
    plt.title('Mean Smoothness vs Mean Compactness')
    plt.xlabel(data.feature_names[4])
    plt.ylabel(data.feature_names[5])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[4,5]].values

        hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi
    # ConvexHull Divide & Conquer

        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        for simplex in hull:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i % len(colors)])

    plt.legend()
    plt.savefig("./out/breast_cancer.png")
    plt.show()
else:
    print("\nInput invalid.")