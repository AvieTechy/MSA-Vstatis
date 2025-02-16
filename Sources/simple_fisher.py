import numpy as np

def fisher_method(X, y):
    """
    Fisher's Linear Discriminant for binary classification.
    
    Parameters:
    X : numpy.ndarray : Feature matrix (n_samples, n_features)
    y : numpy.ndarray : Target vector (n_samples,)
    
    Returns:
    w : numpy.ndarray : Weight vector (n_features,)
    """
    class_labels = np.unique(y)
    if len(class_labels) != 2:
        raise ValueError("Fisher's method is only applicable for binary classification.")
    
    # Separate the data into two classes
    X1 = X[y == class_labels[0]]
    X2 = X[y == class_labels[1]]
    
    # Compute the mean vectors
    mean1 = np.mean(X1, axis=0)
    mean2 = np.mean(X2, axis=0)
    
    # Compute the within-class scatter matrices
    S1 = np.dot((X1 - mean1).T, (X1 - mean1))
    S2 = np.dot((X2 - mean2).T, (X2 - mean2))
    
    # Compute the within-class scatter matrix
    Sw = S1 + S2
    
    # Compute the weight vector
    w = np.dot(np.linalg.inv(Sw), (mean1 - mean2))
    
    return w

X = np.array([[2, 3], [3, 3], [4, 5], [5, 5], [1, 1], [2, 1], [3, 2], [4, 2]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])
w = fisher_method(X, y)
print(w)