import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))  # Bishop (2006), Eq. 4.59

class LogisticRegressionLasso:
    def __init__(self, alpha=0.1, lr=0.01, epochs=1000):
        self.alpha = alpha  # L1 penalty strength (Tibshirani, 1996)
        self.lr = lr        # Learning rate (optimization parameter)
        self.epochs = epochs

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for epoch in range(self.epochs):
            linear_model = np.dot(X, self.weights) + self.bias
            predictions = sigmoid(linear_model) 

            
            dw = (1 / n_samples) * np.dot(X.T, (predictions - y)) + self.alpha * np.sign(self.weights)
            db = (1 / n_samples) * np.sum(predictions - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict_proba(self, X):
        return sigmoid(np.dot(X, self.weights) + self.bias)

    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)

    
if __name__ == '__main__':
    X = np.random.randn(1000, 5)  # Features: discharges, predicted rate, etc.
    y = (X.dot(np.array([0.5, -0.3, 0, 1.2, 0])) + np.random.normal(0, 0.1, 1000) > 0).astype(int)
    
    # Standardize (critical for Lasso)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)
    
    # Fit model