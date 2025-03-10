import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df["species"] = iris.target

df["species"] = df["species"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

df.to_csv("iris_dataset.csv", index=False)

print("iris_dataset.csv")

# Please download Iris Dataset for Binary LDA - run this code