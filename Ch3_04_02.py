from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np


# do not edit this
# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Create a classifier and fit it to our data
k_list = [1, 42, 100, 250]

for i, k in enumerate(k_list):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)

    train_accur = knn.score(x_train, y_train)
    print("training accuracy: %f at k = %d" % (train_accur, k))
    
    test_accur = knn.score(x_test, y_test)
    print("testing accuracy: %f at k = %d \n" % (test_accur, k))
