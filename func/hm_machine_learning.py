import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sklearn
from sklearn.datasets import load_iris, load_boston, make_classification, make_regression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def regression_example():
    # Load Boston housing dataset
    boston = load_boston()
    X = boston.data
    y = boston.target

    # Split dataset into train and test subsets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize Linear Regression model
    reg = LinearRegression()

    # Train the model
    reg.fit(X_train, y_train)

    # Make predictions on test subset
    y_pred = reg.predict(X_test)

    # Evaluate the model
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

def classification_example():
    # Load iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split dataset into train and test subsets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize K-Nearest Neighbors Classifier model
    knn = KNeighborsClassifier(n_neighbors=3)

    # Train the model
    knn.fit(X_train, y_train)

    # Make predictions on test subset
    y_pred = knn.predict(X_test)

    # Evaluate the model
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

def clustering_example():
    # Generate synthetic dataset
    X, y = make_classification(n_samples=300, n_features=2, n_informative=2, n_redundant=0, n_classes=3, random_state=42)

    # Initialize K-Means Clustering model
    kmeans = KMeans(n_clusters=3)

    # Train the model
    kmeans.fit(X)

    # Plot the clusters
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, legend=False)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=200, alpha=0.5)
    plt.title("K-Means Clustering Example")
    plt.show()

def main():
    regression_example()
    classification_example()
    clustering_example()

if __name__ == "__main__":
    main()
